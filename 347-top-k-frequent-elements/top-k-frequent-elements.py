class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        freq = {}

    # Count frequency using dictionary
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

    # Sort based on frequency (desc) and value (desc)
        items = list(freq.items())
        items.sort(key=lambda x: (-x[1], -x[0]))

    # Get top k elements
        result = []
        for i in range(k):
            result.append(items[i][0])

        return result
        