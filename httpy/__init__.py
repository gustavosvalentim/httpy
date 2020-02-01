import logging
from datetime import datetime

from httpy.yaml_parser import YAMLParser
from httpy.api import Api


class HTTPy:
    @staticmethod
    def config_logging():
        """
        Set logging settings for the API like log and format and level.
        """
        logging.basicConfig(format='%(asctime)s:%(levelname)s:[*] %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

    @staticmethod
    def load(yaml_file_path):
        """
        Load YAML config file and transform in a Api instance

        :param yaml_file_path:
        :type yaml_file_path: str

        :rtype: Api
        """
        HTTPy.config_logging()
        parse_yaml = YAMLParser(yaml_file_path)
        return Api(parse_yaml)