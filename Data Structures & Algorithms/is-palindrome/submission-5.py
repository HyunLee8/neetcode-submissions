class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i.lower()
        
        revS = ""

        for i in range(len(newS)):
            revS += newS[len(newS) - 1 - i]

        print(revS)
        print(newS)

        return revS == newS
