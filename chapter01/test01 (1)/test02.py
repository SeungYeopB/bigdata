#(1) 오름차순 정렬
dataset = [3,5,1,2,4]
n =len(dataset)
for i in range(0,n-1):
    print("i값:", i)
    for j in range(i+1,n):
        print("i값:",i,"j값:",j)
        if dataset[i]>dataset[j]:
            tmp=dataset[i]
            dataset[i]=dataset[j]
            dataset[j]=tmp
    print(dataset)



dataset = [5,10,18,22,35,55,75,103]
value = int(input("검색할 값 입력 : "))

low = 0
high = len(dataset)-1
loc = 0
state = False

while (low <= high):
    mid = (low+high)

    if dataset[mid] > value:
        high = mid-1
    elif dataset[mid] < value:
        low = mid+1
    else:
        loc = mid
        state = True
        break
    if state:
        print("찾은위치 : %d번째" % (loc+1))
    else:
        print("찾는 값은 없습니다.")


#<각 단계별 출력 결과 예시>
#단계 1: [10,1,5,2,10,1,5,2]
#단계 2: [10,1,5,2,10,1,5,2,20]
#단계 3: [1,2,1,2,]
lst1 = [10,1,5,2,10,1,5,2]
lst2 = [10,1,5,2,10,1,5,2,20]
lst3 = [1,2,1,2]

lst= [10,1,5,2]
lst
print(lst)
result = lst * 2
print(result)

result[0]
first = result[0]*2
print(first)

result.append(first)
print(result)

result2 = result[1::2]
print(result2)


cnt = int(input('vecter 수 : '))
lst= []
for i in range(cnt):
    #값입력
    #값을 lst에 추가
    val = int(input('값을 입력하세요:'))
    lst.append(val)
print('vector크기',len(lst))


cnt = int(input('vecter 수 : '))
lst= []
for i in range(cnt):
    #값입력
    #값을 lst에 추가
    val = int(input('값을 입력하세요:'))
    lst.append(val)
print('vector크기',len(lst))
lst
search_value = int(input('찾는 수: '))
if search_value in lst:
    print("yes")
else:
    print("no")
#b형
messages = ['spam','ham','spam','ham','spam']
spam_list = [ msg for msg in messages if msg == 'spam']
spam_list
#A형
messages = ['spam','ham','spam','ham','spam']
dummy = [ 1 if msg == 'spam' else 0 for msg in messages]
dummy


position = ['과장','부장','대리','사장','대리','과장']
unique_position = list(set(position))
print('중복제거한 직위:', unique_position)
dict_position = {}
for po in position:
    dict_position[po] = dict_position.get(po,0)+1
print("직위별 빈도수 : ",dict_position)


students=[
    {"name" : "윤인성", "korean":87,"math":98,"english":88,"science":95},
    {"name" : "연하진", "korean":92,"math":98,"english":96,"science":98},
    {"name" : "구지연", "korean":76,"math":96,"english":94,"science":90},
    {"name" : "나선주", "korean":98,"math":92,"english":96,"science":92},
    {"name" : "윤아린", "korean":95,"math":98,"english":98,"science":98},
    {"name" : "윤명월", "korean":64,"math":88,"english":92,"science":92},
    {"name" : "김미화", "korean":82,"math":86,"english":98,"science":88},
    {"name" : "김연화", "korean":88,"math":74,"english":78,"science":92},
    {"name" : "박아현", "korean":97,"math":92,"english":88,"science":95},
    {"name" : "서준서", "korean":45,"math":52,"english":72,"science":78},
    ]

print(students)
print("===========================")
print("      성적        현황      ")
print("===========================")
print("==========================================")
print(" 이름   국어   수학   영어   과학   합계   평균")
print("==========================================")
total = 0
avg = 0
for sungjuk in students:
    #print(sungjuk)
    print(sungjuk["name"], end=' ')
    print(sungjuk["korean"], end='   ')
    print(sungjuk["math"], end='    ')
    print(sungjuk["english"], end='    ')
    print(sungjuk["science"], end='   ')
    total = sungjuk["korean"] + sungjuk["math"] +\
            sungjuk["english"] + sungjuk["science"]
    print(total, end='   ')
    avg = total / 4
    print(avg)


expense=[
    {"date" : "3/1", "traffic":87,"coffee":98,"food":88},
    {"date" : "3/2", "traffic":92,"coffee":98,"food":96},
    {"date" : "3/3", "traffic":76,"coffee":96,"food":94},
    {"date" : "3/4", "traffic":98,"coffee":92,"food":96},
    {"date" : "3/5", "traffic":95,"coffee":98,"food":98},
    {"date" : "3/5", "traffic":64,"coffee":88,"food":92},
    {"date" : "3/6", "traffic":82,"coffee":86,"food":98},
    {"date" : "3/6", "traffic":88,"coffee":74,"food":78},
    {"date" : "3/7", "traffic":97,"coffee":92,"food":88},
    {"date" : "3/8", "traffic":45,"coffee":52,"food":72},
    ]
print("===========================")
print("        용돈 사용 현황       ")
print("===========================")
print("====================================")
print("날짜   교통비    음료대    식대    합계")
print("====================================")
tot_traffic = 0
tot_coffee  = 0
tot_food    = 0
for exp in expense:
    print(exp["date"], end=',   ')
    print(exp["traffic"], end=',     ')
    print(exp["coffee"], end=',     ')
    print(exp["food"], end=',     ')
    #  일 합계
    total = exp["traffic"]+exp["coffee"]+exp["food"]
    print(total)
    tot_traffic = tot_traffic + exp["traffic"]
    tot_coffee = tot_coffee + exp["coffee"]
    tot_food = tot_food + exp["food"]
print("========================================")
print("합계", tot_traffic," ",tot_coffee," ",tot_food)
print("=========================================")


print("합계:","{:3},{:4}".format(100,1000))
print("합계:","{:4},{:5}".format(100,1000))
print("합계:","{:5},{:6}".format(100,1000))
print("합계:","{:6},{:7}".format(100,1000))


help(len)
dataset = list(range(1,6))
print(dataset)

print("len=", len(dataset))
print("sum=", sum(dataset))
print("max=", max(dataset))
print("min=", min(dataset))




import statistics
from statistics import variance, stdev
print("평균=", statistics.mean(dataset))
print("중위수=", statistics.median(dataset))
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))



all([1, True, 10, -15.2])
all([1, True, 0, -15.2])
all([1, False, 10, -15.2])

bin(10)








