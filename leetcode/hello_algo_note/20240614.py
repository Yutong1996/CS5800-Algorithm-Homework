'''
Stack and queue，先入后出的线性数据结构，size可变，顶部元素栈顶，底部元素栈底，，在栈顶添加删除--入栈出栈
push，pop，peek
'''
# 实现stack的类型是stack 入栈出栈本质上是链表头节点加入和删除
class LinkedListStack:
  def __init__(self):
    self._peak: ListNode | None = None
    self._size: int = 0

  def size(self) -> int:
    return self._size
  def is_empty(self) ->bool:
    return self._size == 0
  def push(self, val:int):
    node = ListNone(val)
    node.next = self._peek
    self.peek = node
    self._size += 1
  def pop(self) -> int:
    num = self.peek()
    self._peek = self._peek.next
    self._size -= 1
    return num
  def peek(self) -> int:
    if self.is_empty():
      raise IndexError(" 栈为空")
    return self._peek.val
  def to_list(self) -> list[int]:
    arr = []
    node = self._peek
    while node:
      arr.append(node.val)
      node = node.next
    arr.reverse()
    return arr

#实现stack的类型是数组，使用数组尾元素，删除和添加都是O(1), 需要使用动态数组
class ArrayStack:
  def __init__(self):
    self._stack: list[int] = []
  def size(self) -> int:
    return len(self.stack)
  def is_empty(self) -> bool:
    return self._size == 0
  def push(self, item: int):
    self._stack.append(item)
  def pop(self) -> int:
    if self.is_empty():
      raise IndexError("栈为空")
    return self._stack.pop()
  def peek(self) -> int:
    if self.is_empty():
      return IndexError("栈为空")
    self._stack[-1]
  def to_list(self) -> list[int]:
    return self._stack
  
"""
链表需要手动终止
"""