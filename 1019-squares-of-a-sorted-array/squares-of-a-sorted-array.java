class Solution {
    public int[] sortedSquares(int[] nums) {
        ArrayList<Integer> ans=new ArrayList<>();
        for(int i: nums){
            ans.add(i*i);
        }
        Collections.sort(ans);
        int[] res = new int[ans.size()];
    for(int i = 0; i < ans.size(); i++){
        res[i] = ans.get(i);
    }
    return res;
    }
}