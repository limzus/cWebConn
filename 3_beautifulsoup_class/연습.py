import BeautifulSoup from bs4
import requests
#1

html=soup.urlopen'http://www.pythonscraping.com/pages/warandpeace.html'

녹색 글자만 추출하여 출력

-------------------------------------------
#2
http://www.pythonscraping.com/pages/page3.html

아이템과 가격을 추출


-------------------------------------------
#3
https://wikidocs.net/
 #
 # 1) 책 제목과 저자만 추출
 # 2) 이미지 다운


#8
import requests
from bs4 import BeautifulSoup

requests.session()  # 클라이언트가 접속했을때 한 세션이라고함.-한접속자체를 말함
login_info={
    "m_id":'hhkk',
    "m_passwd":'2didhd1234'
}
#파이썬은 딕셔너리 처리가 더 깔끔함

url_login='https://www.hanbit.co.kr/member/login_proc.php'
res=req.post(url_login, data=login_info)

url_mypage='https://www.hanbit.co.kr/myhanbit/myhanbit.html'
res=req.get(url_mypage)
print(res)
print('-'*50)
soup=BeautifulSoup(res.text,'html.parser')
mileage=soup.select_one('.mileage_section1 span')
print('마일리지:',mileage.get_text())