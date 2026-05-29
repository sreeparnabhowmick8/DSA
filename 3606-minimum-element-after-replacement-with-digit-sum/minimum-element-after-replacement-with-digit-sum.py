class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum1=0
        arr=[]
        for i in nums:
            mini=i
            while(mini>0):
                rem=mini%10
                sum1+=rem
                mini=int(mini/10)
            arr.append(sum1)
            sum1=0
        return min(arr)    
        