import logging


class RequestLogger:
    @staticmethod
    def log_http(_n, _kw):
        headers = '\n'.join(['%s: %s' % (k, v) for k, v in _kw['headers'].items()])
        method = _kw['method'].upper()

        if 'json' in _kw:
            data = _kw['json']

        elif 'data' in _kw:
            data = _kw['data']

        elif 'params' in _kw:
            data = _kw['params']

        else:
            data = ''

        logging.info("""
Running {name}

{method} {url} HTTP/1.1
{headers}

{content}
            """.format(
                name=_n,
                method=method,
                url=_kw['url'],
                headers=headers,
                content=data
            )
        )

    @staticmethod
    def log_exec_time(_et):
        logging.info('Execution time: %.2fs' % _et)