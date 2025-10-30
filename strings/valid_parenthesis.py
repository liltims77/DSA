
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    # stack[-1] -> last value added in the stack
                    # closeToOpen[c] -> Get the value from the dictionary closeToOpen using the key c
                    stack.pop()
                else: return False
            else:
                stack.append(c)
        return True if not stack else False
    





