import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://movies.yahoo.com.tw/movie_intheaters.html')
# print(response.text)
# print(response.status)

rank=[]
name=[]

soup = BeautifulSoup(response.text, "lxml")
# 中文名子
chinese_name =soup.find_all("li")
# 英文名子
english_name =soup.find_all("a")
#
for index in chinese_name:

    if index.div != None:
        # print(index.div['class'])
       if (index.div['class']==['num']):
           rank.append(index.div.text)
           name.append(index.span.text)
        # print('電影名稱: '+str(index.span.text))

data = {
    'rank': rank,
    'name': name,
}

movie_df = pd.DataFrame(data)
# 輸出成csv檔在同一個目錄下
movie_df.to_csv('電影排行.csv', encoding = 'big5')
print(movie_df)


