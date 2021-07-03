N = 100
for n in range(5,0,-1):
    for j in range(5-n):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print()


N = 5
for n in range(1,10):
    print(N,"*",n,"=",N*(n))