import requests

from httpy.request.parsers import parse_endpoint, parse_query_string


class Request:
    """
    Create a dict like object to be used as kwargs in requests.request function

    :param base_url:
    :type base_url: str

    :param _r:
    :type _r: dict

    `_r` must have the following parameters `endpoint` and `method`. If `endpoint` is `/` then it will use base url
    """
    def __init__(self, base_url, _r):
        self.base_url = base_url if not base_url.endswith('/') else base_url[:-1]
        self.raw = _r
        self.request_kwargs = self.__setup()

    def __setup(self):
        method = self.raw['method']
        request_kwargs = {
            'url': parse_endpoint(self.base_url, method),
            'method': self.raw['method'],
            'headers': {}
        }
        endpoint_config = {}

        if 'json' in self.raw:
            endpoint_config['json'] = self.raw['json']

        parse_query = parse_query_string(self.raw['query'], method, **endpoint_config)
        request_kwargs.update(parse_query)

        headers = self.raw['headers'] if 'headers' in self.raw else {}
        request_kwargs.update(headers)

        return request_kwargs

    def run(self):
        response = requests.request(**self.request_kwargs)

        return response
