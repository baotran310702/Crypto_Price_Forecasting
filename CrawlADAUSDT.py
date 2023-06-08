import pandas as pd;
import openpyxl;
import requests;
from datetime import datetime;


#create a new workbook
workbook = openpyxl.Workbook();
worksheet = workbook.active;

worksheet['A1'] =  'Open time';
worksheet['B1'] =  'Open';
worksheet['C1'] =  'High';
worksheet['D1'] =  'Low';
worksheet['E1'] =  'Close';
worksheet['F1'] =  'Volume';
worksheet['G1'] =  'Close time';
worksheet['H1'] =  'Quote asset volume';
worksheet['I1'] =  'Number of trades';
worksheet['J1'] =  'Taker buy base asset volume';
worksheet['K1'] =  'Taker buy quote asset volume';
worksheet['L1'] =  'Ignore';

#url apis binances
url = 'https://api.binance.com/api/v3/klines'
params = {
    'symbol': 'ADAUSDT',
    'interval': '1d',  # Lấy giá theo khoảng thời gian 1 ngày
    'startTime': '1553126400000',  # Ngày bắt đầu (Unix timestamp của ngày 21/03/2019)
    'limit':'1000'
}

params1 = {
    'symbol': 'ADAUSDT',
    'interval': '1d',  # Lấy giá theo khoảng thời gian 1 ngày
    'startTime': '1636828800000',  # Ngày bắt đầu (Unix timestamp của ngày 14/12/2021)
    'limit':'1000'
}



res = requests.get(url,params=params);
res1 = requests.get(url,params=params1);

#Binance trả về tối đa 1000 ngày (3 năm), nên ta sẽ lấy 2 lấy ở 2 khoảng thời gian khác nhau và nối nó lại

if(-1):
    data1 = res.json();
    data2 = res1.json();
    index = 2;
    for i in reversed(data2):                
        open_time = datetime.fromtimestamp(int(i[0])/1000);
        close_time = datetime.fromtimestamp(int(i[6])/1000);
        worksheet['A'+str(index)] =  open_time.strftime("%d-%m-%Y");
        worksheet['B'+str(index)] =  round(float(i[1]),3);
        worksheet['C'+str(index)] =  round(float(i[2]),3);
        worksheet['D'+str(index)] =  round(float(i[3]),3);
        worksheet['E'+str(index)] =  round(float(i[4]),3);
        worksheet['F'+str(index)] =  round(float(i[5]),3);
        worksheet['G'+str(index)] =  close_time.strftime("%d-%m-%Y");
        worksheet['H'+str(index)] =  round(float(i[7]),3);
        worksheet['I'+str(index)] =  round(float(i[8]),3);
        worksheet['J'+str(index)] =  round(float(i[9]),3);
        worksheet['K'+str(index)] =  round(float(i[10]),3);
        worksheet['L'+str(index)] =  i[11];
        index=index+1;
    for i in reversed(data1):                
        open_time = datetime.fromtimestamp(int(i[0])/1000);
        close_time = datetime.fromtimestamp(int(i[6])/1000);
        worksheet['A'+str(index)] =  open_time.strftime("%d-%m-%Y");
        worksheet['B'+str(index)] =  round(float(i[1]),3);
        worksheet['C'+str(index)] =  round(float(i[2]),3);
        worksheet['D'+str(index)] =  round(float(i[3]),3);
        worksheet['E'+str(index)] =  round(float(i[4]),3);
        worksheet['F'+str(index)] =  round(float(i[5]),3);
        worksheet['G'+str(index)] =  close_time.strftime("%d-%m-%Y");
        worksheet['H'+str(index)] =  round(float(i[7]),3);
        worksheet['I'+str(index)] =  round(float(i[8]),3);
        worksheet['J'+str(index)] =  round(float(i[9]),3);
        worksheet['K'+str(index)] =  round(float(i[10]),3);
        worksheet['L'+str(index)] =  i[11];
        index=index+1;


workbook.save('ADAUSDT.xlsx');

print('save file successfully');