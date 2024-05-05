import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL指定
url="https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=46&block_no=47670&year=2020&month=5&day=2&view="
#バイナリデータ取得
response=requests.get(url)

#html解析
soup=BeautifulSoup(response.content,"html.parser")
#表データ取得（タグ付き）
all_data=soup.find_all(class_="data_0_0")
print(all_data)

#表データ取得（テキストのみ）
for toridasu in all_data:
    print(toridasu.text)

#表データをリストに格納（１６項目）１時のみ
list_data=[]

for t in range(16):
    list_data.append(all_data[t].text)

#データフレームのカラム名指定
df=pd.DataFrame(columns=['現地','海面','降水量','気温','露点','蒸気圧','湿度','風速','風向','日照','全天','降雪','積雪','天気','雲量','視程'])

#データフレームの１行目にリスト挿入
df.loc[0]=list_data

#時間の項目数の取得
hour=soup.find_all(style="white-space:nowrap")
h_list=[]

for num in hour:
    h_list.append(num.text)

print(h_list)
h_last=int(h_list[-1])
print(h_last)

#データフレームに各時間の表データをappend
list_data=[]
count=0
hour_num=h_last

for kk in range(hour_num):
    for t in range(16):
        list_data.append(all_data[count].text)
        count=count+1

    df.loc[kk]=list_data
    list_data=[]

print(df)

