class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        count=0
        sum1=0
        for i in range(len(cost)-1,-1,-1):
            if(count==2):
                count=0
            else:
                count+=1
                sum1+=cost[i]
        return sum1            

        