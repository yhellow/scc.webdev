# 패키지를 가져오기 위해 import
import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print(rjson['RealtimeCityAir']['row'][0]['NO2'])

# requests.get(url)
# requests.post(url, data={"id":"username"})
print(rjson)

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu['MSRRGN_NM']
    mise_value = gu['IDEX_MVL']
    if mise_value < 100:
    # print(gu_name)
    print('gu_name' + ' : ' + str(mise_value))

# str = 강제로 문자열로 변환
