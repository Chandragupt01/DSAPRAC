class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            n=x
        else:
            n=-x
        revNum=0
        while n>0:
            lastDigit=n%10
            revNum=(revNum*10)+lastDigit
            n=n//10
        if x>0:
            if revNum<(-2**31) or revNum>(2**31)-1:
                return 0
            else:
                return revNum
        else:
            if revNum<(-2**31) or revNum>(2**31)-1:
                return 0
            return -revNum
        
''' Better Solution
class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        is_negative = False
        if x < 0:
            is_negative = True
            # x=x * -1
            x = abs(x)
        while x > 0:
            last_digit = x % 10
            reverse_number = (reverse_number * 10) + last_digit
            x = x // 10
        if is_negative:
            reverse_number = reverse_number * -1
        if reverse_number < (-(2**31)) or reverse_number > (2**31 - 1):
            return 0
        return reverse_number
'''