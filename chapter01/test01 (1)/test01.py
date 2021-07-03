import random

print('숫자 맞추기 게임')
com = random.randint(1,10)
print(com)
while True:

    my = int(input('예상 숫자를 입력 하세요 :'))
    if my == com :
        print("~~ 성공 ~~")
        break
    elif my > com :
        print("더 작은 수를 입력 하세요")
    elif my < com :
        print("더 큰 수를 입력 하세요")

#[문제3] for 반복문을 이용한 수열 출력하기
# 1 ~100 사이에서 3의 배수이면서 2의 배수가 아닌 수를 한줄에 출력하고 누적합을 출력 하시오
#<출력 결과>
#수열  29 15 21 27 ~~~~~99
#누적합 = 867
# https://fullyalive.tistory.com/19?category=628624 식 잘나와있음

result=0
for n in range(1,101):
    if n % 3 ==0 and n % 2 !=0:
           print(n,end=' ')
           result +=n
print('\n합계= %d' % result)

tot = 0
print('수열:', end=' ')
for i in range(1,101):
    print(i)
    if i % 3 == 0 and i % 2 != 0 :
        print(i, end=' ')
        tot += i
print('\n누적합 = %d' % tot)

#[문제4] 중첩 반복문을 이용한 단어 타운트하기(word count)
#다음과 같은 multiline의 문자열 객체를 이용하여 단어를 추출하고 단어의 개수를 출력하시오.
multiline="""안녕하세요 파이썬 세계로 오신걸
환영합니다
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

<출력결과>
안녕하세요
파이썬
세계로
오신걸
환영합니다
파이썬은
---
언어입니다.

multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다
파이썬은 비단뱀처럼 매력적인 언어입니다."""
cnt=0
sents = []
words=[]
for line in multiline.split("\n"):
    sents.append(line)
    for word in line.split(" "):
        words.append(word)
        print(word)
        cnt+=1
print(sents)
print(words)
print("단어개수:", cnt)

(1) str 클래스 형식
str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])

# (2) str 클래스 간편 형식
str_var2 = 'string'
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var[-1])

lst=[1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[:i]) # i 전까지

x=list(range(1,11))
print(x)
print(x[:5]) #5미만까지 해라
print(x[-5:])   #x:y x는 숫자의 위치 y는 그냥 숫자 얘기하는거
print('index 2씩증가')
print(x[::2])
print(x[1::2])

a = ['백승엽','이병구','서동석','음영현','김호용']
print(a)

b= [10,20,a,5,True,'문자열']
print(b[0]) #10
print(b[2]) # a
print(b[2][0]) #
print(b[2][1:])

num = ['백','승','엽','이','다']
print(num)
print(len(num))

num.append('!')
print(num)

num.remove('!')
print(num)

num[2]='열'
print(num)

num.insert(5,'!')
print(num)

x = [10,20,30,40,50]
y = [60,70,80]
z = x+y
print(z)

x.extend(y)
print(x)

x.append(y)
print(x)

lst = [10,20,30,40,50,60]
result = lst * 2
print(result)

x = [1,2,3,4]
x1 = []
for xx in x:
    x1.append(xx*2)
print(x)
print(x1)

import random
r = []
for i in range(5):
    r.append(random.randint(1,5))
print(r)

if 4 in r :
    print('4있다')
else :
    print('4없다')

num = list(range(1,11))
print(num)

list2 = [i**2 for i in num if i % 2 ==0]
print(list2)

[1,2,3,4,5]

lst = [1,2,3,4,5]

for i in lst :
    # array = lst[i-1: ]
    # array.reverse()
    # print(array)
    print(lst[i-1: ])

lst = [1,2,3,5,4]
lst=sorted(lst, reverse=True)
for i in range(len(lst)):
    print(lst[i:])


#1 2 3 4 5
#0 1 2 3 4 여기는 위치 얘기하는거지
#i-1이니까 1부터 차례대로 대입하자 그러면  처음에 0 [0: ] 이렇게 되니까 0부터 끝까지 1 2 3 4 5
#그다음엔 2를 대입하자 그럼 [1:0]이 된다 그러면 숫자 2부터 끝까지 2 , 3, 4, 5

t = (10,)
print(t)

t2 = (1, 2, 3, 4, 5)
print(t2)

print(t2[-1], t2[2:4], t2[-5])

#t2[0] = 10

for i in t2:
    print(i,end=' ')

if 6 in t2 :
    print("\n6있음")
else:
    print("\n6없음")

lst=list(range(1,6))
t3=tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4)) #index는 현재 t3이  1 2 3 4 5 인데
# 4의 위치 정보를 알려달라! 4의 위치는     0 1 2 3 4 이므로 4의 위치는 3이니 값은 3으로 출력

s = {1,3,5,3,1}
print(s)
print(len(s))


for d in s :
    print(d, end=' ')
print()

s2= (3,6)
print(s.union(s2))

gender = ['남','여','남','여']

sgender=set(gender)
lgender=list(sgender)
print(sgender)
print(type(sgender))
print(type(lgender))

print(lgender[1])
print(lgender[0:3]) #3은 3 미만까지라는 뜻
#(1)dict 생성방법1
dic = dict(key1=100, key2=200, key3=300)
print(dic)
#(2)dict 생성방법2
person={'name':'홍길동','age':35,'address':'서울시'} #만약에 'name':'홍길동' 또 붙는다라고 가정한다면
print(person) # 키 :  값인데 키값은 중복이 안되 그냥 지워지는게지
print(person['name'])
print(type(dic),type(person))
#(3)원소 수정, 삭제, 추가
person['age'] =45
print(person)
#dict 원소 삭제
del person['address']
print(person)
#dict 원소추가
person['pay']=350
print(person)

print(person['age'])
print('age' in person)

for key in person.keys() :###############################################
    print(key)
for v in person.values() :###############################################
    print(v)

for i  in person.items() :###############################################
    print(i)

charset = ['abc','code','band','band','abc']

wc = {}
for key in charset:
    wc[key]=wc.get(key,0) + 1
print(wc)

name = ['홍길동','이순신','강감찬']
print('name address=',id(name))

name2=name
print('name2 address=',id(name2))

print(name)
print(name2)

name2[0] = "김길동"
print(name)
print(name2)

import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)
print(id(name))
print(id(name3))

print('name address=',id(name))
print('name3 address=',id(name3))

name[1] = "이순신장군"
print(name)
print(name3)

import random
dataset = []
for i in range(10):
    r=random.randint(1,100)
    dataset.append(r)
print(dataset)

vmax=vmin=dataset[0]

for i in dataset:
    if vmax<i:
        vmax=i
    if vmin>i:
        vmin=i

print('max=',vmax,'min=',vmin)

su=5
print("su 주소:",id(su))
dan=800
print("dan 주소:",id(dan))
print("금액:",su*dan)

#y=2.5 * g

fat=int(input("지방의그램을 입력하세요"))
carbo=int(input("탄수화물의 그램을 입력하세요"))
pro=int(input("단백질의 그램을 입력하세요"))

print("총칼로리:",9*(fat)+4*(carbo)+4*(pro),"cal")

word1 = "Korea"
word2 = "Baseball"
word3 = "Orag"
print("=========")
print(word1[0]+word2[0]+word3[0])

word1=input("첫번째단어")
word2=input("두번째단어")
word3=input("세번째단어")
print("약자 : "+word1[0]+word2[0]+word3[0])

a=10
b="10"
print(a!=b)


tot=int(input("짐의무게는 얼마입니까?"))

if  tot<10 :
    print("수수료는 없습니다.")
else :
    print("수수료는 10,000입니다")


while True:
    tot = int(input("짐의무게는 얼마입니까?"))
    if tot>10:
        price=tot/10
        price=int(price)
        print("수수료는",price*10000,"원입니다")
    else :
        print("수수료는 없습니다")

import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1,10)

# while True:
#     my = int(input('예상 숫자를 입력하시오 : '))
#
#     if com == my :
#         print('~~~성공~~~~')
#     elif com<my :
#         print('더 작은수 입력')
#     else :
#         print('더 큰수 입력')

result=0

for i in range(1,101) :
    if i % 3 == 0 and i % 2 != 0 :
        print(i,end=" ")
        result += i

print('\n누적합 : ', result)


multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다.
"""
word=multiline.split()
for x in word:
    print(x)
print("단어 개수 : ",len(word))