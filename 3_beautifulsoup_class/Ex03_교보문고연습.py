import requests

#교보문고>'파이썬'검색>국내도서

html=urlopen("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")
soup=BeautifulSoup(html,'html.parser')
prod_uten=soup.select('li.prod_item')
for prod_info in prod_item:
    imgTag=prod_info.select('img')
    print(imgTag)


