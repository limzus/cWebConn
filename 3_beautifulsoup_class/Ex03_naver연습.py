"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res=req.urlopen(url)
print(res)

#파싱하기
soup=Beautifulsoup(res,'html.parser')
#유로/달러 추출하기
z=soup.select_one('div.head_info point_dn>span.value')
print(z)





