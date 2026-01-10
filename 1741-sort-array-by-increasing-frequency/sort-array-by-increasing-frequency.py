class Solution:
    def frequencySort(self, arr: List[int]) -> List[int]:
        dic={}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
         # Step 2: Sort array using custom key
        # -dic[i]  → higher frequency first
        # i        → smaller number first if freq same
        arr.sort(key=lambda i:(-dic[i],i))
        return arr[::-1]
        