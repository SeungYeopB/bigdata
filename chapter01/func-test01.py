import random


def add_number(n1,n2):
    tot = n1 + n2
    return tot

# 문자 더하기
def add_text(t1,t2):
    return t1 + " " + t2

result_num = add_number(10,2)
print(result_num)

text1 = 'python'
text2 = 'Good!!!'
result_text = add_text(text1,text2)
print(result_text)

# 함수 만들기
# mul_num - 숫자 곱하기 (n1,n2)
# mul_text - 문자 곱하기 (t1 t2) t1 -문자, t2-숫자

def mul_num(n1,n2):
    tot = n1 * n2
    return tot

result_num = mul_num(10,2)
print(result_num)

def mul_text(n1,n2):
    tot_text = n1 * n2
    return tot_text
result_text = mul_text('python  ',3)
print(result_text)

# if 사용해서 n1 n2 값이 둘중에 하나가 숫자가 아니면 pass 명령을 실행하게 바꾸세요.

a = type(text1)
print(a)
print(a.)
# 숫자, 문자 인지?
# type 사용하면 숫자 문자 구분 가능한데 사용?
# isdigit(), isalpha()
# 키워드 : python 문자 숫자 구분하기

def mul_text1(n1,n2):
    tot_text = n1 * n2
    return tot_text

result_text = mul_text1('python',3)
print(result_text)
result_text = mul_text1('python', 'good')
print(result_text)

print(text1)
aaa = text1.isalpha()
if(aaa):
    print('문자입니다')
print(aaa)
text1 = 2
aaa = text1.isalpha()

if isdigit(n1) and isdigit(n2):
else: pass


from statistics import mean, variance
from math import sqrt

dataset = [2,4,5,6,1,8]
def Avg(data):
    avg =  mean (data)
    return avg

print('산술평균=', Avg(dataset))

def var_sd(data):
    avg = Avg(data)
    diff = [ (d-avg)**2 for d in data]

    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)

    return var, sd

v, s, = var_sd(dataset)
print('분산=', v)
print('표준편차=', s)

def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print("3변의 길이 : ", a,b,c)
pytha(2,1)
import random
def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0,1)
        if ( r == 1 ):
            result.append(1)
        else :
            result.append(0)
    return result
print(coin(10))

def Func1(name, *names):
    print(name)
    print(names)

Func1('홍길동','이순신','유관순')
from statistics import mean, variance, stdev

def Adder(x,y):
    add = x + y


    return add
print('add=', Adder(10,20))

print('add=', (lambda x,y:x+y)(10,20))

x =50 # 전역변수
def local_func(x):
    x += 50 #지역변수
local_func(x)
print('x=',x)

def global_func():
    global x
    x+=50 # x+50 = 100

global_func()
print('x=',x)


#(1) 일급함수
def a(): # outer
    print('a 함수')
    def b(): # inner
        print('b 함수')
    return b
b = a() # 외부함수 호출 : a 함수
b() # 내부 함수 호출 : b 함수
#(2)함수 클로저
data = list(range(1,101))
def outer_func(data):
    dataSet = data

    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot=', tot_val)
avg_val = avg(tot_val)
print('avg=',avg_val)



from statistics import mean #평균
from math import sqrt #제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]
#(1)외부함수 : 산포도 함수
def scattering_func(data): # outer
    dataSet = data # data 생성

    #(2)내부함수 : 산술 평균 반환
    def avg_func():
        avg_val=mean(dataSet)
        return avg_val
    #(3)내부함수 : 분산 반환
    def var_func(avg):
        diff=[(data-avg)**2 for data in dataSet]
        #print(sum(diff)) # 차의 합
        var_val=sum(diff)/(len(dataSet)-1)
        return var_val
    #(4)내부함수 : 표준 편차 반환
    def std_func(var):
        std_val=sqrt(var)
        return std_val
    #함수 클로저 반환
    return avg_func, var_func, std_func
avg,var,std = scattering_func(data)
#(5)내부함수 호출
print('평균', avg())
print('분산', var(avg()))
print('표준편차', std(var(avg())))

#(1) 중첩함수의 정의
def main_func(num):
    num_val = num # 자료생성
    def getter(): # 획득자 함수, return 있음
        return num_val
    def setter(value): # 지정자 함수 인수 있음
        nonlocal  num_val #nonlocal 명령어
        num_val = value

    return getter, setter # 함수 클로저 반환
#(2)외부 함수 호출
getter, setter = main_func(100) # num 생성
#(3)획득자 호출
print('num=', getter()) #획득한 num 확인    num=100

#(4)지정자 획득
setter(200) #num값 수정
print('num=', getter()) #num 수정 확인



#(1) 래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요!') # 시작 부분에 삽입
        func()  # 인수로 넘어온 함수(hello)
        print('잘가요!') # 종료 부분에 삽입
    return decorated # 클로저 함수 반환
#(2) 함수 장식자 적용
@wrap
def hello():
    print('hi ~ ', '홍길동')
#(3) 함수 호출
hello()

#(1) 재귀함수 정의 :  1-n 카운트
def Counter(n):
    if n == 0:
        return 0
    else :
        Counter(n-1)
        print(n, end=' ')
#(2) 함수 호출1
print('n=0 : ', Counter(0))
#(3) 함수 호출2
Counter(5)


#(1)재귀함수 정의 : 1 ~ n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n == 1 : #종료 조건
        return 1
    else :
        result = n + Adder(n-1) # 재귀호출

        print(n, end=' ') # (4) 스택 영역 2,3,4,5
        return result
#(2) 함수 호출1
print('n=1 : ', Adder(1))
#(3) 함수 호출2
print('\nn=5 : ', Adder(5))

################while 문##############################
def StarCount(height):
    h_cnt = s_cnt = 0
    while(h_cnt < height):
        h_cnt+=1
        print('*' * h_cnt)
        s_cnt+=h_cnt
    return s_cnt

height = int(input('height : '))
# start 개수 출력
print('start 개수 : %d'%StarCount(height))
################for문####################
def StarCount(height):
    h_cnt = s_cnt = 0

    for i in range(height):
        cnt=i+1
        #h_cnt+=cnt
        print('*' * cnt)
        s_cnt+=cnt

    return s_cnt

height = int(input('height : '))
# start 개수 출력
print('start 개수 : %d'%StarCount(height))



def bank_account(bal):
    balance = bal # 잔액 초기화(1000)

    def getBalance() : # 잔액 확인(getter)
        return balance

    def deposit(money): # 입급하기(setter)
        nonlocal balance  # outer 변수지정
        balance += money

    def withdraw(money): #출금 하기(setter)
        nonlocal balance
        if balance < money :
            print('잔액이 부족합니다.')
        else:
            balance -=money

    return getBalance, deposit, withdraw
getBalance, deposit, withdraw = bank_account(1000) #num 생성
print('Balance = ', getBalance()) #num = 1000
deposit(15000) # 입금
print('Balance = ', getBalance())
withdraw(3000) # 출금
print('Balance = ', getBalance())
withdraw(23000) # 출금
print('Balance = ', getBalance())

#패토리얼(Factorial)을 계산하는 재귀함수의 빈 칸을 채우시오
#예)5!(5*4*3*2*1)=120
def Factorial(n):
    if n == 1 : #종료 조건
        return 1
    else:
        result = n * Factorial(n-1)
        print(n, end=' ')
        return result
print('n=1 : ', Factorial(1))
print('n=2 : ', Factorial(2))
print('n=3 : ', Factorial(3))
print('n=4 : ', Factorial(4))
print('\nn=5 : ', Factorial(5))
result_fact = Factorial(5)
print('패토리얼 결과:', result_fact)




def strcheck(a):
    if a.isalpha():
        return 'alpha'
    elif a.isdigit():
        return 'digit'

c=input('input\n')
while c!='quit':
    print(c+' is '+strcheck(c)+'\n')
    c=input('input\n')

def mul_text(t1,t2):
    if str(t1).isalpha() and str(t2).isalpha():
        pass
    else:
        total = t1 * t2
        return total
result = mul_text(2,10)
print(result)

result=mul_text('python','good!')
print(result)

result=mul_text('python','good')
print(result)

def mul_text(t1,t2):
    if type(t1) == str and type(t2)==str:
        pass
    else:
        total = t1 * t2
        return total
result = mul_text(2,10)
print(result)

result=mul_text('python','good!')
print(result)

result=mul_text('python','good')
print(result)


