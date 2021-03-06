from requests import Session

from httpy.request import Request
from httpy.environment import Environment


class Api:
    def __init__(self, _o):
        """
        Initiate the Api object

        :param _o:
        :type _o: YAMLParser
        """
        self.session = Session()
        self.name = _o.name
        self.base_url = _o.base_url
        self.raw_requests = _o.requests
        self.requests = {}
        self.__load()
        self.environment = None

    def __getattr__(self, attr):
        """
        Get the requests as attributes by using their names

        :param attr:
        :type attr: str

        :rtype: Request
        :return:
        """
        if attr not in self.requests:
            raise AttributeError('Request with name %s not found in %s' % (attr, self.name))

        return self.requests[attr]

    def __load(self):
        """
        Load the raw requests and set them as Request object in Api.requests dict
        """
        for k, v in self.raw_requests.items():
            self.requests[k] = Request(self.base_url, k, v, self.session)

    def attach_environment(self, env):
        if type(env) != Environment:
            raise TypeError('Parameter env in Api.attach_environment must be of type Environment not %s' % type(env))
    
        self.environment = env
