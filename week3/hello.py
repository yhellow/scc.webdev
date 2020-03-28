print("hello world!")
# 주석 처리
# JS에서 썼었던 let const var 불필요
a = 3
b = 'sparta'
sparta_coding = 10
# snake case를 권장
c = a + b
c = a - b
c = a * b
c = a / b
c = a % b

# 변수타입
a = 'sparta coding'
b = "sparta coding"
a = 10.3
# boolean 첫글자는 무조건 대문자
a = True
b = False
a = [10, 'sparta', True, 11]
# 딕셔너리의 키 값은 무조건 감싸줘야한다
b = {
    "Sparta": 10
    "Coding": False
}
c = a[0]
d = b['sparta']

a = []
a, append(10)
# js 에서는 push
b = {}
b = ["sparta"] = 10

# 반복문
# for(let i=0 ; i<10 ; i++)
for i in range(10):
    print(i)
# 0 부터 시작해서 range 만큼 print
# 기본 문법은 colon + tab 한번

# 조건문
# if(){}
if a > 10:
    print(a)
elif b > 10:
    print(b)
else:
    print(c)


# 함수
# function 함수명(){}
def test(a=10):
    print(a)


# 실행 방법
test(10)
test(20)
