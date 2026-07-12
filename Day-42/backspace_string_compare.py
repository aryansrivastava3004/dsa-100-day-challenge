class Solution:
    def backspaceCompare(self, s, t):

        def build(string):

            stack = []

            for char in string:

                if char != "#":
                    stack.append(char)

                elif stack:
                    stack.pop()

            return stack

        return build(s) == build(t)
