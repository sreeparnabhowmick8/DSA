class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            convert=str(i)
            if len(convert)%2==0:
                count+=1
        return count        
        