def generateParenthesis(n: int):
    ans = []
    def rec(s, left, right):
        if len(s) == 2*n:
            ans.append(''.join(s))
            return
        if left < n:
            s.append('(')
            rec(s, left + 1, right)
            s.pop()
        if right < left:
            s.append(')')
            rec(s, left, right + 1)
            s.pop()
    rec([], 0, 0)
    return ans

print(generateParenthesis(3))