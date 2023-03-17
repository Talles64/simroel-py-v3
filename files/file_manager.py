import os
from glob import glob
import json


def structure(directory, extension):
    paths = glob(directory + "\*" + extension)
    elements = list(map(lambda path: path.split("\\")[-1].replace(extension, ""), paths))

    return dict(zip(elements, paths))


def get_files(directory, extension="\*.txt"):
    return glob(directory + extension)


class FileManager(object):
    def __init__(self):
        abs_path = os.path.abspath(os.getcwd())
        # TODO: arrumar esse path
        abs_path = abs_path[:abs_path.find("simroel-py-v3") + len('simroel-py-v3') + 1]
        self.data_dir = abs_path + "\data"

        self.data_dir = os.path.join(abs_path, "data")
        self.topologies_dir = os.path.join(self.data_dir, "topologies")
        self.osnr_dir = os.path.join(self.data_dir, "osnr")
        self.crosstalk_dir = os.path.join(self.data_dir, "crosstalk")
        self.parameters_path = os.path.join(self.data_dir, "parameters.json")
        self.confidence_interval_path = os.path.join(self.data_dir, "confidence_interval.csv")
        self.traffic_input_file_path = os.path.join(self.data_dir, "traffic_input_file.csv")

        topologies_paths = get_files(self.topologies_dir)
        topologies = list(map(lambda path: path.split("\\")[1].replace(".txt", ""),
                              topologies_paths))

        self.dict_topologies = dict(zip(topologies, topologies_paths))
        self.traffic_input_file_path = os.path.join(self.data_dir, "traffic_input_file.csv")
        self.dict_topologies = structure(self.topologies_dir, ".txt")
        self.dict_osnr = structure(self.osnr_dir, ".txt")
        self.dict_crosstalk = structure(self.crosstalk_dir, ".txt")

    def get_properties(self):
        print(self.parameters_path)
        with open(self.parameters_path, "r") as f:
            properties = json.load(f)
        return properties