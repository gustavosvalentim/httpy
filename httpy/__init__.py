from httpy.yaml_parser import YAMLParser
from httpy.api import Api


class HTTPy:
    @staticmethod
    def load(yaml_file_path):
        parse_yaml = YAMLParser(yaml_file_path)
        return Api(parse_yaml)
