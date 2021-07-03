#(1) random module 추가
import random
help(random) #모듈 도움말

#(2) random모듈의 함수 도움말
help(random.random)

#(3) 0 - 1 사이 난수 실수
r = random.random()
print('r=',r) #r=0.3940

#[실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt =0
while True:
    r=random.random()
    print(random.random())
    if r<=0.01:
        break # loop exit
    else:
        cnt +=1
        print('난수 개수=',cnt)  # 난수개수 = 9개


#(1) random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices) # 모집단에서 k 크기 목록 반환

#(2) 이름 list에 전체이름, 특정이름 출력
names=['홍길동','이순신','유관순']
print(names) #전체이름
print(names[2]) #, 특정 이름 출력

#(3) list에서 자룡 유무 확인하기
if '유관순' in names:
    print('유관순 없음')
else:
    print('유관순 있음')

#(4) 난수 정수로 이름 선택하기
idx=random.randint(0,2)
print(names[idx])

i=0
while i<10:
    i+=1 #카운터
    if i==3:
       continue #다음문장 skip
     if i==6: #탈출 조건
        break #exit
    print(i,end='')

#(1) 문자열 열거행객체 이용
string = "홍길동"
print(len(string)) #문자길이 : 3
for s in string : # 1문자 -> 변수 넘김 : 3회
    print(s,end=',') # 홍,길,동으로 출력해보기

#(2) list 열거형객체 이용
lstset = [1,2,3,4,5] # 5개 원소를 갖는 열거행객체

for e in lstset :
    print('원소:', e)

i=0
for s in string:
    i+=1
    if i==3:
        print(s,end='')
    else:
        print(s,end=',')


num1 = range(10)  # range(start)
print('num1:', num1)
num2 = range(1, 10)  # range(start, stop)
print('num2:', num2)
num3 = range(1, 10, 2)  # range(start, stop, step)
print('num3:', num3)

for n in num1:
    print(n,end='')
print()
for n in num2:
    print(n,end='')
print()
for n in num3:
    print(n,end='')

#(1) list에 자료 저장하기
lst=[]#빈 list만들기
for i in range(10): #0~9
    r=random.randint(1,10) #난수 발생
    lst.append(r) #난수 저장

print('lst=',lst) #난수 출력

#(2)list에 자료 참조하기
for i in range(10): #0~9
    print(lst[i]*0.25) #난수*0.25

# 구구단 출력 : range() 함수 이용
#(1) 바깥족 반복문
for i in range(2, 10):
    print('~~~ {}단 ~~~'.format(i))

    #(2)안쪽 반복문
    for j in range(1, 10):
        print()

# 구구단 출력 : range() 함수 이용
print("==============")
print("구    구     단")
print("==============")
for i in range(1,10):
    #바깥쪽 영역
    print("---------------")
    print(' {}단 출력 '.format(i))
    print("---------------")
    for j in range(1,10):
        print('%d * %d = %d' % (i, j, i * j))
print("===============")

string = """나는 홍길동 입니다.
주소는 서울시 입니다
나이는 35세 입니다"""

sents = [] #문장 저장
words = [] #단어 저장
#(1) 문단 -> 문장
for sen in string.split(sep="\n"):
    sents.append(sen)
    for word in sen.split():
        words.append(word)

print('문장:', sents)
print('문장수:', len(sents))
print('단어:', words)
print('단어수:', len(words))

num1=10
num2=20

bool_result=num1 == num2 #두 변수의 값이 같은지 비교
print(bool_result)
bool_result=num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

bool_result=num1>num2
print(bool_result)
bool_result=num1>=num2
print(bool_result)
bool_result=num1<num2
print(bool_result)
bool_result=num1<=num2
print(bool_result)

v1, v2 = 100, 200
v2,v1=v1,v2
print(v1,v2)

#패킹(packing) 할당
lst=[1,2,3,4,5]
v1,*v2=lst
print(v1,v2) # 1 [2,3,4,5]

*v1,v2=lst
print(v1,v2) # [1,2,3,4] 5

#  %d 10진수 정수
#  %o 8진수 정수
#  %x 16진수 정의
#  %f 실수(%f전체자릿수.소수점자릿수)
#  %s 문자열
#  %c 단일 문자열

#(4) format(0)함수 인수 : format(value, "format")
print("원주율=",format(3.14159, "8.3F"))  # 원주율= 3.142
print("금액=", format(10000,"10d"))   # 금액 =   10000
print("금액=", format(125000, "3,d"))  # 금액 = 125,000

#(5)양식문자 인수 : print( "%양식문자" %(값))
name="홍길동"
age=35
price=125.456
print("이름: %s, 나이 : %d, data = %.2f" %(name,age,price)) #이름 : 홍길동, 나이 : 35, data = 125.46


#(1) 특정 글자 수 반환
oneLine ="this is one line string"
print('t  글자 수 :', oneLine.count('t'))

#(2)접두어 문자 비교 판단
print(oneLine.startswith('this'))

#(3)문자열 교체
print

# \n 줄바꿈처리

# \t Tab 키 처리가능

# \r   캐리지 리턴 처리(다음줄 첫 칸으로 이동 가능)
# \f   폼 피드 처리(한 페이지 넘김 기능)
# \b   백스페이스 처리(back space 키 기능)
# \\   문자 "\"처리
# \'   문자' 처리
# \"   문자" 처리
# \000 널문자 처리

#<처리조건>
#<조건1> 수량 변수 : su = 5
#<조건2> 단가 변수 : dan=800
#<조건3> su,dan 변수 주소 확인
#<조건4> 금액 계산=수량 x 단가
#<조건5> 기타 세부내용<출력 화면 예시>참고


#<출력 화면 예시>
#su 주소 : 1858560352
#dan 주소 : 2241324818224
#금액 = 4000

#2차방정식 : y= 2.5*x제곱 + 3.3*x+6 (단 x=2일떄)
#<출력화면 예시>
#2차 방정식 결과 =22.6

#지방(fat), 탄수화물(carbohydrate), 단백질(protein)칼로리의 합계를 계산하는 프로그램을 작성하시오.
#<조건1>지방. 탄수화물, 단백질의 그램을 키보드로 입력받는다
#<조건2> 총 칼로리=지방 *9 + 단백질 *4+탄수화물*4

#<출력화면 예시>
# 지방의 그램을 입력하세요 : 25
# 탄수화물의 그램을 입력하세요 : 520
# 단백질의 그램을 입력하세요 : 45
# 총 칼로리 : 2,485 cal

print("지방의 그램을 입력하세요")
fat=input()
print("탄수화물을 입력하세요")
carbo=input()
print("단백질을 입력하세요")
prot=input()

print("총 칼로리는 "+(fat*9+carbo*4+prot*4)+"cal")

# 3개의 단어를 키보드로 입력 받아서 각 단어의 첫글자를 추출하여 단어의 약자를 출력하시오
#<처리조건>
#<조건1> 각 단어 변수(word1, word2, word3)저장
#<조건2> 입력과 출력 구분선 : 문자열 연산
#<조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장

#<출력화면 예시>
#첫번째 단어 : Korea
#두번재 단어 : Baseball
#세번재 단어 : Orag
#====================
#약자 : KBO


weight = int(input("짐의 무게는 얼마입니까?"))
if weight < 10 :
    print('수수료는 없습니다.')
else:
    print('수수료는 10,000원 입니다')

weight = int(input("짐의 무게는 얼마입니까?"))
if weight < 10 :
    print('수수료는 없습니다.')
else:
    exp = (weight //10) * 10000
    print('수수료는' + format(exp,'3,d')+'입니다')
    print('수수료는 {}입니다'.format(exp,'3,d'))


