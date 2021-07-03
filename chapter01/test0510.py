import pandas as pd
import os

print(os.getcwd())

score = pd.read_csv("./data/score.csv")
print(score.info())
print(score.head())

kor = score.kor
eng = score["eng"]
mat = score["mat"]
dept = score["dept"]

print("max kor=", max(kor))
print("max eng=", max(eng))
print("max mat=", max(mat))

print("min kor=", min(kor))
print("min eng=", min(eng))
print("min mat=", min(mat))

from statistics import mean
print("국어 점수 평균 : ", round(mean(kor), 3))
print("영어 점수 평균 : ", round(mean(eng), 3))
print("수학 점수 평균 : ", round(mean(mat), 3))

dept_count = {}

for key in dept:
    dept_count[key] = dept_count.get(key, 0) + 1
print(dept_count)

sam = pd.ExcelFile("./data/sam_kospi.xlsx")

kospi = sam.parse("sam_kospi")
print(kospi.info())

high = kospi["High"]
low = kospi["Low"]

from statistics import mean
print("high mean :", mean(high))
print("low mean :", mean(low))

print("High mean :", high.mean())
print("Low mean :", low.mean())

import json

user = {"id": 1234, "name": "홍길동"}

print(type(user))
print(user["name"])

jsonString = json.dumps(user, ensure_ascii=False)

print(jsonString)
print(type(jsonString))

pyObj = json.loads(jsonString)
print(type(pyObj))

print(pyObj["name"])
for key in pyObj:
    print(key, ":", pyObj[key])


