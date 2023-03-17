class PCE:
    def __init__(self,
                 fiber,
                 crosstalk,
                 router,
                 modulation,
                 assignment,
                 params):
        self.params = params
        self.fiber = fiber
        self.crosstalk = crosstalk
        self.router = router
        self.modulation = modulation
        self.assignment = assignment
        self.fes = None

        self.k_paths = params.get_k_routes()
        self.modulations = params.get_modulation()
        self.core_selection_fn = params.get_core_selection_fn()
        self.cores = params.get_cores()

    def process(self, pcep, fes, stats):
        self.fes = fes

        for conn in pcep.conn_list:
            i = 0
            routes = self.router.shortest_paths(conn.src, conn.tgt)

            while True:
                skip_cores = set()

                for modulation in self.modulations:
                    alloc_status = "resource"
                    cores = self.core_selection_fn(self.cores)
                    is_alloc = True

                    for core in cores:
                        if core not in skip_cores:
                            route = routes[i]

                            conn.modulation = modulation
                            conn.slots = self.modulation.calculate_n_slots(modulation, conn)

                            if is_alloc:
                                is_alloc = self.assignment.alloc(conn, self.fiber, route, core)
                                print('*'*50)
                                print(conn)
                                print('*' * 50)

                                alloc_status = "allocated" if is_alloc else "resource"

                                if alloc_status == "resource":
                                    skip_cores.add(core)
                                    is_alloc = True

                                else:
                                    break
                            else:
                                break

                    if (alloc_status == "allocated") or (len(skip_cores) == len(cores)):
                        break
                i += 1

                if (i >= self.k_paths) or (alloc_status == "allocated"):
                    break

            if stats.block_control(alloc_status):
                pcep.add_conn_assigned(conn)
                conn.release = conn.sim_clock + conn.hold
                fes.insert(conn, conn.release)
                if conn.sim_clock == -1:
                    raise ValueError("Conn.simclock == -1")

            else:
                conn.fiber_slot = -1

        pcep.conn_list.clear()

    def release_connection(self, connection, clock, stats):
        self.fiber.free(connection)
