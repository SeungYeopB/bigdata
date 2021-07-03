#
# result = []
# for i in range(1, 21):
#     result.append(i)
#
# def trans_location(a, b):
#     array = []
#     answer = []
#
#     for i in range(a, b+1):
#         array.append(result[i-1])
#     array.reverse()
#
#     for i in range(1, a):
#         answer.append(result[i-1])
#
#     for i in array:
#         answer.append(i)
#
#     for i in range(b+1, 21):
#         answer.append(result[i-1])
#
#     return answer
#
# for i in range(10):
#     question = input().split(" ")
#     result = trans_location(int(question[0]), int(question[1]))
#
# print(result)
#
# card = [i for i in range(21)]
#
# for _ in range(10):
#     a, b = map(int, input().split())
#
#     for i in range((b - a + 1) // 2):  # 바꿈
#         temp = card[b - i]
#         card[b - i] = card[a + i]
#         card[a + i] = temp
#
# for i in card[1:]:
#     print(i, end=' ')
#
# list = [i for i in range(1, 21)]
# print(list)
#
#
#
#
#
# for i in range(10):
#     a, b = map(int, input().split())
#     temp = list[a - 1:b]
#     temp.reverse()
#     print(temp, list[a-1: b])
#     list[a - 1:b] = temp
#     print(list)
#
# for i in range(len(list)):
#     print(list[i], end=' ')


for n in range(1,6):

    for p in range(5-n):
        print(" ", end="")
    print("*"*n)

