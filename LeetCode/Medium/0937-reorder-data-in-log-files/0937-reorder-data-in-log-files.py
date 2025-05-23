class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []

        for log in logs:
            letter_log = re.sub('[^a-z]', '', ''.join(log.split()[1:]))
            if letter_log:
                let.append(log)
            else:
                dig.append(log)

        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let + dig