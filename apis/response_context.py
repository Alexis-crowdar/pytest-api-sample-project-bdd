class ResponseContext:
    def __init__(self):
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def __enter__(self):
        return self._response
