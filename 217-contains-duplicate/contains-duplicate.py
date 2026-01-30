class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in nums:
        #    if(nums.count(i)>=2):
        #     return True
        # else:
        #     return False     
        nums.sort()
        count=1
        for i in range(len(nums)-1): 
            if(nums[i]==nums[i+1]):
                count+=1
            if(count>=2):
                return True
                break
        return False          
        