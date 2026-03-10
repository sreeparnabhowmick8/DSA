class Solution {
    private void findcombination(int idx,int[] arr,int target,List<List<Integer>> ans, List<Integer> ds){
        if(idx==arr.length){ //BASE CASE
            if(target==0){
                ans.add(new ArrayList<>(ds));
            }
            return;
        }
        if(arr[idx]<=target){ //PICK
            ds.add(arr[idx]);
            findcombination(idx,arr,target-arr[idx],ans,ds);//recurse
            ds.remove(ds.size()-1);//backtrack (remove it)
        }
        findcombination(idx+1,arr,target,ans,ds);//NOT PICK
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
       List<List<Integer>> ans=new ArrayList<>();
       findcombination(0,candidates,target,ans,new ArrayList<>()) ;
       return ans;
    }
}