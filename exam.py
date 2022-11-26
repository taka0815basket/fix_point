import pandas as pd
import numpy as np
import datetime
from netaddr import *

# csvをdataframeで値を取得
df = pd.read_csv('log.csv', sep=',', names=('AccessDate','serverAdress','result'))
# print(df)

# 設問１のタイムアウトをしたものを表示する
# df.query('応答結果 == "-"'))

# データフレームを配列に変換
new_df = df[['AccessDate','serverAdress','result']].values
# print(new_df)    

count = 0
# 行数を取得
n = len(df)
# print(n)

for i in range(n):
    if new_df[i][2] == "-":
        count = 0
        print("故障状態のサーバーアドレス: " +new_df[i][1])
        if i==0:
            print("始めから故障していました")
        for j in reversed(range(i)):
            if (new_df[i][1] == new_df[j][1]):
                count += 1
                d1 = str(new_df[j][0])
                d2 = str(new_df[i][0])
                dt1 = datetime.datetime.strptime(d1, '%Y%m%d%H%M%S')
                dt2 = datetime.datetime.strptime(d2, '%Y%m%d%H%M%S')
                print("故障期間：{} ~ {}" .format(dt1, dt2))
                break
            if j == 0:
                if count == 0:
                    print("始めから故障していました")
            
print()
# 設問２
N=3
count = 0
for i in range(n):
    if new_df[i][2] == "-":
        # print("故障状態のサーバーアドレス: {}" .format(new_df[i][0]))
        count = 0
        for j in range(i,n):
            if new_df[i][1] == new_df[j][1]:
                if new_df[j][2] == "-":
                    count += 1
                    if count >= N:
                        d = str(new_df[i][0])
                        dt = datetime.datetime.strptime(d, '%Y%m%d%H%M%S')
                        print("故障状態になった時間：{}" .format(dt))
                        print("故障状態のサーバーアドレス: {}" .format(new_df[i][1]))
                        print("連続してタイムアウトをしたので故障です")
                        break
                else:
                    count = 0
                    
print()
#設問３
m = 3
t = 15
sum = 0
average = 0
count = 0

for i in range(n):
    if new_df[i][2] != "-":
        s = int(new_df[i][2])
        # print(i)
        sum = s
        count = 1
        for j in range(i+1,22):
            if new_df[i][1] == new_df[j][1]:
                if new_df[j][2] == "-":
                    count += 1
                    break
                
                s = int(new_df[j][2])
                sum += s
                count += 1
                if count >= m:
                    average = sum / m
                    count = 0
                    if average >= t:
                        d1 = str(new_df[i][0])
                        d2 = str(new_df[j][0])
                        dt1 = datetime.datetime.strptime(d1, '%Y%m%d%H%M%S')
                        dt2 = datetime.datetime.strptime(d2, '%Y%m%d%H%M%S')
                        print("サーバーアドレス：{}" .format(new_df[i][1]))
                        print("{} ~ {}" .format(dt1,dt2))
                        print("過負荷状態です。")
                    else:
                        d1 = str(new_df[i][0])
                        d2 = str(new_df[j][0])
                        dt1 = datetime.datetime.strptime(d1, '%Y%m%d%H%M%S')
                        dt2 = datetime.datetime.strptime(d2, '%Y%m%d%H%M%S')
                        print("サーバーアドレス：{}" .format(new_df[i][1]))
                        print("{} ~ {}" .format(dt1,dt2))
                        print("過負荷状態ではありません。")
                        
print()                   
# 設問４
for i in range(n):
    if new_df[i][2] == "-":
        count = 1
        ip = IPNetwork(new_df[i][1])
        for j in range(i+1,n):
            ip2  = IPNetwork(new_df[j][1])
            if ip == ip2:
                # print(ip.network)
                if new_df[j][2] == "-":
                    count += 1
                    # print(count)
                    if count >= m:
                        d1 = str(new_df[i][0])
                        d2 = str(new_df[j][0])
                        dt1 = datetime.datetime.strptime(d1, '%Y%m%d%H%M%S')
                        dt2 = datetime.datetime.strptime(d2, '%Y%m%d%H%M%S')
                        print("故障のサブネット: {}" .format(ip.network))
                        print("故障期間: {} ~ {}" .format(dt1, dt2))
                else:
                    count = 0
                    break