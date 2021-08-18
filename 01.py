#print("Hello Python")
'''print("Hello Python")'''
"""fdfdfdd"""
#print('Hello Python')

'''
a,b,c,d =0,0,0,0
hap= 0
a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))
hap = a+b+c+d
print("합계 => %d" % hap)

aa=[0,0,0,0]
hap=0
aa[0]=int(input("1번째 숫자 : "))
aa[1]=int(input("2번째 숫자 : "))
aa[2]=int(input("3번째 숫자 : "))
aa[3]=int(input("4번째 숫자 : "))
hap = aa[0]+aa[1]+aa[2]+aa[3]
print("합계 => %d" % hap)
'''
'''
aa =[]
aa.append(100)
aa.append(200)
aa.append(300)
aa.append(400)

print("리스트 변수 크기는 %d", len(aa))
print(aa)

bb=[]
for i in range(0,100):
    bb.append(i)
print(bb)
'''
'''
aa=[10,20,30,40]
print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1],aa[-2]))
print(aa[0:2])
print(aa[2:4])
print(aa[0:])
'''
'''
aa=[30,10,20]
print("현재의 리스트  : %s" %aa)
aa.append(40)
print("append 후의 리스트  : %s" %aa)
aa.pop()
print("pop 후의 리스트  : %s" %aa)
aa.sort()
print("sort 후의 리스트  : %s" %aa)
aa.reverse()
print("reverse 후의 리스트  : %s" %aa)
aa.insert(2,222)
print("insert(2,222) 후의 리스트  : %s" %aa)
print("20값의 위치 : %d" %aa.index(20))
aa.remove(222)
print("remove(222) 후의 리스트  : %s" %aa)
aa.extend([77,88,77])
print("extend(77,88,77) 후의 리스트  : %s" %aa)
print("77값의 개수 : %d" %aa.count(77))

aa =[[1,2,3,4],
    [5,6,7,8],
    [9,19,11,12]]

print(aa[0])
print(aa[0][0])
print(aa[1][2])
'''
'''
str ="파이썬 문자열"
print(str[0])
print(str[-1])

card = 'red',4,'python',True
print(card)
print(card[1])

one ="하나"
print(type(one))
one = '원'
print(one)
two ='둘'
print(type(two))
print(two[0])

#card = 'red',4,'python',True
a,b,c,d = card
print(a)
print(b)
print(c)
d-False
print(d)
'''
'''
dict ={'번호' : 10, '성명' :'장동건', '나이' :23, '사는곳' :'서울'}
print(dict)
print(type(dict))
print(dict['나이'])
dict['나이'] =24
print(dict['나이'])
dict['직업'] = '배우'
print(dict)
print(dict.keys())
print(dict.values())
print('사는곳' in dict)
del dict['사는곳']
print('사는 곳' in dict)
print(dict)
'''
'''
sum =0
for i in range(1,11,1):
    sum += i
print("sum : %d" %sum)
print("------")

sum =0
for j in range(1,11,1):
    if j<10:
        print("%d + " %j, end ="")
    elif j==10:
        print("%d = " %j, end="")
    sum += j
print("%d"%sum)
'''

'''
str="꿈은 이루어 진다."
i=0
while i<3:
    print(str)
    i += 1
print("-------")

i=int(input("반복 횟수 숫자를 입력합니다."))
j=0
flag =True
while flag:
    if i<=j:
        flag = False
    else:
        print(str)
    j = j+1
'''

'''
sum =0
for i in range(1,50,1):
    sum += i
    if sum>100:
        break;
sum = sum-i
print("%d" % sum)
print("-------")

sum, i=0,1
j=int(input("숫자를 입력합니다."))

while True:
    if i<= j:
        sum += i
        i = i+1
    elif j<i:
        break;

print("1에서 %d까지의 합은 %d입니다."%(j,sum))
'''
'''
def mydef01():
    i=10
    j=20
    print(10+20)

def mydef02(i,j):
    print(i+j)

def mydef03(i,j,p):
    if p=='+':
        print(i+j)
    elif p=='-':
        print(i-j)
    elif p=='*':
        print(i*j)
    elif p=='/':
        print(i/j)

mydef01()
mydef02(10,20)

n=int(input("첫번째 숫자를 입력합니다."))
m=int(input("두번째 숫자를 입력합니다."))
p=int(input("연산자를 입력합니다.(+,-,*,/)"))
mydef03(n,m,p)
'''

import module01

module01.mydef01()
module01.mydef02(10,20)