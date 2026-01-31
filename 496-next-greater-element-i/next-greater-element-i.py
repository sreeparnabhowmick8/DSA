class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        for i in nums2:
            while stack and stack[-1]<i:
                dic[stack.pop()]=i
            stack.append(i)
        while stack:
            dic[stack.pop()]=-1
        return [dic[i] for i in nums1]            



        