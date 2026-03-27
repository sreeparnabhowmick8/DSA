class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def calculate(nums,k):
            l,r,sum1=0,0,0
            count=0
            n=len(nums)
            while(r<n):
                sum1+=(nums[r]%2)
                while(sum1>k):
                    sum1-=(nums[l]%2)
                    l+=1
                if(sum1<=k):
                    count+=(r-l+1)
                r+=1
            return count
        return calculate(nums,k)-calculate(nums,k-1)                

        