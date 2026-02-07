class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1,count=0,0
        for i in nums:
            if(i==1):
                count+=1
                max1=max(max1,count)
            else:
                count=0
        return max1            
        