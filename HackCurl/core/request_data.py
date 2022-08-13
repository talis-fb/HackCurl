IRequestData = str | dict[str, str]


class RequestData:
    def __init__(self, **datas: IRequestData):
        self.url = datas["url"]
        self.method = datas["method"]
        self.headers = datas["headers"]
        self.body = datas["body"]

    def setHeaders(self, headers: dict[str, str]):
        self.headers = headers
