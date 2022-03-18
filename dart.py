import OpenDartReader
import pandas as pd
import os

# 인증키
api_key = '7c30288e8f6aa302edef11d0eed2f6a3313bbe4c'

# OpenDartReader 객체를 생성
dart = OpenDartReader(api_key)

# 삼성전자 2021 재무제표 사업보고서(11013)
report = dart.finstate(corp='005930', bsns_year=2021, reprt_code='11013')

df = pd.DataFrame(report)


#excel 추출
path = 'D:\\Sources'
folder = 'financial_report'
fileName = path + "\\" + folder + "\\" + 'report_삼성전자.xlsx'
if folder not in os.listdir(path):
    os.mkdir(path + "\\" + folder)

df.to_excel(excel_writer=fileName)
