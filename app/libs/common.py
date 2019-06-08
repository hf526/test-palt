"""
create by  --HF
"""
from flask import make_response, jsonify


class ToDict:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def Res(data, status=200, **kwargs):
    """
    构造响应方法，作为公共方法使用
    :param Response: 继承flask自带的方法
    :return:
    """
    headers = dict(
        content_type='application/json',
    )
    headers.update(kwargs)
    result = make_response(jsonify(data), status, headers)
    return result


