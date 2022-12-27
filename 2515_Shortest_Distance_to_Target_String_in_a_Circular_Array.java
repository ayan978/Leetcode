class Solution {
    public int closetTarget(String[] words, String target, int startIndex) {
        int i = startIndex, j = startIndex;
        int forward = 0, backward = 0;
        int n = words.length;
        
        do{
            if(words[i].equals(target)){
                break;
            }
            i = (i+1)%n;
            forward++;
        }while(i!=startIndex);

        do{
            if(words[j].equals(target)){
                break;
            }
            j = ((j-1)+n)%n;
            backward++;
        }while(j!=startIndex);
        
        if(words[i].equals(target) && words[j].equals(target)){
            if(forward<backward){ 
                return forward;
            }
            else{
                 return backward;
            }
        }
        
        return -1;
    }
}
