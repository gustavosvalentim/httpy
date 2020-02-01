class Environment:
    """
    Storage for variables to replace in the template.
    """
    def __init__(self, **kwargs):
        self.__data = kwargs

    def get(self, key=None, default=None):
        """
        Retrieve data from current environment.

        :param key:
        :type key: str

        :param default:
        :type default: any

        :rtype: any
        """
        if key and key not in self.__data:
            return default

        if not key:
            return self.__data
    
        return self.__data[key]

    def set(self, key, value=None):
        """
        Set a value to the current environment.

        :param key:
        :type key: str

        :param value:
        :type value: any
        """
        self.__data[key] = value

    def update(self, _d):
        """
        Update values in the current environment

        :param _d:
        :type _d: dict
        """
        self.__data.update(_d)


global_environment = Environment()
