num1 = 100
num2 = 20
log_result = num1 >=50 or num2 <=10
print(log_result)

log_result = num1 >=50
print(log_result)

log_result = not(num1 >= 50)
print(log_result)
# 변수에 값 할당(=)
i = tot = 10 # i =10; tot = 10
i += 1 # i = i + 1
tot +=i # tot = tot + i
print(i, tot)

#같은줄에 중복 출력
print('출력1', end=' , ') # end='구분자'
print('출력2')

v1, v2, = 100, 200


num = input("숫자 입력 :")
print('num type:',type(num)) #<class 'str'>
print('num=', num)
print('num=', num*2)

#문자형 숫자를 정수형으로 변환
num1 =int(input("숫자입력:")) # str -> int (형변환)
print('num=', num1*2)

#문자형 숫자를 실수형으로 변환
num2 = float(input("숫자입력:")) #str -> float t(형변환)
result = num1 + num2 # 실수 = 정수 + 실수
print('result=', result)

#(1) value 인수
print("value=", 10+20+30+40+50)
#(2) sep인수 : 값과 값을 특수문자로 구분
print("010","1234","5678", sep="-")
#(3) end 인수
print("value=",10, end=",")
print("value=",20)

#(6) 외부 상수 인수
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f"%(name, age, price))
print("이름 : {}, 나이 : {}, data={}".format(name, age, price))
print("이름 : {1}, 나이: {0}, data={2}".format(age,name,price))

#(7) format 축약형(SQL문 작성)
uid = input("id input:")
query=f"select * from member where uid={uid}" # id input : >?hong
print(query)# memeber 테이블에서 uid가 hong인 레코드 검색  답 : select * from member where uid id= hong

#(1)문자열 색인
string="python"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

#(1)문자열 연산
print("python"+" program") #결합연산자
#print("python-"+3.7+".exe") #error 3.7은 숫자열 나머지는 문자열이니까 안된다
print("python-"+str(3.7)+".exe") #python-3.7.exe

print("-"*30) #반복연산자

oneline = "this is one line string"
print(oneline)
print(oneline[0:4])
print(oneline[:4]) # [:end-1] : 처음부터~
print(oneline[:]) #전체원소 전부다 this is one line string
print(oneline[::2]) #2의 배수  index : ti soeln tig

print('escape 문자 차단')
print('\n출력 이스케이프 문자') # \n 줄바꿈 가능
print('\\n출력 이스케이프 차단1')
print(r'\n출력 이스케이프 차단2')

var = 10 # if 블럭에서 사용될 변수
if var >= 5 : #조건식
    print('var=', var)
    print('var는 5보다 크다')

    print('조건이 참인 경우 실행')

    print('항상 실행')

#문제 c:\'aa'\"abc.txt" 되도록 출력하시오
'''
print("c:\\\'aa\'\\\"abc.txt\"") # c:\'aa'\"abc.txt"
'''
#문제 num 변수 대상 -> 등급게산(A:100~90 B:89~80 C:79~70, D:69~60, F:60미만 학점)
#출력 형식 => 점수 85, 등급 : B
num = 78
grade = "" #공백
if num >=90 :
    grade = "A"
elif num >=80 :
    grade = "B"
elif num >=70 :
    grade = "C"
elif num >=60 :
    grade = "D"
else :
    grade = "F"
print(f"점수1 : {num}, 등급 : {grade}")
print("점수2 : %d, 등급 : %s"%(num, grade))

num = 9 # 초기화
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
    print('result=', result)
# (2) 제 3항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >=5 else num + 2
print('result2=', result2) # 18

# (1) 카운터와 누적변수
cnt = tot = 0 # 변수 초기화 누적시키기위해
while cnt<5:    #True : loop 수행
    cnt+=1      # 카운터 변수(cnt= cnt+1) 처음값 1 cnt는 0이니까
    tot+=cnt    # 누적변수 : tot=tot+cnt cnt값 1이 고대로 내려와서 tot는 0이니까 여기 값을 1이된다.
    print(cnt,tot) #처음값은 1 1  위에 while 값이 성립이 되니가 다시 그 값 그대로 올라간다.

#실습 1~100 사이 3의 배수 합과 원소 추출하기
cnt=tot=0
dataset=[] # 빈 list

while cnt<100: #100회 반복
    cnt+=1 #카운터
    if cnt%3==0:
        tot+=cnt  #누적변수
        dataset.append(cnt)  #cnt 추가
print('1~100사이 3의 배수 합=%d'%tot)
print('dataset=',dataset)

