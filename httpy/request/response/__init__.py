import json

from httpy.request.response._assert import Assert
from httpy.log.messages.request.response import ResponseLogger


class Response:
    """
    Response data from `requests.request` method.

    :param _r:
    :type _r: Response

    :param _et:
    :type _et: float
    """
    def __init__(self, _r, _et):
        self._r_bckp = _r
        self.execution_time = _et
        self.__proc(_r)

    def __proc(self, _r):
        """
        Transform the response from `requests.request` method in attributes of Response object. 

        :param _r:
        :type _r: requests.Response

        :rtype: void
        """
        self.status = _r.status_code
        self.reason = _r.reason
        self.content = _r.content.decode('utf-8')
        self.is_json = self.__is_json(self.content)
        self.json = json.loads(self.content) if self.is_json else None
        self.headers = _r.headers

        ResponseLogger.log_response_message(_r.request.method, _r.request.url, self.status, self.reason, self.headers, self.content)

        self._assert = Assert(self)

    def __is_json(self, _c):
        """
        Check if the content from the request is in json format.

        :param _c:
        :type _c: str

        :rtype: bool
        """
        try:
            _r_dict = json.loads(_c)

            return True

        except json.JSONDecodeError as err:
            return False
