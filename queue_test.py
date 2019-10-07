from pqueue import Pqueue
import sys

def newCMP(a, b):
  if a == b: return 0
  if len(a) < len(b): return -1
  if len(b) < len(a): return 1
  a = a.upper()
  b = b.upper()
  if a < b: return -1
  else: return 1

def getAryCommands(filename):
  file = open(filename, "r")
  lines = file.readlines()
  for i in range(len(lines)): lines[i] = lines[i].replace("\n", "")
  return lines

def executeCommands():
  pq = Pqueue(newCMP)



print(getAryCommands("test.blah"))
