/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int decimal_to_binary(String b) {
    
        int n = b.length();
        int decimal = 0;

        for(int i = 0, j = n-1; i < n; j--, i++){
            if(b.charAt(i) == '1'){
                decimal +=(int)Math.pow(2,j);
            }

        }
        return decimal;

    }
    public int getDecimalValue(ListNode head) {
        ListNode temp=head;
        ArrayList<Integer> ll=new ArrayList<>();
        String s="";
        while(temp!=null){
           s+=Integer.toString(temp.val);
           temp=temp.next;
        }
        return decimal_to_binary(s);
    }
}