/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<Integer> ll=new ArrayList<>();
    public void checkinorder(TreeNode root){
        if(root==null){
            return;
        }
        checkinorder(root.left);
        ll.add(root.val);
        checkinorder(root.right);
    }
    public boolean isValidBST(TreeNode root) {
        checkinorder(root);
        int i=0;
        while(i<ll.size()-1){
            if(ll.get(i)>=ll.get(i+1)){
                return false;
            }
            i++;
        }
        return true;
    }
}