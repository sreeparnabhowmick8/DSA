class Solution {
    public int singleNumber(int[] arr) {
        HashMap<Integer,Integer> dic=new HashMap<>();
        for(int i: arr){
            dic.put(i,dic.getOrDefault(i,0)+1);
        }
        for(int i:arr){
            if(dic.get(i)==1){
                return i;
            }
        }
        return 0;
    }
}