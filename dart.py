import OpenDartReader
import pandas as pd
import os
import FinanceDataReader as fdr
import time

# 한국 거래소에 상장된 주식 종목 리스트
# Symbol Market Name Sector	Industry ListingDate SettleMonth Representative	HomePage Region
stockList = fdr.StockListing("KRX").dropna()
# for code, name in stockList[['Symbol', 'Name']].values:
#     print(code, name)
# 인증키
api_key = '7c30288e8f6aa302edef11d0eed2f6a3313bbe4c'

# OpenDartReader 객체를 생성
dartInfo = OpenDartReader(api_key)

# file 경로
path = 'D:\\Sources\\financial_report\\재무제표'


# 재무제표 정보 추출 후 저장
def extract_info_and_save(dart, path, year, code, name, report_type, report_type_code):
    report = dart.finstate(corp=code, bsns_year=year, reprt_code=report_type_code)
    if report is None:
        pass
    else:
        if name not in os.listdir(path):
            os.mkdir(path + "\\" + name)

        report.to_excel(path + "\\" + "{}/{}년_{}.xlsx".format(name, year, report_type))

# TO_DO : 유일로보틱스, 388720, 보고서가 없는 경우, None 값에 의한 에러 수정
for code, name in stockList[['Symbol', 'Name']].values:
    for year in range(2021, 2022):
        for report_type, report_type_code in zip(["1분기보고서", "반기보고서", "3분기보고서", "사업보고서"],
                                                 ["11013", "11012", "11014", "11011"]):
            while True:
                try:
                    extract_info_and_save(dart=dartInfo
                                          , path=path
                                          , year=year
                                          , code=code
                                          , name=name.replace('.', '')
                                          , report_type=report_type
                                          , report_type_code=report_type_code)
                    time.sleep(0.5)
                    break

                except:
                    time.sleep(60)
