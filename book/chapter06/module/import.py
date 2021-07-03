class Rectangle :
    # (1) 멤버 변수
    width = 0
    height = 0
    # (2) 생성자
    def __init__(self, width, height):
        # 멤버 변수 초기화
        self.width = width
        self.height = height
    def area_calc(self):
        area = self.width * self.height
        return area
    def circum_calc(self):
        dule = (self.width + self.height) * 2
        return dule

print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input("사각형의 가로 입력 : "))
h = int(input("사각형의 세로 입력 : "))
#초기화
print("----------------------")
square = Rectangle(w,h)
area = square.area_calc()
print("사각형 넓이 : ", area)
square = Rectangle(w,h)
area = square.circum_calc()
print("사각형 둘레 : ", area)
print("----------------------")

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

# 산포도 클래스
class Scattering
    #생성자