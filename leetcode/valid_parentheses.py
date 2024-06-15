class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
        stack = ['?']
        for c in s:
          if c in dic: stack.append(c)
          elif dic[stack.pop()] != c: return False
        return len(stack) == 1
'''
if ths stack is initially empty, we can't use stack.pop(). So I added '?' in it.
左开右闭的括号 结构上就像是 后进先出的stack
'''