class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []

    # Step 1: add elements following arr2 order
        for x in arr2:
            res.extend([x] * freq[x])
            del freq[x]#Remove elements already placed in result, so they are not added again later.

    # Step 2: add remaining elements in ascending order
        for x in sorted(freq):
            res.extend([x] * freq[x])

        return res       
        