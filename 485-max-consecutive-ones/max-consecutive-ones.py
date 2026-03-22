class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1,one_count=0,0
        for i in nums:
            if(i==1):
                one_count+=1
                max1=max(max1,one_count)
            else:
                one_count=0
        return max1                        
        