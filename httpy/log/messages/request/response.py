import logging


class ResponseLogger:
    @staticmethod
    def log_response_message(method, url, status, reason, headers, data):
        """
        Log message http received

        :param method:
        :type method: str

        :param url:
        :type url: str

        :param status:
        :type status: int

        :param reason:
        :type reason: str

        :param headers:
        :type headers: dict

        :param data:
        :type data: any
        """
        s_headers = '\n'.join(['%s: %s' % (k, v) for k, v in headers.items()])
        logging.info("""

{method} {url} {status} {reason}
{s_headers}

{data}

        """.format(
            method=method,
            url=url,
            status=status,
            reason=reason,
            s_headers=s_headers,
            data=data
        ))