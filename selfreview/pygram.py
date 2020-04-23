def allsum(mylist): 
    sum = 1
    for i in mylist: 
	    sum = sum+1
    return sum

sth_list = [1,2,3,4,5,6,7,8,9]
# print(allsum(sth_list))	

# intValue = 1
# print(type(intValue)) 
#output: <class 'int'>

str3 = """Hello   
World"""
# print(str3)


name = "라이언"
greeting = "안녕하세요 %s입니다" %name
introduce = "%d 세이고 키는 %.1f cm입니다" %(100, 200)
percent = "100%%" # 100%

introduce2 = "{age} 세,{height} cm입니다".format(age=10,height=100.0)
greeting2 = "안녕하세요 {name:*>7}입니다".format(name=name)
introduce3 = "키는 {height:_^10.1f}입니다".format(height=191.124)

print (greeting)
print(introduce)
print(percent)
print(introduce2)
print(greeting2)
print(introduce3)

greeting3 = f"안녕하세요 {name}입니다"
print (greeting3)