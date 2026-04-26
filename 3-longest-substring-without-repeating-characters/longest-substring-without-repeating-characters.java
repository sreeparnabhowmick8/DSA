class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> st=new HashSet<>();
        int left=0,maxlen=0;
        for(int i=0;i<s.length();i++){
            while(st.contains(s.charAt(i))){
                st.remove(s.charAt(left));
                left++;
            }
            st.add(s.charAt(i));
            maxlen=Math.max(maxlen,i-left+1);
        }
        return maxlen;
    }
}