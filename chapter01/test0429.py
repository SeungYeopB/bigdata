class Account:
    #(1) 은닉 멤버변수
    __balance = 0 #잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    #(2) 생성자 : 멤버변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal # 잔액초기화
        self.__accName = name #예금주
        self.__accNo = no # 계좌번호

    #(3) 계좌정보 확인 : Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    #(4) 입금하기 : Setter
    def deposit(self, money):
        if money < 0 :
            print("금액확인")
            return #종료(exit)
        self.__balance +=money
    #(5) 출금하기 : Setter
    def withdraw(self, money):
        if self.__balance < money:
            print("잔액 부족")
            return # 종료(exit)
        self.__balance -=money
#(6) object 생성
acc = Account(1000, "홍길동", "125-152-4125-41") #생성자
#(7) Getter
#acc.__balance #오류(Error)
bal = acc.getBalance()
print("계좌정보 : ", bal)
#(8) Setter 호출
acc.deposit(20000) #20,000 입금
bal = acc.getBalance()
print("계좌 정보 : ", bal) #입금확인

#(1)부모 클래스
class Super:
    #생성자 : 동적 멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #메서드
    def display(self):
        print('name : %s, age : %d'%(self.name, self.age))
sup = Super('부모', 55)
sup.display() #부모 멤버 호출

#(2) 자식 클래스
class Sub(Super) : # 클래스 상속
    gender = None # 자식 멤버
     #(3)생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #(4)메서드 확장
    def display(self):
        print('name : %s, age : %d, gender : %s'
              %(self.name, self.age, self.gender))
sub = Sub("자식", 25, "여자")
sub.display() # 자식 멤버 호출

#(1) 부모 클래스
class Parent :
    # 생성자 : 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 멤버 함수
    def display(self):
        print("name : {}, job : {}".format(self.name, self.job))
#부모 클래스 객체 생성
p = Parent("홍길동", "회사원")
p.display()
#(2) 자식 클래스
class Children(Parent) : #Parent 클래스 상속
    gender = None #자식 클래스 멤버변수 추가

    #(3)자식 클래스 생성자
    def __init__(self, name, job, gender):
        # 부모 클래스 생성자 호출
        super().__init__(name, job) # name, job 초기화
        self.gender = gender # 자식 멤버변수 초기화
    # 멤버 함수(method)
    def display(self): # 함수 재정의
        print("name : {}, job : {}, gender : {}".format(self.name, self.job, self.gender))
# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()

#(1) 부모 클래스
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
# (2) 자식 클래스 : 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)  #부모 생성자 호출
    def pay_calc(self, base, bonus):
        self.pay = base + bonus  #급여 = 기본급 + 상여금
        print('총 수령액 : ', format(self.pay, '3,d'), '원')
#(3) 자식 클래스 : 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)  #부모 생성자 호출
    def pay_calc(self, tpay, time):
        self.pay = tpay * time  #급여=작업시간*시급
        print('총 수령액 : ', format(self.pay, '3,d'), '원')
#(4) 객체 생성
p = Permanent("이순신")
p.pay_calc(3000000, 200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)

#(1) 리스트 열거형 객체 이용
lst = [1, 3, 5]
for i, c in enumerate(lst) :
    print("색인 : ", i, end=", ")
    print("내용 : ", c)
#(2) 튜플 열거형 객체 이용
dit = {"name" : "홍길동", "job": "회사원", "addr":"서울시"}
for i, k in enumerate(dit) :
    print("순서 : ",  i, end=", ")
    print("키 : ", k, end=", ")
    print("값 : ", dit[k])