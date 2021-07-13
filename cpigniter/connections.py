from pyignite import Client


class Connection:
    _client = None

    def __init__(
            self,
            host=None,
            port=0,
            ):

        self.host = host or "localhost"
        self.port = port or "10800"
        
        self.connect()

    def connect(self):
        self._client = Client()
        self._client.connect(self.host, self.port)

    def query(self, sql):
        return self._client.sql(sql)

