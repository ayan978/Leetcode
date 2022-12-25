class Solution {
    public int[] plusOne(int[] digits) {
        int length = digits.length;
        for(int i=length-1;i>=0;i--){
            if(digits[i]==9){
                digits[i] = 0;
            }
            digits[i]++;
            return digits;
        }

        int[] result = new int[length+1];
        result[0] = 1;
        return result;      
    }
}
