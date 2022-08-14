import HackCurl.core.request_data as RequestData
import json


def test_answer():

    dict_request = {
        "url": "www",
        "method": "GET",
        "headers": {"content-type": "json"},
        "body": {"ola": "mundo"},
    }

    request = RequestData.RequestData(dict_request, "primeiro.json")

    # dict_request["a"] = 2
    request.set_body({"a": 1})

    print(dict_request)

    assert request.datas != dict_request

    request.save()

    dict_request["body"] = {"a": 1}
    assert request.datas == dict_request
