class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0)
        {
            return false;
        }
        int num=0,rem=0;
        long long rev=0;
        num=x;
        while(num!=0)
        {
            rem=num%10;
            rev=rev*10+rem;
            num=num/10;
        }
        return(rev==x);
    }
};