#점수 계산 하는것을 함수화 작업 해주세요.
#1) list에 자료 입력을 함수로 하는것으로 변경.
#2) 합계 구하는 것을 함수로 하는 것으로 변경
#3) 평균 구하는 것을 함수로 하는것으로 변경.

students=[
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
    {"name": "김미화", "korean": 82, "math": 86, "english": 98, "science": 88},
    {"name": "김연화", "korean": 88, "math": 74, "english": 78, "science": 92},
    {"name": "박아현", "korean": 97, "math": 92, "english": 88, "science": 95},
    {"name": "서준서", "korean": 45, "math": 52, "english": 72, "science": 78},
]
print(students)

def create_student(name,korean,math,english,science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }
def student_get_sum(student):
    return student["korean"] + student["math"] +\
            student["english"] + student["science"]
def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{} \t {} \t {} \t {} \t {} \t {} \t {}".format(
        student["name"],
        student["korean"],
        student["math"],
        student["english"],
        student["science"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("윤인성",87,98,88,95),
    create_student("연하진",92,98,96,98),
    create_student("구지연",76,96,94,90),
    create_student("나선주",98,92,96,92),
    create_student("윤아린",95,98,98,98),
    create_student("윤명월",64,88,92,92),
    create_student("김미화",82,86,98,88),
    create_student("김연화",88,74,78,92),
    create_student("박아현",97,92,88,95),
    create_student("서준서",45,52,72,78)
]
print("이름  ","국어  ","수학  ","영어  ","과학  ", "총점  ", "평균", sep=" \t ")
for student in students:
    #출력합니다
    print(student_to_string(student))
