class Assert:
    """
    Assert for the API to use in the Response.

    :param response:
    :type response: requests.Response
    """
    def __init__(self, response):
        self._r = response

    def is_json(self):
        """
        Check if the content from the response is in JSON format.
        """
        if self._r.is_json:
            return True

        else:
            raise AssertionError('%s is not a valid JSON object.' % self._r.content)

    def contains(self, attr):
        """
        Check if response contains the attribute else raise AssertionError.

        :param attr:
        :type attr: str

        :rtype: bool
        """
        if attr in self._r.content:
            return True

        else:
            raise AssertionError('Response does not contains attribute %s.' % attr)
