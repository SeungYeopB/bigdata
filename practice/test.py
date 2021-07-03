
N=int(input())
result = 0
for n in range(N+1):
    result += n

print(result)

N = int(input())
for i in range(N):
    for j in range(1, N-i):
        print(" ", end="")
    for j in range(i*2+1):
        print("*", end="")
    print()

N = int(input())
for i in range(N):
    for j in range(1,N-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(1,4):
    print(i)

N = int(input())
for i in range(N):
    for j in range(1,2N-1):
        print("*",end="")
    for j in range(1,7):
        print(" ",end="")

N = int(input())
for i in range(0,N):
    for j in range(0,i):
        print(" ", end="")
    for j in range(2*(N-i)-1, 0, -1):
        print("*", end="")
    print(" ")

N = int(input())
for i in range(0,N):
    for j in range(i,N-1):
        print(" ",end="")
    for j in range(2*N,2*(N-i)-1,-1):
        print("*",end="")
    print(" ")
for i in range(1,N):
    for j in range(0,i):
        print(" ", end="")
    for j in range(2*(N-i)-1, 0, -1):
        print("*", end="")
    print(" ")

N = int(input())
for i in range(1,2*N):
    for j in range(1,2*N):
        if
        print("*",end="")

    for j in range():
        print(" ",end="")
    print(" ")

a = '1'
if(a == '1'):
    print("hi")

N = int(input())
for i in range(0, 2*N):
    if (N == 1):
        print("*")
        break
    for j in range(0, N):
        if((i + j) % 2 == 0):
            print("*", end ="")
        else :
            print(" ", end="")
    print("")

f = open("./text.txt", "r")

# 입력부
arr = f.readlines()

input_text = input()
condition = input_text.strip()
input_text = input()
data = input_text.strip()

N = condition.split(" ")[0]
X = int(condition.split(" ")[1])

# 조작부
for n in data.split(" "):
    if X > int(n):
        print(n, end=" ")


condition = input().strip()
data = input().strip()

N = condition.split(" ")[0]
X = int(condition.split(" ")[1])

for n in data.split(" "):
    if X > int(n):
        print(n, end=" ")

*
**
***
****
*****

N = int(input())

for i in range(1, N+1):
    for j in range(0, i):
        print("*", end="")
    print("")

    *
   **
  ***
 ****
*****

N= int(input())

for i in range(1, N+1):
    for j in range(i,N):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print("")

*****
****
***
**
*

N = int(input())

for i in range(1,N+1):
    for j in range(i,N+1):
        print("*",end="")
    for j in range(1,i):
        print(" ",end="")
    print("")

*****
 ****
  ***
   **
    *
N = int(input())

for i in range(1,N+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(i,N+1):
        print("*", end="")
    print("")