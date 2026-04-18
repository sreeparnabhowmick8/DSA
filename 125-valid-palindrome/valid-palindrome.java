class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        char[] c=s.toCharArray();
        int start=0;
        int end=s.length()-1;
        while(start<end){
            if(c[start]!=c[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}