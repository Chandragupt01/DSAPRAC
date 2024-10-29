class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        num=x
        while num>0:
            lastDigit=num%10
            rev=(rev*10)+lastDigit
            num=num//10
        if rev==x:
            return True
        return False
        