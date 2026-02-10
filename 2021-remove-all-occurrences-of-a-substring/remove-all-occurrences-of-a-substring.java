class Solution {
    public String removeOccurrences(String s, String part) {
        // Keep removing 'part' until it's no longer found
        while (s.contains(part)) {
            s = removeSubstring(s, part);
        }
        return s;
    }
    // Helper method to remove one occurrence of 'part'
    static String removeSubstring(String s, String part) {
        int index = s.indexOf(part);
        if (index == -1) return s;
        // Rebuild the string without the matched 'part'
        return s.substring(0, index) + s.substring(index + part.length());
    }
}