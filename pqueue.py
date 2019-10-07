# -*- coding: utf-8 -*-
#2n and 2n + 1 and parent is n/2
import random
def my_cmp(a,b):
  if len(a) < len(b): return -1
  if len(a) == len(b): return 0
  return 1

#makes array (of length n) of arrays with a random length (capped at maxLength)
def makeAryAry(n, maxLength):
  output = []
  for idx in range(n):
    length = random.randint(0, maxLength)
    aryToAdd = [1] * length
    #for i in range(length): aryToAdd.append(1)
    output.append(aryToAdd)
  return output

class Pqueue:

  def __init__(self, comparator = my_cmp):
    self.compFunction = comparator
    self.ary = []
    self.ary.append(None)

  #added a method to clear the pqueue without having to sort it
  def clear(self): self.ary = [None]

  def push(self, thing):
    self.ary.append(thing)
    if (len(self.ary) == 2): return
    idx = len(self.ary) - 1
    while(self.compFunction(self.ary[idx], self.ary[int(idx/2)]) == -1):
      self.ary[idx],self.ary[int(idx/2)] = self.ary[int(idx/2)],self.ary[idx]
      idx = int(idx/2)
      if idx < 2: return

  def pop(self):
    if len(self.ary) == 1: return None
    self.ary[1],self.ary[len(self.ary) - 1] = self.ary[len(self.ary) - 1],self.ary[1]
    output = self.ary[-1]
    self.ary.pop(-1)
    idx = 1
    while True:
      left = idx * 2
      right = idx * 2 + 1
      if left >= len(self.ary): return output
      if right >= len(self.ary) and left < len(self.ary):
        cToLeft = self.compFunction(self.ary[idx], self.ary[left])
        if cToLeft == 1: self.ary[idx],self.ary[left] = self.ary[left],self.ary[idx]
        return output
      lToR = self.compFunction(self.ary[left], self.ary[right])
      if lToR == 1: switchIdx = right
      else: switchIdx = left
      if self.compFunction(self.ary[idx], self.ary[switchIdx]) == 1:
        self.ary[idx],self.ary[switchIdx] = self.ary[switchIdx],self.ary[idx]
        idx = switchIdx
      else: return output

  def getOrderedList(self):
    output = []
    while len(self.ary) > 1:
      output.append(self.pop())
    return output
