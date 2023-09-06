class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 ){

            return false;
        }
        String x_str = Integer.toString(x);
        char ch;
        String nstr = "";
        //System.out.println(x_str);
        for (int i=0; i<x_str.length(); i++)
        {
            ch= x_str.charAt(i); //extracts each character
            nstr= ch+nstr; //adds each character in front of the existing string
        }
        //System.out.println("Reversed word: "+ nstr);
        return nstr.equals(x_str);
        
    }
}