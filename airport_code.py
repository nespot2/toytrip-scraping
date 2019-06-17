"""
@author : jiye-choi
Scraping and Saving airport code from airportal website
"""

from common_def import str_encode
from common_def import get_html
from common_def import list_to_str
from common_def import write_file
from bs4 import BeautifulSoup


fixstr = ("공항명", "가", "히", "0", "A")
reqlist = str_encode(fixstr[0:3], "euc_kr", "euc_kr")

url = "http://www.airportal.co.kr/knowledge/airports/KfMain01.jsp?" \
      "df_area=" + reqlist[0] + "&df_search_target=name2" \
      "&df_search_keyword=" + reqlist[1] + "&df_search_keyword2=" + reqlist[2] + \
      "&proctype=list" \
      "&df_sort=name2" \
      "&df_desc=N"

# get total count
totalhtml = get_html(url)
soup = BeautifulSoup(totalhtml, 'html.parser')
totaltmp = soup.find("td", {"align":"left"}).string
total = totaltmp[2:totaltmp.index("건")]

# get airport code
url += "&df_start=0" + "&df_end=" + total + "&df_count=" + total
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
tr = soup.find("table", {"width": "660"}, 3).find_all("tr")[14:-2]

def soup_to_dict(soup):
      td_arr = soup.find_all("td")[2:]
      generator = map(lambda v: v.get_text().strip(), td_arr)
      return list_to_str(generator)


result = map(soup_to_dict, tr)

write_file("airport_code", result)







