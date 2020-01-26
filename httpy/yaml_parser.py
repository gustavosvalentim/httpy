from os import path

import yaml
from yaml.loader import SafeLoader


class YAMLParser:
    def __init__(self, yaml_file_path):
        if not path.isfile(yaml_file_path):
            raise FileNotFoundError('File %s not found' % yaml_file_path)

        with open(yaml_file_path) as _buf:
            yaml_content = _buf.read()

        self.parse_yaml = yaml.load(yaml_content, SafeLoader)

    def __getattr__(self, attr):
        if attr not in self.parse_yaml:
            raise KeyError('Key %s not found in %s YAML.' % (attr, self.parse_yaml['name']))

        return self.parse_yaml[attr]
