from bs4 import BeautifulSoup
import requests

url = "https://bscscan.com/address/0x831e899dd8f80c3f4ffa819c3fad8a34628b90d2#readContract"
page = requests.get(url)
dung = BeautifulSoup(page.text,"lxml")
print(dung)
link = soup.select(".cf-column")
print(link)