class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,ds,ans,freq):
            if(len(ds)==len(nums)):
                ans.append(ds[:])
                return
            for i in range(len(nums)):
                if(freq[i]==False):
                    freq[i]=True
                    ds.append(nums[i])
                    helper(nums,ds,ans,freq)
                    ds.pop(len(ds)-1)
                    freq[i]=False
        ds=[]
        ans=[]
        freq=[False]*len(nums)
        helper(nums,ds,ans,freq)
        return ans            

        