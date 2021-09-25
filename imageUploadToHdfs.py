import pandas as pd
from hdfs import InsecureClient
import os
import io
import matplotlib.pyplot as plt
from PIL import Image

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

# 읽은 데이터로 plot을 그려 hdfs 저장

client_hdfs = InsecureClient('http://adm1.io:9870',user='root')
with client_hdfs.read('/user/root/mat', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader, header = None)
x = df[0]
y = df[1]
plt.plot(x, y, 'g^') 
buf= io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
with client_hdfs.write('/user/root/mat_img.png', overwrite=True) as writer:
    writer.write(buf.getvalue())
buf.close()

# hdfs 저장한 plot image를 읽어옴

client_hdfs = InsecureClient('http://adm1.io:9870',user='root')
with client_hdfs.read('/user/root/mat_img.png') as reader:
    buf = reader.read()

data_io = io.BytesIO(buf)
img = Image.open(data_io)  
img