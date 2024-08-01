def printNos(i,n):
    if i < 1 :
        return
    printNos(i-1,n)
    print(i)