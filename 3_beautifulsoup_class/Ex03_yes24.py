from  bs4 import beautifulsoup
from urllib import request

html=request.urlopen('http://http://www.yes24.com/Product/Search?domain=ALL&query=python')
soup=beautifulsoup(html,'html.parser')

# 2
imgUrls=soup.select('#yesSchlist div.itemUnit img')
#print(imgUrls)
for imgUrl in imgUrls:
#이미지링크를 출력 : src
#책제목을 출력:olt
    imgPath=imgUrl.attrs['data-original']
    bookName=imgUrl.attrs['alt'].strip().replace('/','_')
    print(bookName,imgPath)
    request.urlretrieve(imgPath,'imgs/'+bookName+'.jpg')
#이미지 폴더 만들어야함