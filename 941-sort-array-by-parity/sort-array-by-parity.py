class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return nums
        odd=[]
        even=[]    
        for i in nums:
            if(i%2==0):
                even.append(i)  
            else:
                odd.append(i)
        res=even+odd
        return res             
        