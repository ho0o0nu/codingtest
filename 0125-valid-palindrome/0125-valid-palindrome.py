class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        for i in range(len(clean)):
            if clean[i] == clean[-(i + 1)]:
                continue
            else:
                return False
                
        return True