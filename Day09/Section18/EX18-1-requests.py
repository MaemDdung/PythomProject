'''
크롤링
외부 모듈 requsts
pip install requests

'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?'
# url = 'https://www.naver.com'
param = {'code':161967}
response = requests.get(url, params=param)
print(response.text)
