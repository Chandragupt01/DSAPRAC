
class Solution:
    def lcmAndGcd(self, a , b):
        # code here 
        greater,smaller=0,0
        if a>b:
            greater=a
            smaller=b
        else:
            greater=b
            smaller=a
        lcm=0
        for i in range(greater,a*b+1,greater):
            if i % smaller==0:
                lcm=i
                break
        gcd=1
        for i in range(1,smaller+1):
            if greater%i==0 and smaller%i==0:
                gcd=i
        return[lcm,gcd]
            

