class Solution {
    public String reverseWords(String s) {
        // int i=0;
        // int n=s.length()-1;
        // String[] arr = s.split(" ");
        // while(i<n){
        //   String temp=arr[i];
        //   arr[i]=arr[n];
        //   arr[n]=temp;
        //   i++;
        //   n--;
        // }
        // return Arrays.toString(arr);
        String[] words = s.split("\\s+");
        StringBuilder res = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            res.append(words[i]);
            if (i != 0) {
                res.append(" ");
            }
        }

        return res.toString().trim();
    }
}