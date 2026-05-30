class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse=True)

        rank = {}

        for i, val in enumerate(arr):
            rank[val] = i + 1

        ans = []

        for s in score:

            if rank[s] == 1:
                ans.append("Gold Medal")
            elif rank[s] == 2:
                ans.append("Silver Medal")
            elif rank[s] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank[s]))

        return ans          
                    





        