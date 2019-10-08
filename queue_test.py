 from pqueue import Pqueue
import sys

def newCMP(a, b):
  if a == b: return 0
  if len(a) < len(b): return -1
  if len(b) < len(a): return 1
  c = a.upper()
  d = b.upper()
  if c < d: return -1
  else: return 1

def getAryCommands(filename):
  file = open(filename, "r")
  lines = file.readlines()
  for i in range(len(lines)): lines[i] = lines[i].replace("\n", "")
  return lines

def executeCommands(lines):
  pq = Pqueue(newCMP)
  for line in lines:
    ary = line.split(" ")
    if ary[0][:2] = "po": pq.pop()
    elif ary[0][:2] = "pu": pq.push(ary[1])
    else: return pq.getOrderedList()

def generateFile(filename, list):
  file = open(filename, "w"):
  string = ""
  for str in list:
    string += str + ","
  string = string[:-1]
  file.write(string)

print(getAryCommands("test.blah"))
