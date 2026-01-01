class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # res=nums1+nums2
        
        # res.sort()
        # if(len(res)%2==0):
        #     c1=res[len(res)//2-1]
        #     c2=res[len(res)//2]
        #     return (float(c1)+float(c2))   
        # else:
        #     return (float(res[len(res)//2])) 
        merged = nums1 + nums2

        # Sort the merged array.
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0

        