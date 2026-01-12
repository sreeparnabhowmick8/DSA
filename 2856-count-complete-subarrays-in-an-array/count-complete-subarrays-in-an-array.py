class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k=len(set(nums))
        c=0
        for i in range(len(nums)):
            subarr=set()
            for j in range(i,len(nums)):
                subarr.add(nums[j])
                if(k==len(subarr)):
                    c+=1
        return c            

        