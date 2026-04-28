class Solution {
    public int maxScore(int[] arr, int k) {
       int lsum=0,rsum=0, maxlen=0;
        for(int i=0;i<k;i++){
            lsum+=arr[i];
            maxlen=Math.max(maxlen,lsum);
        }
        int rightidx=arr.length-1;
        for(int i=k-1;i>=0;i--){
            lsum-=arr[i];
            rsum+=arr[rightidx];
            rightidx--;
            maxlen=Math.max(maxlen,(rsum+lsum));
        }
        return maxlen; 
    }
}