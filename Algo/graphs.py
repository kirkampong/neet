from collections import defaultdict
 
# Build graph from undirected edges
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
     
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

# CLONE GRAPH:
# Given a reference of a node in a connected undirected graph. 
# Return a deep copy (clone) of the graph.
# O(n)
def cloneGraph(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None

# COURSE SCHEDULE: (topologicalSort)
# You have to take courses labeled from 0 to numCourses - 1. There's an array prerequisites where 
# prerequisites[i] = [ai, bi] means you must take course bi first to take course ai.
# Return true if you can finish all courses. Otherwise, return false
# O(n+p)
# Approach:
#   - Use an adjacency list(map) : a graph connection from 1 -> 0 means 0 is a preReq for 1
#   - Run DFS starting from a node, on its neighbors. when we get to a course with no preReqs,
#       we know it CAN be completed,
#   - Then we backtrack, for each node remove from courses we know CAN be completed from its preReqs
#   - Maintain a visited set to prevent cycles
def canFinish(numCourses, prerequisites):
  # create map from course to prereq list
  requiredMap = {i:[] for i in range(numCourses)}
  for course, pre in prerequisites:
    requiredMap[course].append(pre)

  visited = set()
  def dfs(course):  
    if course in visited: # cycle
      return False
    if requiredMap[course] == []: # course has no preReqs
      return True
    
    # visit course
    visited.add(course)
    for pre in requiredMap[course]:
      if not dfs(pre): return False
    visited.remove(course)

    # small optimization : memoize - We know it CAN be completed so mark as having no preReqs
    requiredMap[course] = []

    return True
  
  for course in range(numCourses):
    if not dfs(course): return False
  return True

# COURSE SCHEDULE II: 
# You have to take courses labeled from 0 to numCourses - 1. There's an array prerequisites where 
# prerequisites[i] = [ai, bi] means you must take course bi first to take course ai.
# Return the ORDERING of courses you should take to finish all courses.
def findOrder(numCourses, prerequisites):
  preMap = {c:[] for c in range(numCourses)}
  for course, pre in prerequisites:
    preMap[course].append(pre)

  # a course has 3 possible states: unvisited, visited (added to output) &
  # visiting -> not added to ouput, but added to cycle
  output = []
  visited,cycle = set(),set()

  def dfs(course):
    if course in cycle: return False
    if course in visited: return True # continue/pass
    cycle.add(course)
    
    for pre in preMap[course]:
      if dfs(pre) == False:
        return False
    cycle.remove(course)
    visited.add(course)
    output.append(course)
    return True
  
  for course in range(numCourses):
    if dfs(course) == False: #cycle
      return []
  return output

# COURSE SCHEDULE III: 
# Given n courses, where courses[i] = [duration(i), lastDay(i)] indicates that the ith course 
# should be taken continuously for duration(i) days and must be finished before or on lastDay(i).
# You start on the 1st day and cannot take two or more courses simultaneously.
# Return the maximum number of courses that you can take.
# Approach (Greedy):
#   - First sort by end time helps maximize numCourses we can take by minimizing endTime
#       eg: [[100,200],[1000,1250],[200,1300],[2000,3200]]
#   - Iterate thru above, maintaining a list to track the durations also tracking total_time taken, 
#       and checking if it exceeds endTime of curr entry
#   - If total_time exceeds endTime of curr, pop off the LARGEST duration (we will use a max heap)
#   - Return length of durations list
import heapq
def scheduleCourse(courses):
  # sort by end time
  courses.sort(key = lambda x:x[1])
  heap = []
  total_time = 0

  for duration,endTime in courses:
    heapq.heappush(heap,duration)
    total_time += duration
    if total_time > endTime:
      biggest_time = heapq.heappop(heap)
      total_time -= biggest_time
  
  return len(heap)


# LONGEST CONSECUTIVE SEQUENCE:
# Given an unsorted array of integers, return the length of the longest 
# consecutive elements sequence. It must run in O(n) time!
# Approach:
#   - We can sort nums and iterate to find answer but its O(nlogn)
#   - Eg: [100,4,200,1,3,2] -> we want to group them as such: {1,2,3,4},{100},{200}
#   - To get the start of each group, find nums without a left neighbor (one less) - use a set
#   - Then to get length of that group sequence check for consecutive elements in our set
# Complexity: we visit each element at most twice so O(n)
def longestConsecutiveSeq(nums):
  numSet = set(nums)
  longestSeq = 0
  for num in nums:
    # check if num is start of sequence
    if (num-1) not in numSet:
      currLen = 0
      while (num + currLen) in numSet:
        currLen += 1
      longest = max(currLen,longestSeq)
      
  return longestSeq

# ALIEN DICTIONARY: (TOPOLOGICAL SORT)
# Given a sorted dictionary (array of words) of an alien language, find the order of all 
# unique characters in the language. The language uses lowercase english alphabets.
# If there's no solution return ""
# Approach:
#   - Go through consecutive pairs in wordsDict, comparing char by char and build a graph
#       where a->b means a 'comes before' b
#   - Then traverse the graph to spit out the right ordering (we'll use DFS)
#   - Cycles in our graph represent invalid contradictions, return ""
#                                                      /--------|
#                                                     |         v
#   - CATCH: We need a POST ORDER DFS: so if we have  A -> B -> C, We don't return 'A,C,B,C'
#     We will add a node to output when we get to a leaf! This will give us a reverse order
def alien_order(words):
  # for each char in our list of words map it to a set()
  adjList = {} # = {c:set() for w in words for c in w}
  for w in words:
    for c in w:
      adjList[c] = set()

  # maybe: handle ["z", "z"], or ["aba"]
  if not words: return ""
  if len(set(words)) == 1: 
    return "".join(set(c for c in words[0]))

  # iterate thru pairs of words
  for i in range(len(words)-1):
    first,second = words[i], words[i+1]
    minLen = min(len(first),len(second))
    #if prefixes are identical but longer comes first, invalid
    if len(first)>len(second) and first[:minLen] == second[:minLen]:
      return ""
    # go through chars
    for j in range(minLen):
      if first[j] != second[j]:
        adjList[first[j]].add(second[j])
        break

    # DFS! We'll need to track both visited and inCurrPath so use dict
    # map nodes to False(visited),True(visited AND in currPath)
    visited = {}
    result = []
    
  def dfs(ch):
    if ch in visited:
      return visited[ch] # returns True if loop detected
    visited[ch] = True #visited and in currPath
    for neighbor in adjList[ch]:
      if dfs(neighbor):
        #loop detected
        return True
    visited[ch] = False #visited but not in currPath
    result.append(ch)
  
  for ch in adjList:
    if dfs(ch):
      return ""
  
  result.reverse()
  return "".join(result)

# VERIFY AN ALIEN DICTIONARY:
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.
# Approach:
# The idea is to look at pairs of adjacent words and look for first different symbol, eg; hello and help 
# means 'o' comes before 'p'. Also need to deal with cases like if 'hello' is before 'hell', return False.
# Complexity:
# O(m), where m is the total length of all words in words.
def isAlienSorted(words, order):
  ord_d = {l:i for i, l in enumerate(order)}
  for w1, w2 in zip(words, words[1:]):
      for i, j in zip(w1, w2):
          if i != j:
              if ord_d[i] > ord_d[j]: return False
              break
      if w1.startswith(w2) and w1 != w2: return False
      
  return True

# GRAPH IS VALID TREE:
# Given n nodes labeled from 0 to (n-1) and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
# (Assume no duplicate edges. Since edges are undirected, [0, 1] is the same as [1, 0])
# Approach O(E+V):
#   - A Tree must: [be connected] AND [have no loops]
#   - Create a list of neighbors for every input node, starting from 0, Do a DFS graph traversal
#   - At the end check of the number of visited nodes matches num inputNodes
#   - Also check we didn't encounter any cycles or loops!
#      (To be able to check for loops we keep track of prevNode, since it's an undirected graph)
def valid_tree(n, edges):
  if not n: return True
  adjList = {i:[] for i in range(n)}
  for n1,n2 in edges:
    adjList[n1].append(n2)
    adjList[n2].append(n)

  visited = set()
  def dfs(i,prev):
    if i in visited:
      return False
    visited.add(i)

    for j in adjList[i]:
      if j == prev: 
        continue
      if not dfs(j,i):
        return False #loop detected
    return True
  
  return dfs(0,-1) and len(visited) == n

# PACIFIC ATLANTIC WATER FLOW:
# Given an m x n rectangular island with values representing the height above sea level, The matrix 
# The Pacific Ocean borders the LEFT AND TOP edges, and Atlantic, the RIGHT AND BOTTOM.
# Return a list of coordinates result where result[i] = [ri, ci] denotes that rain water can flow from 
# the cell to both the Pacific and Atlantic oceans. 
# Water can only flow in 4 directions to a cell of lower or equal height!
# APPROACH O(n*m):
#   - We can dfs from each cell O((nm)^2) ; Eliminate repeated work
#   - We can start from each ocean, find all its bordering cells, then start dfs from each border cell,
#     we find the other cells that can also reach that ocean, return intersection of the 2 results
#   - Since we're starting dfs from border cells, we only move to cells with height >= curr.
#   - Keep track of previous Height so we move to valid cells
def pacificAtlantic(heights):
  numRows, numCols = len(heights), len(heights[0])
  pacific, atlantic = set(), set() # visited sets
  #result = []
  
  def dfs(row,col,visited,prevHeight):
    if (row,col) in visited or \
        row < 0 or row >= numRows or \
        col < 0 or col >= numCols or \
        heights[row][col] < prevHeight:
          return

    visited.add((row,col))

    dfs(row+1,col,visited,heights[row][col])
    dfs(row-1,col,visited,heights[row][col])
    dfs(row,col+1,visited,heights[row][col])
    dfs(row,col-1,visited,heights[row][col])

   # visited.remove((row,col))
      
  # start from top row (pac) and bottom row(atl)
  for col in range(numCols):
    dfs(0,col,pacific,heights[0][col]) 
    dfs(numRows-1,col,atlantic,heights[numRows-1][col])
  
  # start from left col(pac) and right col(atl)
  for row in range(numRows):
    dfs(row,0,pacific,heights[row][0])
    dfs(row,numCols-1,atlantic,heights[row][numCols-1])
  
  # check for cells reachable from pacific AND atlantic
  result = []
  for row in range(numRows):
    for col in range(numCols):
      if (row,col) in atlantic and (row,col) in pacific:
        result.append([row,col])

  return result