import twstock
import pandas as pd


stock_num = input("請輸入股票代號:")
stock = twstock.Stock(stock_num)  #告訴twstock我們要查詢的股票
y , m = int(input("查詢年:")),int(input("查詢月:"))  
target_time = stock.fetch_from(y, m)#取用y/m至今每天的交易資料
tit_name = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change','Trascation']#設定表頭  

data = pd.DataFrame(columns=tit_name, data=target_time)
print(data)


df = pd.DataFrame(columns=tit_name, data=target_time)#整理成csv
filename = f'D:\python\stock.csv'#設定csv路徑
df.to_csv(filename)