class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        nums.sort()
        i=0
        while(i<n):
            j=i+1
            while(j<n):
                l=j+1
                r=n-1
                while(l<r):
                    f_sum=nums[i]+nums[j]+nums[l]+nums[r]
                    if(f_sum<target):
                        l+=1
                    elif(f_sum>target):
                        r-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while(l<r and nums[l]==nums[l-1]):
                            l+=1
                j+=1
                while(j<n and nums[j]==nums[j-1]):
                    j+=1
            i+=1        
            while(i<n and nums[i]==nums[i-1]):
                i+=1        
        return res                        
        