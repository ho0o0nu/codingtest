class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        cleaned = re.sub('[^0-9a-z]', ' ', paragraph).split()
        counter = Counter(cleaned)

        while True:
            answer = counter.most_common(1)[0][0]
            if answer in banned:
                counter.pop(answer)
            else:
                return answer
