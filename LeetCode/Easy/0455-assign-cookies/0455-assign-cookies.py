class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ptr = 0
        cnt = 0
        for i in g:
            while ptr < len(s):
                if s[ptr] >= i:
                    #print(ptr)
                    ptr += 1
                    cnt += 1
                    break
                ptr += 1

        return cnt