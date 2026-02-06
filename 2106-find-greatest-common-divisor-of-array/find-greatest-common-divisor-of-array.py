class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max1=max(nums)
        min1=min(nums)
        i=min1
        while(i>=1):
            if(max1%i==0 and min1%i==0):
                return i
            i-=1      

        