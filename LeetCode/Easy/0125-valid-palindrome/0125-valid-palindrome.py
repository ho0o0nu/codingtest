class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = Deque()
        cleaned = s.lower()
        for ch in cleaned:
            if ch.isalnum():
                d.append(ch)
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True