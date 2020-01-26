def parse_endpoint(base_url, endpoint):
    """
    Remove characters from the request config endpoint so it can be join with the api base url

    :param base_url:
    :type base_url: str

    :param endpoint:
    :type endpoint: str

    :rtype: str
    :return:
    """
    base_url = base_url if not base_url.endswith('/') else base_url[:-1]
    endpoint = endpoint if not endpoint.startswith('/') else endpoint[1:]

    return '/'.join([base_url, endpoint])


def parse_query_string(query, method, **kwargs):
    """
    Parse the query string configured to a query string that can be used `requests.request`

    :param query:
    :type query: str

    :param method:
    :type method: str

    :param kwargs:
    :type kwargs: dict

    :rtype: dict
    :return:
    """
    _r = {}

    if method.lower() == 'get':
        _r['params'] = query

    else:
        _r['data'] = query
        _r['headers'] = {}

        if 'json' in kwargs and kwargs['json']:
            _r['headers']['Content-Type'] = 'application/json'

        elif method.lower() == 'post':
            _r['headers']['Content-Type'] = 'application/x-www-form-urlencoded'

    return _r
