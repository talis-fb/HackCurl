import json
import os

import HackCurl.core.request_data as RequestData
from HackCurl.core.file_buffer import FileBuffer

this_folder = os.path.dirname(__file__)
file_target_name = "file_request.json"
file_target_path = this_folder + "/" + file_target_name

FileBuffer.DEFAULT_PATH = this_folder


def test_setting_datas():
    dict_request = {
        "url": "www",
        "method": "GET",
        "headers": {"content-type": "json"},
        "body": {"ola": "mundo"},
    }

    request = RequestData.RequestData(dict_request, file_target_name)

    request.set_body({"a": 1})
    assert request.datas != dict_request

    dict_request["body"] = {"a": 1}
    assert request.datas == dict_request

    # TEST SAVING IN FILE
    with open(file_target_path, "r") as fileJson:
        assert fileJson.read() == ""

    request.save()
    with open(file_target_path, "r") as fileJson:
        assert fileJson.read() == request._datas_to_json()

    # Just to erase everthing of file
    with open(file_target_path, "w") as fileJson:
        pass
