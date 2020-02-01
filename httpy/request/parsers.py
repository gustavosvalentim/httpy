import json
import logging

from httpy.environment import global_environment


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
        _r['headers'] = {}

        if 'json' in kwargs and kwargs['json']:
            try:
                json_dumps = json.dumps(query)
                _r['json'] = query
                _r['headers']['Content-Type'] = 'application/json'

            except json.JSONDEcodeError as err:
                logging.error('Error decondig json: %s' % str(query))
                

        elif method.lower() == 'post':
            _r['headers']['Content-Type'] = 'application/x-www-form-urlencoded'
            _r['data'] = query

    return _r


def parse_envvar(_o, env=global_environment):
    """
    Get values from dict and iterate through them recursively to replace all variables for values from the env parameter.

    :param _o:
    :type _o: dict

    :param env:
    :type env: Environment

    :rtype: dict
    """
    if isinstance(_o, dict):
        return dict([[k, parse_envvar(v)] for k, v in _o.items()])

    elif isinstance(_o, list):
        return [parse_envvar(_i) for _i in _o]
    
    elif isinstance(_o, str):
        return _o.replace('{{', '{').replace('}}', '}').format(**env.get())