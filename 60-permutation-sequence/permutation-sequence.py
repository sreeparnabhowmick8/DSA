class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        nums = list(range(1, n + 1))
        fact = math.factorial(n - 1)
        k -= 1  # convert to 0-based index
        ans = ""

        while nums:
            index = k // fact
            ans += str(nums[index])
            nums.pop(index)

            if not nums:
                break

            k = k % fact
            fact = fact // len(nums)

        return ans            
        