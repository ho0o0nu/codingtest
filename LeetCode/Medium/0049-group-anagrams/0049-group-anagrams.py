class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram in anagrams:
                anagrams[anagram] += [s]
            else:
                anagrams[anagram] = [s]
        
        return [*anagrams.values()]