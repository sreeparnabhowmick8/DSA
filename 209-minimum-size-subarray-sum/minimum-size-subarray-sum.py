class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,currsum=0,0
        minlen=float("inf")
        n=len(nums)
        for right in range(n):
            currsum+=nums[right]
            while(currsum>=target):
                if(right-left+1<minlen):
                    minlen=right-left+1
                currsum-=nums[left]
                left+=1
        if(minlen==float("inf")):
            return 0
        else:
            return minlen                

           


        