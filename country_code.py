"""
@author : nespot2
위키피디아에서 국가코드 데이터 크롤링 후 파일에 저장하는 code
"""

from common_def import get_html
from common_def import list_to_str
from common_def import write_file
from bs4 import BeautifulSoup


def soup_to_dict(soup):
    td_arr = soup.find_all("td")
    generator = map(lambda v: v.get_text().strip(), td_arr)
    return list_to_str(generator)


html = get_html("https://ko.wikipedia.org/wiki/ISO_3166-1")

soup = BeautifulSoup(html, 'html.parser')

tr = soup.find("table", {"class": "wikitable sortable"}).find("tbody").findAll("tr")

head, *tail = tr

result = map(soup_to_dict, tail)

write_file("country_code", result)
