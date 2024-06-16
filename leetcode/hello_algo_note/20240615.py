"""
Queue, push() add an element on the rear, pop()move out the first one, peek()visit the first one
在python中我们使用deque，双向队列，更好用
"""
from collections import deque

from leetcode.remove_linked_list_elements import ListNode
que: deque[int] = deque()

que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)

front: int = que[0]

pop: int = que.popleft()

size: int = len(que)

is_empty: bool = len(que) == 0

class LinkedListQueue:
  def __init__(self):
    self._front: ListNode | None = None # 头节点 front
    self._rear: ListNode | None = None # 尾节点
    self._size: int = 0

  def size(self) -> int:
    return self._size
  def is_empty(self) -> bool:
    return self._size == 0
  def push(self, num: int):
    node = ListNode(num)
    if self._front is None:
      self._front = node
      self._rear = node
    else:
      self._rear.next = node
      self._rear = node
    self._size +=1
  def pop(self) -> int:
    num =self.peek()
    self._front = self._front.next
    self._size -= 1
    return num
  
  def peek(self) -> int:
    if self.is_empty():
      raise IndexError(" Queue is empty")
    return self._front.val
  def to_list(self) -> list[int]:
    #转化为列表用于打印
    queue =[]
    temp = self._front
    while temp:
      queue.append(temp.val)
      temp = temp.next
    return queue

class ArrayQueue:
  # 基于环形数组实现的队列
  def __init__(self, size: int):
    self._nums: list[int] = [0]*size #用于存储队列元素的数组
    self._front: int=0 # 队首支针，指向队首元素
    self._size: int=0 # 队列长度
  def capacity(self) -> int:
    return len(self._nums)
  
  def size(self) -> int:
    return self._size
  
  def is_empty(self) -> bool:
    return self._size == 0
  def push(self, num:int):
    if self._size == self.capacity():
      raise IndexError("Queue is full")
    # 计算队尾指针，指向队尾索引+1
    # 通过取余操作实现rear越过数组尾部后回到头部
    rear: int = (self._front + self._size) % self.capacity()
    #将num添加到队尾
    self._nums[rear] = num
    self._size += 1

  def pop(self) -> int:
    num: int = self.peek()
    # 队首支针向后移动一位，若越过尾部，则返回到数组头部
    self._front = (self._front + 1) % self.capacity()
    self._size -= 1
    return num
  
  def peek(self) -> int:
    if self.is_empty():
      raise IndexError
    return self._nums[self._front]
  
  def to_list(self) -> list[int]:
    res = [0] * self.size()
    j: int = self._front
    for i in range(self.size()):
      res[i] = self._nums[(j % self.capacity())]
      j+=1
    return res
  
  """
  还可以通过双向列表实现双向队列"""