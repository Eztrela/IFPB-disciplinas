N =  int(input())
flag = True
for i in range(1,N+1):
    if (i == 1):
        print(1)
    elif (i == 2):
        print(2)
    elif (i == 3):
        print(3)
    else:
        for j in range(2,(i//2)+1):
            if ((i % j) == 0):
                flag = False
                break
        
        if (flag):
            print(i)
        flag =  True
