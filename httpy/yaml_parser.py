from os import path

import yaml
from yaml.loader import FullLoader

from httpy.environment.yaml_constructor import environment_yaml_constructor


class YAMLParser:
    def __init__(self, yaml_file_path):
        if not path.isfile(yaml_file_path):
            raise FileNotFoundError('File %s not found' % yaml_file_path)

        _f = open(yaml_file_path)
        yaml.add_constructor(u'!env', environment_yaml_constructor)
        self.parse_yaml = yaml.load(_f, Loader=FullLoader)

        _f.close()

    def __getattr__(self, attr):
        if attr not in self.parse_yaml:
            raise KeyError('Key %s not found in %s YAML.' % (attr, self.parse_yaml['name']))

        return self.parse_yaml[attr]
