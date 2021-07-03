class MyClass1:

    var = "안녕하세요"
    def __init__(self, var):
        self.var = var

    def sayHello(self):
        print(self.var)

obj = MyClass1("반갑습니다")
print(obj.var) #ERROR
obj.sayHello()

# 생성자 추가 - 값을 새로운 값으로 class 를 instance 하게
# 바꿔주세요