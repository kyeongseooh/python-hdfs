import pandas as pd
from hdfs import InsecureClient
import os

# hdfs에 연결한 후 hdfs에 csv파일을 쓰고 읽어옴

client_hdfs = InsecureClient('http://adm1.io:9870', user='root')
item1 = ['kim', '20']
item2 = ['park', '30']
df = pd.DataFrame(data={'list1': item1, 'list2': item2})

with client_hdfs.write('/user/test.csv', encoding='utf-8') as writer:
    df.to_csv(writer)
with client_hdfs.read('/user/test.csv', encoding='utf-8') as reader:
    df = pd.read_csv(reader, index_col=0)
    print(df)
