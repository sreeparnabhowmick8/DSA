class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]
        # return []

        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
            else:
                dic[nums[i]]=i
        return [0,0]                        
                   
        
              
                  

        