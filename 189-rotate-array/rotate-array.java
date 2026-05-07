class Solution {
    public void rotate(int[] arr, int d) {
       int[] res=new int[arr.length];
        int j=0;
        d = d % arr.length;
        for(int i=arr.length-d;i<arr.length;i++){
            res[j]=arr[i];
            j+=1;
        }
        for(int i=0;i<arr.length-d;i++){
            res[j]=arr[i];
            j+=1;
        }
        j=0;
        for(int i=0;i<arr.length;i++){
            arr[i]=res[j];
            j+=1;
        }
    }
}