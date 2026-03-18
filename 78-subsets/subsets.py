class Solution:
    def calculate_subset(self,arr,ans,n,idx,ds):
        if(idx==n):
            ans.append(ds[:])
            return
        
        ds.append(arr[idx])
        self.calculate_subset(arr,ans,n,idx+1,ds)
            
        ds.pop()
        self.calculate_subset(arr,ans,n,idx+1,ds)    

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        ds=[]
        self.calculate_subset(nums,ans,n,0,ds)
        return ans
               
        