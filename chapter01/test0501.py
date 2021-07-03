
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h


    def area_calc(self):
        return self.w * self.h
    def circum_calc(self):
        return (self.w + self.h) * 2

print("사각형의 넓이와 둘레를 계산합니다")
w = int(input('사각형의 가로 입력 : '))
h = int(input("삼각형의 세로 입력 : "))

sagak = Rectangle(w, h)
print("사각형의 넓이 : " + str(sagak.area_calc()))
print("사각형의 둘레 : " + str(sagak.circum_calc()))

def area_calc(w, h):
    return w * h

def circum_calc(w, h):
    return (w + h) * 2

print("사각형의 넓이 : " + str(area_calc(w, h)))
print("사각형의 둘레 : " + str(circum_calc(w, h)))

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]
# 산포도 클래스
class Scattering :

    def __init__(self, data):
        self.data = data

    def avg(self):
        avg = mean(self.data)
        return avg

    def var_sd(data):
        avg = Avg(data)
        diff = [(d-avg) ** 2 for d in data]
        var = sum(diff) / (len(data) - 1)
        sd = sqrt(var)

        return var, sd

    # 출력부분
    data = [2, 4, 5, 6, 1, 8]

    print(var_sd(data))


class Person:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print("이름 : {}, 성별 : {}, 나이 : {}".format(self.name,self.gender,self.age))

name = input("이름 : ")
gender = input("성별(male/female) : ")
age = int(input("나이 : "))

person = Person(name, gender, age)


class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name


class Permanent(Employee):
    def __init__(self, name, pay1, pay2):
        super().__init__(name)
        self.pay1 = pay1
        self.pay2 = pay2

    def getName(self):
        return self.name

    def get_sum(self):
        return self.pay1+self.pay2



class Temporary(Employee):
    def __init__(self, name, time, pay3):
        super().__init__(name)
        self.time = time
        self.pay3 = pay3

    def getName(self):
        return self.name

    def get_mul(self):
        return self.time * self.pay3


empType = input("고용형태 선택(정규직<P>, 임시적<T>) : ")
if empType == "P" or empType == "p":
    name = input("이름 : ")
    pay1 = int(input("기본급 : "))
    pay2 = int(input("상여금 : "))
    print("고용형태 : 정규직")

    p = Permanent(name, pay1, pay2)

    print("이름 : {}, 급여 : {}".format(p.name, p.get_sum()))

elif empType == "T" or empType == "t":
    name = input("이름 : ")
    time = int(input("작업시간 : "))
    pay3 = int(input("시급 : "))
    print("고용형태 : 임시직")

    t = Temporary(name, time, pay3)

    print("이름 : {},\n급여 : {}".format(t.name, t.get_mul()))

else :
    print("="*30)
    print("입력 오류")

class Exam:

    def __init__(self, info, math, sciense, english):
        self.info = info
        self.math = math
        self.sciense = sciense
        self.english = english

    def get_sum(self):
        return self.info + self.math + self.sciense + self.english

manse = Exam(100, 80, 70, 60)
minkuk = Exam(80,70,80,90)

a = manse.get_sum()
b = minkuk.get_sum()

if a > b:
    print(a)
else:
    print(b)


class Expense:
    def __init__(self, date, coffee, traffic, bob):
        self.date = date
        self.coffee = coffee
        self.traffic = traffic
        self.bob = bob

    def get_sum(self):
        return self.coffee + self.traffic + self.bob

    def get_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.date,
            self.coffee,
            self.traffic,
            self.bob,
            self.get_sum())


    def tot_expense(self):
        return "{}\t{}\t{}\t{}".format(
            self.tot_coffee

        )

expenses = [
    Expense("3/1", 8700, 9800, 8800),
    Expense("3/2", 5700, 9700, 6700),
    Expense("3/3", 8700, 9800, 9800),
    Expense("3/4", 5700, 9500, 6700),
    Expense("3/5", 8700, 6800, 8800),
    Expense("3/6", 5700, 9700, 6700),
    Expense("3/7", 8300, 9800, 9800),
    Expense("3/8", 5700, 9500, 9700)
]

print("일자","음료대","교통비","기타비용","합계")
for e in expenses:
    print(e.get_string())

for e, i in enumerate(expenses):
    print(e.get_string())
    if i == len(expenses) - 1:
        print("{}\t{}".format(e, i))

r = [1, 2, 3, 4, 5]




for e, i in enumerate(r):
    print("{}\t{}".format(e,i))

import keyword
print(keyword.kwlist)





