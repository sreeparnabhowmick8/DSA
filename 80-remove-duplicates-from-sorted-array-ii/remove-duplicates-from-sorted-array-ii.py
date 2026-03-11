class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=0
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        demo=sorted(dic.keys())
        count=0   
        for i in demo:
            if(dic[i]>=2):
                nums[idx]=i
                idx+=1
                nums[idx]=i
                idx+=1
                count+=2
            else:
                nums[idx]=i
                idx+=1
                count+=1
        del nums[idx:]        

        return len(nums)              



        