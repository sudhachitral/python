class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.lower()
        r=''
        for i in range(len(s)):
            if s[i].isalnum():
                r+=s[i].lower()
        if r==r[::-1]:
            return True
        else:
            return False
        
