class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()){
            return false;
        }
        
        else{
            int[] counter = new int[26];
            int length = s.length();
            for(int i=0;i<length;i++){
                counter[s.charAt(i)-'a']++;
                counter[t.charAt(i)-'a']--;
            }
            length = counter.length;
            for(int i=0;i<length;i++){
                if(counter[i]!=0){
                    return false;
                }
            }
            return true;
        }
    }

}
