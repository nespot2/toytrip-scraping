"""
@author : jiye-choi, netspot2
common module
"""
import requests
from urllib import parse


def get_html(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    return ""


def str_encode(strlist, enctype, quotetype):
    result = list(map(lambda v: parse.quote(v.encode(enctype), quotetype), strlist))
    return result


def list_to_str(gen):
    return "|".join(gen)


def write_file(filename, result):
    result = [i for i in result if i]
    with open(filename, "w", encoding='UTF8') as f:
        f.write("\n".join(result))

