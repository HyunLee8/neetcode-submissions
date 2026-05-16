class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].lower().isalnum():
                l += 1
            if not s[r].lower().isalnum():
                r -= 1
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    print(s[l])
                    print(s[r])
                    return False
                l += 1
                r -= 1
        return True