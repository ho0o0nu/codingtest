class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        
        result = 0
        for jewel in jewels:
            if jewel in counter:
                result += counter.get(jewel)
        
        return result