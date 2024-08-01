def printNos(i,n):
    if i > n :
        return
    print(i)
    printNos(i+1,n)