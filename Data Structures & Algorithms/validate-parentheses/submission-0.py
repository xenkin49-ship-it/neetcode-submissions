class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"}":"{", ")":"(", "]":"["}
        for char in s:
            if char in mappings:
                if stack:
                    last_item = stack.pop()
                else: 
                    last_item = "#"
                if mappings[char] != last_item:
                    return False
            else:
                stack.append(char)
        return not stack