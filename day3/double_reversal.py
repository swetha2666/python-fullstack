#this code only satisfies given test cases
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # reversenum=0
        # originalnum=abs(num)
        # while originalnum>0:
        #     digit=originalnum%10
        #     eversenum=reversenum*10+digit
        #     roriginalnum //=10
        # return num==reversenum or num==  -reversenum
        return num==0 or num%10!=0