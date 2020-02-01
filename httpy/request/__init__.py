import time

import requests

from httpy.request.parsers import parse_endpoint, parse_query_string, parse_envvar
from httpy.log.messages.request import RequestLogger
from httpy.request.response import Response


class Request:
    """
    Create a dict like object to be used as kwargs in requests.request function

    :param base_url:
    :type base_url: str

    :param _r:
    :type _r: dict

    `_r` must have the following parameters `endpoint` and `method`. If `endpoint` is `/` then it will use base url
    """
    def __init__(self, base_url, _n, _r, _s):
        self.session = _s
        self.name = _n
        self.base_url = base_url
        self.raw = _r
        self.request_kwargs = self.__parse_request_kwargs()

    def __parse_request_kwargs(self):
        """ Transform the request configuration from the file to parameters that will be used by requests.request method. """

        if 'method' not in self.raw:
            raise KeyError('YAML config must contain method property')

        method = self.raw['method']
        endpoint = self.raw['endpoint'] if 'endpoint' in self.raw else ''
        request_kwargs = {
            'url': parse_endpoint(self.base_url, endpoint),
            'method': method.lower(),
            'headers': {}
        }
        endpoint_config = {}

        if 'json' in self.raw:
            endpoint_config['json'] = self.raw['json']

        if 'query' in self.raw:
            parse_query = parse_query_string(self.raw['query'], method, **endpoint_config)
            request_kwargs.update(parse_query)

        headers = self.raw['headers'] if 'headers' in self.raw else {}
        request_kwargs['headers'].update(headers)

        return request_kwargs

    def run(self):
        """ Run the request and get metrics like execution time, then return as a Response object. """
        parse_kwargs = parse_envvar(self.request_kwargs)
        req = requests.Request(**parse_kwargs)
        prep_request = req.prepare()

        RequestLogger.log_http(self.name, self.request_kwargs)

        t1 = time.time()

        _r = self.session.send(prep_request)

        t2 = time.time()
        execution_time = round(t2 - t1, 2)

        RequestLogger.log_exec_time(execution_time)

        response = Response(_r, execution_time)

        return response