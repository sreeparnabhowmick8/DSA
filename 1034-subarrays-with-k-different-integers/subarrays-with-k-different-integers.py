class Solution:
    def less_than_equals_to_k(self,nums,k):
        l,r,count=0,0,0
        dic={}
        n=len(nums)
        while(r<n):
            dic[nums[r]]=dic.get(nums[r],0)+1
            while(len(dic)>k):
                dic[nums[l]]-=1
                if(dic[nums[l]]==0):
                    del dic[nums[l]]
                l+=1
            count+=(r-l+1)
            r+=1
        return count            

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.less_than_equals_to_k(nums,k)-self.less_than_equals_to_k(nums,k-1)