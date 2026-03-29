class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        count = {}  # Dictionary to track frequency of numbers in the window
        l = 0
    
        for r in range(len(nums)):
        # 1. Add the current element to the window
            current_sum += nums[r]
            count[nums[r]] = count.get(nums[r], 0) + 1
        
        # 2. If the window size exceeds k, shrink it from the left
            if r - l + 1 > k:
                current_sum -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
            
        # 3. If window is exactly size k AND all elements are unique
            if r - l + 1 == k:
                if len(count) == k:
                    max_sum = max(max_sum, current_sum)
                
        return max_sum             

        