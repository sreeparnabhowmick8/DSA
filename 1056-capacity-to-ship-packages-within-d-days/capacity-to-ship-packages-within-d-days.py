class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def reqdays(weights,mid):
            load=0
            day=1
            for i in range(len(weights)):
                if(load+weights[i]<=mid):
                    load+=weights[i]
                else:
                    day+=1
                    load=weights[i]  
            return day          
        low,high=max(weights),sum(weights)
        while(low<=high):
            mid=int((low+high)/2)
            if(reqdays(weights,mid)<=days):
                high=mid-1
            else:
                low=mid+1
        return low            
        