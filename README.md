# 기업 재무 데이터 추출하는 프로젝트
Python OpenDartReader 패키지를 사용하여 한국거래소에 상장된 기업의 재무제표를 추출하는 프로젝트

## install
```bash
pip install opendartreader
```
이미 설치되어 있고 업그레이드가 필요하다면 다음과 같이 설치합니다.
```bash
pip install --upgrade opendartreader 
```

## 상장기업 재무정보
```python
dart.finstate(corp, bsns_year, reprt_code='11011')
```
- corp (문자열): 검색대상 회사의 종목코드를 지정합니다. 고유번호, 회사이름도 가능합니다.
- bsns_year (문자열 혹은 정수값): 사업연도
- reprt_code (문자열): 보고서 코드 ('11013'=1분기보고서, '11012'=반기보고서, '11014'=3분기보고서, '11011'=사업보고서)


참조 : https://nbviewer.org/github/FinanceData/OpenDartReader/blob/master/docs/OpenDartReader_reference_manual.ipynb