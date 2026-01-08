class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # a,b=-1,-1
        # res=[]
        # for i in range(0,max(nums)+1):
        #     if i in nums:
        #         if(a!=-1):
        #             b=i
        #         a=i
        #     else:
        #         if(b==-1):
        #             res.append(str(a))
        #             a=-1
        #             b=-1
        #         else:
        #             res.append(f"{a}->{b}")
        #             a=-1
        #             b=-1
        # return res                
        res = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]

            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")

            i += 1

        return res

        
        