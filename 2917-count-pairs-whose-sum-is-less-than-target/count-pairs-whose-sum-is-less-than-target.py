class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # l=0
        # r=len(nums)-1
        # count=0
        # while(l<r):
        #     sum1=nums[l]+nums[r]
        #     if(sum1<target):
        #         count+=1
        #         r-=1
        #     elif(sum1==target):
        #         r-=1
        #     else:
        #         l+=1
        # return count   
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum1=nums[i]+nums[j]
                if(sum1<target):
                    count+=1
        return count               

        