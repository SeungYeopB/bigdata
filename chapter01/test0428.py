#(1)함수정의
def calc_func(a,b):
    #변수 선언 : 자료저장
    x = a # 10
    y = b # 20

    def plus():
        p = x + y
        return p
    def minus():
        m = x - y
        return m
    return plus, minus
# (2) 함수 호출
p, m = calc_func(10,20)
print('plus =', p())
print('minus=', m())
#(3) 클래스 정의
class calc_class :
    #클래스 변수 :  자료저장
    x = y = 0

    #생성자 : 객체 생성 + 멤버변수 초기화
    def __init__(self, a, b):
        self.x = a # 10
        self.y = b # 20
    #클래스 함수
    def plus(self):
        p = self.x + self.y # 변수 연산
        return p
    #클래스 함수
    def minus(self):
        m = self.x - self.y # 변수연산
        return m
#(4) 객체 생성
obj = calc_class(10,20)
#(5) 멤버 호출
print('plus=', obj.plus()) # plus = 30
print('minus =', obj.minus()) # minus = -10

obj2 = calc_class(100,50)
print('plus=', obj2.plus())
print('minus=', obj2.minus())

print(id(obj), id(obj2))
print(type(obj), type(obj2))

class Car:
    #(1) 멤머변수
    cc = 0 #엔진 cc
    door = 0 #문짝 개수
    carType = None # null
    #(2) 생성자
    def __init__(self, cc, door, carType):
        #멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType # 승용차, SUV
    #(3)메서드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s"
              %(self.cc,self.door,self.carType))
#(4) 객체 생성
car1 = Car(2000, 4, "승용차") # 객체 생성 + 초기화
car2 = Car(3000, 5, "SUV")
#(5) 멤버 호출 : Object.member()
car1.display() # cal1 멤버 호출
car2.display() # cal2 멤버 호출

#(1) 생성자 이용 멤버변수 초기화
class multiply:
    #멤버 변수
    x = y = 0
    #생성자 : 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #메서드
    def mul(self):
        return self.x * self.y
obj = multiply(10,20)
print('곱셉 =', obj.mul())
#(2)메서드 이용 멤버변수 초기화
class multiply2 :
    # 멤버 변수
    x = y = 0
    #생성자 없음 : 기본 생성자 제공
    def __init__(self):
        pass
    #메서드 : 멤버 변수 초기화
    def data(self, x, y):
        self.x = x
        self.y = y

    #메서드 : 곱셈
    def mul(self):
        return self.x * self.y
obj = multiply2() # 기본 생성자
obj.data(10,20) #동적 멤버변수 생성
print('곱셈 =', obj.mul())

class multiply3 :
    # 멤버 변수 없음
    # 생성자 없음

    # 동적 멤버변수 생성/초기화
    def data(self, x, y):
        self.x = x
        self.y = y

    #곱셉 연산
    def mul(self):
        result = self.x * self.y
        self.display(result) # 메서드 호출
    #결과 출력
    def display(self, result):
        print('곱셈 = %d' %(result))
obj = multiply3()
obj.data(10,20)
obj.mul()

class DatePro:
    #(1) 멤버 변수
    content = "날짜 처리 클래스"

    #(2) 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self, month, day):
        self.month = month
        self.day = day
    #(3) 객체 메서드(instance method)
    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))
    #(4) 클래스 메서드(class method)
    @classmethod # 함수 장식자
    def date_string(cls, dateStr): #19951025
        year = dateStr[0:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")
#(5)객체 멤버
date = DatePro(1995,10,25) # 생성자
print(date.content) #날짜 처리 클래스
print(date.year) #1995
date.display() # 1995 - 10 -25
#(6)클래스 멤버
print(DatePro.content) #날짜 처리 클래스
#print(DatePro.year) #AttributeError
DatePro.date_string('19951025') #1995년 10월 25일


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{} \t {} \t {} \t {} \t {} \t {} \t {}".format(
            self.name,
            self.korean,
            self.math,
            self.english,
            self.science,
            self.get_sum(),
            self.get_average())

students = [
    Student("박이성",85,98,88,95),
    Student("운이성",85,78,88,95),
    Student("윤정성",55,98,88,94),
    Student("김이성",85,98,68,95),
    Student("신이성",85,74,88,95),
    Student("조이성",85,78,78,75),
    Student("민지성",85,98,88,95),
    Student("최이성",65,98,48,85),
    Student("석우성",85,98,88,65),
    Student("민현성",65,88,88,95),
    Student("감이성",85,98,85,95)
]

print("이름    ", "국어    ", "수학   ", "영어    ", "과학    ", "총점    ", "평균")
for student in students:
    print(student.to_string())

#(1) 모듈 내장 클래스 import
import datetime  # 모듈 import
from datetime import date, time

#(2) date 클래스
help(date) # date 클래스 도움말

today = date(2019, 10, 23) # date 객체 생성
print(today) # date 객체 정보

# date 객체 멤버 변수 호출
print(today.year)
print(today.month)
print(today.day)

#date 객체 메서드 호출
w = today.weekday() # Monday==0...Sunday==6
print('요일 정보 : ', w) # 요일 정보

#(3)time 클래스
help(time) #time 클래스 도움말

currTime = time(21, 4, 30)  #time 객체 생성
print(currTime) # time 객체 정보

#time 객체 멤머 변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

#time 객체 메서드 호출
isoTime = currTime.isoformat() # HH:MM:SS
print(isoTime)