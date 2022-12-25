class Solution {
    public int lengthOfLastWord(String s) {
        String s1 = s.trim();
        int i = s1.length()-1, length=0;

        while(i>=0 && s1.charAt(i)!=' '){
            length++;
            i--;
        }

        return length;
    }
}
