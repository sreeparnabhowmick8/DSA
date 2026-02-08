class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return nums
        odd=[i for i in nums if i%2!=0 ]
        even=[i for i in nums if i%2==0]    
        res=even+odd
        return res             
        