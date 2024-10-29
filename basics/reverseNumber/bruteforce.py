num = int(input("Enter a number: "))
n=num
revNum=0
while n>0:
    a=n%10
    revNum=(revNum*10)+a
    n=n//10
print(num)
print(revNum)