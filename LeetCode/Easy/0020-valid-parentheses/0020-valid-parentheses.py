class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack:
                    comp = stack.pop()
                    if ch == ")" and comp != "(":
                        return False
                    elif ch == "}" and comp != "{":
                        return False
                    elif ch == "]" and comp != "[":
                        return False
                else:
                    return False
                

        if stack:
            return False

        return True