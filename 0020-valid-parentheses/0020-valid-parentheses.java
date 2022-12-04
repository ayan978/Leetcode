class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> s1 = new Stack<>(); 
        
        for(int i=0; i<s.length();i++){
            if(s.charAt(i)=='(' || s.charAt(i)=='{' || s.charAt(i)=='['){
                s1.push(s.charAt(i));
            }
            
            else if(!s1.isEmpty() && ((s.charAt(i)==')' && s1.peek()=='(') || (s.charAt(i)=='}' && s1.peek()=='{') || (s.charAt(i)==']' && s1.peek()=='['))){
                s1.pop();
            }
            
            else{
                s1.push(s.charAt(i));
            }
        }
        
        if(s1.isEmpty()){
            return true;
        }
        return false;
    }
}