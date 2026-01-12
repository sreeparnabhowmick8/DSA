from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num=int(len(nums)/2)
        count=Counter(nums)
        for i,val in count.items():
            if val==num:
                return i
        