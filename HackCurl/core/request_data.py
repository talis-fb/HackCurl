import json

from HackCurl.core.file_buffer import FileBuffer
from HackCurl.utils.types import IRequestValues


class RequestData:
    def __init__(self, datas: dict[str, IRequestValues], fileName=None):
        self.file = FileBuffer(fileName)
        self.datas = datas.copy()

    def _datas_to_json(self):
        return json.dumps(self.datas)

    def _update_datas(self, new: dict):
        for k in new.keys():
            self.datas[k] = new[k]

        self.file.overwrite(self._datas_to_json())

    def set_headers(self, news_headers: dict[str, str]):
        self._update_datas({"headers": news_headers})

    def set_body(self, new_body):
        self._update_datas({"body": new_body})

    def save(self):
        self.file.save()
