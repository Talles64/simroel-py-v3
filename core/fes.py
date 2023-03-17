import heapq


class FESControl(object):
    def __init__(self):
        self.event_heap = []

    def insert(self, value, key):
        heapq.heappush(self.event_heap, (key, value))

    def is_empty(self):
        return len(self.event_heap) == 0

    def remove_min(self):
        if self.is_empty(): return False
        self.event_heap.remove(self.get_min())
        return True

    def compare_min(self, next_arrival):
        if self.is_empty(): return True
        return self.get_min()[0] > next_arrival

    def get_min(self):
        return heapq.nsmallest(1, self.event_heap, key=lambda kv: kv[0])[0]

    def get_index_min(self):
        return self.event_heap.index(self.get_min())