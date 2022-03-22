import OpenDartReader
import pandas as pd
import time

# 인증키
api_key = '7c30288e8f6aa302edef11d0eed2f6a3313bbe4c'

# OpenDartReader 객체를 생성
dartInfo = OpenDartReader(api_key)

# file 경로
path = 'D:\\Sources\\financial_report\\재무제표2'

# 종목명
stock_name = '삼성전자'

df2 = pd.DataFrame(columns=['유동자산', '부채총계', '자본총계', '매출액', '매출총이익', '영업이익',
                            '당기순이익'], index=['1900-01-01'])

# '11013'=1분기보고서, '11012' =반기보고서, '11014'=3분기보고서, '11011'=사업보고서
reprt_code = ['11013', '11012', '11014', '11011']

for i in range(2016, 2022):
    current_assets = [0, 0, 0, 0]   # 유동자산
    liabilities = [0, 0, 0, 0]      # 부채총계
    equity = [0, 0, 0, 0]           # 자본총계
    revenue = [0, 0, 0, 0]          # 매출액
    grossProfit = [0, 0, 0, 0]      # 매출총이익
    income = [0, 0, 0, 0]           # 영업이익
    net_income = [0, 0, 0, 0]       # 당기순이익

    for j, k in enumerate(reprt_code):
        df1 = pd.DataFrame()
        report = dartInfo.finstate_all('005930', i, reprt_code=k, fs_div='CFS')

        if report is None:
            print("{}({})는 {}년도 보고서 없음".format('삼성전자', '005930', i))
            pass
        else:
            df1 = pd.concat([df1, report])
            # 재무상태표
            condition1 = (df1.sj_nm == '재무상태표') & (df1.account_nm == '유동자산')  # 유동자산
            condition2 = (df1.sj_nm == '재무상태표') & (df1.account_nm == '부채총계')  # 부채총계
            condition3 = (df1.sj_nm == '재무상태표') & (df1.account_nm == '자본총계')  # 자본총계

            current_assets[j] = float(df1.loc[condition1].iloc[0]['thstrm_amount'])
            liabilities[j] = float(df1.loc[condition2].iloc[0]['thstrm_amount'])
            equity[j] = float(df1.loc[condition3].iloc[0]['thstrm_amount'])

            if k == '11013':  # 1분기.
                path_string = str(i) + '년 1분기'
            elif k == '11012':  # 2분기
                path_string = str(i) + '년 2분기'
            elif k == '11014':  # 3분기
                path_string = str(i) + '년 3분기'
            else:  # 4분기. 1 ~ 3분기 데이터를 더한다음 사업보고서에서 빼야 함
                path_string = str(i) + '년 4분기'

            # 데이터프레임에 저장하는 부분
            df2.loc[path_string] = [current_assets[j], liabilities[j], equity[j],
                                    revenue[j], grossProfit[j], income[j], net_income[j]]
            df2.tail()  # 데이터프레임 끝에 저장한다.
        time.sleep(0.1)

df2.drop(['1900-01-01'], inplace=True)  # 첫 행 drop

# 엑셀로 저장
writer = pd.ExcelWriter(path + "\\" + "result_{}.xlsx".format('삼성전자'))
df2.to_excel(writer, sheet_name='Sheet1')

# Pandas writer 객체에서 xlsxwriter 객체 가져오기
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# 숫자 포맷 만들기
number_format = workbook.add_format({'num_format': '#,##0'})

# 컬럼에 포맷 적용
worksheet.set_column('B:D', 20, number_format)

## Pandas writer 객체 닫기
writer.close()
