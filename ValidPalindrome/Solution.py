class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s if x.isalnum())
        s = ''.join(s.split())
        s = s.lower()
        revstr=''.join(reversed(s)) 
        print(s)
        print(revstr)
        if(s==revstr):
            return True
        return False