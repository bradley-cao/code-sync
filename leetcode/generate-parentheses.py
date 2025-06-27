class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        stack.append(("(", 1, 0))
        
        combos = []

        while len(stack) > 0:
            (combo, left, right) = stack.pop()
            if left < n:
                stack.append((combo + "(", left + 1, right))
            if right < left:
                stack.append((combo + ")", left, right + 1))
            if left == n and right == n:
                combos.append(combo)
        
        return combos