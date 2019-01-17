#! /bin/python


class Node(object):
  def __init__(self, data=None, next=None):
    if next is not None and (not isinstance(next, Node)):
      raise TypeError('next must be type Node')
    self._data = data
    self._next = next

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, d):
    self._data = d

  @property
  def next(self):
    return self._next

  @next.setter
  def next(self, next):
    if not isinstance(next, Node):
      raise TypeError('next must be type Node')
    self._next = next

  def __str__(self):
    return '%s' % (self._data)


if __name__=="__main__":
  node = Node(data=1, next=None)
  datas = [d for d in range(10)]

  current= None
  for d in datas:
    if current is None:
      current = Node(d, next=None)
      root = current
    else:
      tmp = Node(d, next=None)
      current.next = tmp
      current = tmp
  current.next = root.next.next

  slow=root
  fast=root
  visited = root
  while slow is not None:
    fast = slow.next
    visited = fast
    slow = slow.next
    if visited == fast:
      break