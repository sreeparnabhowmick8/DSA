class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        l2=[]
        for i in nums:
            if(i==0):
                l1.append(i)
            else:
                l2.append(i)    
        nums[:]=l2+l1
        return nums