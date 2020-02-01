from yaml import YAMLObject

from httpy.environment import global_environment


def environment_yaml_constructor(loader, node):
    """
    Constructor for !env tag in YAML config.

    :param loader:
    :type loader: yaml.FullLoader

    :param node:
    :type node: yaml.Node

    :rtype: str
    """
    value = loader.construct_scalar(node)
    return '{{%s}}' % value