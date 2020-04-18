import requests

r = requests.get(
    "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99"
)
rjson = r.json()
# print(rjson["RealtimeCityAir"]['row'])

gus = rjson["RealtimeCityAir"]["row"]

for gu in gus:
    if gu["IDEX_MVL"] < 100:
        print(gu["MSRSTE_NM"], gu["IDEX_MVL"])

