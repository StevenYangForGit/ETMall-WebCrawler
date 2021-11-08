import requests
import pandas as pd
import time
import random
import openpyxl

keyword = '亞帝芬奇'

url = 'https://www.etmall.com.tw/Search/Get'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

products_list = []

for i in range(15):
  data = {'keyword': keyword,
          'model[cateName]': '全站',
          'model[page]': 0,
          'model[storeID]': '',
          'model[cateID]': '-1',
          'model[filterType]': '',
          'model[sortType]': '',
          'model[moneyMaximum]': '',
          'model[moneyMinimum]': '',
          'model[pageSize]': 48,
          'model[SearchKeyword]': '',
          'model[fn]': '',
          'model[fa]': '',
          'model[token]': '',
          'page': i}

  requests.encoding = 'big-5'
  rqpost = requests.post(url,data = data,headers = headers)

  json_rqpost = rqpost.json()

  products = json_rqpost["searchResult"]["products"]

  products_list += products

  # time.sleep(5)
  RandomNum = random.uniform(1, 10)
  time.sleep(RandomNum)
  
df = pd.DataFrame(products_list)
#print(len(products_list))
#print(df)
  
df.to_excel("abc.xlsx")

  
