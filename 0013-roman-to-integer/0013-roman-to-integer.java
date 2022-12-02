class Solution {
    public int romanToInt(String s) {
        
        char[] symbols = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] value = {1, 5, 10, 50, 100, 500, 1000};

        Map<Character, Integer> m = new HashMap<>();
        int j = 0, result=0;
        for (int i=0; i<symbols.length;i++) {
            m.put(symbols[i],value[j]);
            j++;
        }

        for(int i=0;i<s.length()-1;i++){
            if(m.get(s.charAt(i))<m.get(s.charAt(i+1))){
                result -= m.get(s.charAt(i));
            }
            else{
                result += m.get(s.charAt(i));
            }
        }
        result += m.get(s.charAt(s.length()-1));
        return result;
    }
        
    }
