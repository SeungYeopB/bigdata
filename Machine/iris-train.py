from sklearn import svm, metrics
import random, re

# iris csv file 읽기
csv = []
with open("iris.csv", "r", encoding="utf-8") as fp:
    # 한줄씩 읽기
    for line in fp:
        line = line.strip()  # 줄바꿈 제거
        cols = line.split(",")  # 쉼표로 자르기
        print(cols)
        fn = lambda n : float(n) if re.match(r"^[0-9\.]+$",n) else n
        cols = list(map(fn, cols))
        csv.append(cols)
len(csv)
csv[0]
del csv[0]  # 맨 윗줄 헤더 제거
csv[0]
#  데이터 섞기
random.shuffle(csv)
#  데이터 분할  학습 2 : 테스트 1 비율
tot_len = len(csv)
train_len = int(tot_len *2 / 3)
print(tot_len)
print(train_len)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(tot_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

print(len(train_data))
print(len(train_label))
print(len(test_data))
print(len(test_label))
# 데이터 학습
clf = svm.SVC()  # SVC 인공지능 뭐시기
clf.fit(train_data, train_label)
pre = clf.predict(test_data)  # predict 에측
# 정답률 비교
score = metrics.accuracy_score(test_label, pre)
print("정답률:", score)