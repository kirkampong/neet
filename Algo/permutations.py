# MATH:
# The number of permutations of n objects taken r at a time 
# is given by: P(n,r) = n!/(n−r)!
# The Number of permutations of 'abc' = 3! (n=r=3)

# GET ALL ITER PERMUTATIONS OF A STRING OR LIST:
# NOTE: Use it.permutations(s,r) to take 'r' items at a time
# O(n!)
import itertools as it 
def iterPermutations(s):
  result = []
  perms = list(it.permutations(s))
  for item in perms:
    # for a list input: result.append(list(item))
    result.append(''.join(item))
  return result

# Solution 2 => (recursive):
#                         ______________
#========================| PERMUTATIONs |==========================
#                         --------------
# Given an array of DISTINCT ints, return all possible permutations. 
# You can return the answer in any order.
# Approach:
#   - We could simply use itertools above for n! solutions
#   - We will use a decision tree with backtracking approach
#         Input:    [1,2,3]
#                  /   |   \
#              [2,3] [1,3]  [1,2]
#              /  \   /  \    /  \
#            [3] [2] [3] [1] [2] [1]
#   - Each step down the tree we are choosing to remove one element
#     until we get to the single entry base case
#   - In backtracking upwards we append the removed element at the end
#   - When we reach the end we add the list to our results
#
# Complexity:
#   - O(n * n!) time , O(n!) space
#   - There are n! perms for array of length n. For each permutation, 
#         we need to make n calls to get to the leaves 
def permute(nums):
  result = []
  # base case
  if len(nums) == 1:
    # return a copy so as not to get caught up in a call
    # by reference problem, we want to pass these on by value
    return [nums[:]]
  
  for i in range(len(nums)):
    #moving down: remove first elem and permute rest
    n = nums.pop(0)
    perms = permute(nums)
    # back track: append removed value to perm(subproblem)
    for perm in perms:
      perm.append(n)
    result.extend(perms)
    # moving up: add removed value back to nums
    nums.append(n)
  
  return result

#                        ____________________
#=======================|/END : PERMUTATIONS/|=======================
#                        --------------------


#                         ________________
#========================| PERMUTATIONs II|==========================
#                         ----------------
# Given a list of nums that may contain DUPLICATES, return all possible 
# unique permutations in any order.
# Approach:
#   - We will solve with backtracking like above, but make adjustments
#   - To avoid duplicates, instead of using the array in our decision tree,
#         we will use a hashmap to avoid 'identical children' in our tree
#   - At each decision level our children will be UNIQUE hashmap keys,
#         Counts will track how many times we can use each element
# Complexity:
#   - Might be O(n * 2^n) or n! at worst, not sure
# SHORTCUT: append this to permutations I solutions:
#   - Return list([list(y) for y in (set([tuple(x) for x in perm1solution])]) 

# Solution 1:
def permute(nums):
  result = []
  perm = [] #To build each permutation
  count = {num:0 for num in nums} #Fill hashmap keys
  for num in nums:
    count[num] += 1 #Fill hashmap values

  def dfs():
    #base case
    if len(perm) == len(nums):
      # append a copy cos we have only 1 instance of perm
      # which is updated we want pass by value vs reference
      result.append(perm.copy()) #perm[:]
      return
    
    for num in count:
      if count[num] > 0:
        perm.append(num)
        count[num] -= 1

        dfs()
        # cleanup/backtrack
        count[num] += 1
        perm.pop()

  dfs()
  return result
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# Solution 2:
def permuteUnique(nums):
  ans=[]
        
  def dfs(num,scope):
    if len(scope)==0:
      ans.append(num.copy())
                        
    visited=set()
    for i in range(len(scope)):
      if scope[i] not in visited:
        visited.add(scope[i])
        dfs(num+[scope[i]], scope[:i]+scope[i+1:])
                    
  dfs([],nums)         
  return ans

#                      _______________________
#=====================|/END : PERMUTATIONS II/|=======================
#                      -----------------------


#                     ________________________
#====================| PERMUTATIONs IN STRING |=======================
#                     ------------------------
# Given s1 and s2, return true if s2 contains a permutation of s1.
# ie; return true if one of s1's permutations is the substring of s2.
# eg: s1 = "ab", s2 = "eidbaooo" => True
# Approach
#   - Instead of getting bogged down by permutations, think anagrams
#   - Using a sliding window check every window in s2 of size s1 O(n*m)
#   - We can get O(26n) if all chars are lowercase, we hashmaps:
#        Maintain a hashmap for s1 and one for currWindow in s2
#   - Even better we get O(n) by using 2 hashmaps like above:
#       - Maintain a 'matches[0-26]' variable to track the number of matches
#         of each char between the 2 hashmaps across ascii 'a-z'
#       - As we slide our window, update hashmap_s2 and matches[26]

# Solution 2 (O(26) sliding window and Counter hashmap):
from collections import Counter
def checkInclusion(s1, s2):
  l = 0
  r = len(s1)
  s1Count = Counter(s1) #collections.Counter(s1) w/out import 
  while r <= len(s2):
    if s1Count == Counter(s2[l:r]):
      return True  
    l += 1
    r += 1     
  return False

# ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---  ---

# Solution 1 (Best O(n)):
def checkIncludesPerm(s1,s2):
  if len(s1) > len(s2):
    return False
  if s1 == s2 or s1[::-1] == s2:
    return True
  # We can use arrays instead since we have fixed values
  # convert chars to integers and use as indices
  s1Count = [0]*26
  s2Count = [0]*26

  # set s1Count and first few indices of s2
  for i in range(len(s1)):
    s1Count[ord(s1[i]) - ord('a')] += 1
    s2Count[ord(s2[i]) - ord('a')] += 1
  
  matches = 0
  for i in range(26):
    matches += (1 if s1Count[i] == s2Count[i] else 0)
  
  # construct sliding window
  left = 0
  for right in range(len(s1), len(s2)):
    if matches == 26:
      return True

    # RIGHT SIDE 
    # new window member
    index = ord(s2[right]) - ord('a') 
    s2Count[index] += 1
    # new window mem has matching count with s1
    if s1Count[index] == s2Count[index]:
      matches += 1
    # new window mem overshot our count with s1
    elif s1Count[index] + 1 == s2Count[index]:
      matches -= 1
    
    # LEFT SIDE 
    # new window member
    index = ord(s2[left]) - ord('a') 
    s2Count[index] -= 1
    # new window mem has matching count with s1
    if s1Count[index] == s2Count[index]:
      matches += 1
    # new window mem undershot our count with s1
    elif s1Count[index] - 1 == s2Count[index]:
      matches -= 1
    
    left += 1
  
  return matches == 26 #(last run may match all)

#                     _______________________
#====================|/END : PERMS IN STRING/|====================
#                     -----------------------


#                        __________________
#=======================| NEXT PERMUTATION |=======================
#                        ------------------
# The next permutation of an array of integers is the next lexicographically 
# greater permutation of its integer. More formally, if all the permutations 
# of the array are sorted in one container according to their lexicographical 
# order, then the next permutation of that array is the next entry
# Eg: [1,3,4,2,3,4] -> [1,3,4,2,4,3]
#
# Approach: find pivot, work backward, find first match > currPivot, swap
def nextPermutation(nums):
  N = len(nums)
  pivot = 0

  # Walk backwards to find picot
  for i in range(N-1,0,-1): #We're not checking first
    if nums[i-1] < nums[i]:
      pivot = i
      break

  if pivot == 0: # we are at max lexicography
    nums.sort()
    return #break??

  # walking backwards again then find the swap which first number > pivot
  swap = N-1
  while nums[pivot-1] >= nums[swap]:
    swap -= 1

  #swap
  nums[swap],nums[pivot-1] = nums[pivot-1],nums[swap]
  nums[pivot:] = sorted(nums[pivot:]) # can use reversed instead of sorted


#                        __________________
#=======================| K'TH PERMUTATION |=======================
#                        ------------------
# Given n and k, return the kth element of its ordered permutation sequence.
# Input is n: [1,2,3..n] Eg: 3: [1,2,3] ; k = 5
"123"
"132"
"213"
"231"  # we know at k=5, perm starts with 3 : 
"312"  # [3] + perm(1,2)
"321"
# take advantage of ordering
# index = k-1 , 
# factorial = 3 * 2 * 1  (3==n)
# nums:[1,2,3]
# 1st elem = index/2 = nums[2], 2nd elem = 1stElem/2 = nums[0]

def getKthPermutation(n,k):
  # array in question = [1,2,3...., n]
  nums = [str(i) for i in range (1,n+1)]
  output = []
  factorial = math.factorial(n)
  index = k-1

  while (nums):
    factorial = factorial // len(nums)
    pos = index // factorial
    number = nums.pop(pos)
    output.append(number)
    index = index % factorial

  return ''.join(output)



#                        ________________________
#=======================| RECONSTRUCT PERMUTATION |=======================
#                        ------------------------
# A permutation(6) array of size 6(N) can be given as: [6,5,1,3,2,4]
# The derivative:
# min in A is at [position 3] , we remove it giving us [6,5,3,2,4]
# The next minimum is at [position 4], we remove it giving us [6,5,3,4]
# keep going, and derivative is the collection of positions!

# permutation(6) = [6,5,1,3,2,4] , derivative = [3,4,3,3,2,1]
# From the derivative, reconstruct the original array!!!

# derivative = [3,4,3,3,2,1]
#             /             \
#           pos(1)          pos(6)

# go right to left, of derivative, positions, while going N -> 1 in value
# at each iteration, slot the value at the position relative to the ones placed
# so far
# O(N^2)

# Approach:
#   - Initialize empty array(N), Then place 1(smallest) in array[der[0]]
#   - Recursively get number of free indexes on left side and right side
#   - Construct a tree on top of the array with free indexes as vals(pic)
#     We can tell which direction to go to get to that index

# input > der: [3,4,3,3,2,1]
# (placing second - index 4, value 2)
# tree:         5     
#             /   \    go right to place, we place in (4-2)th index on right
#           2       3                                 /   \
#         / \       | \  \                        index    leftNode val
#       [  |  | 1 |  |  |  ]
#  Then update right subtree, 3 -> 2 and repeat
#  WE NEED A SEGMENT TREE ???
# 
#  




# OR TRY DISJOINT SET UNION ??
# Path Compression for DSU
def find(parent, vertex):
    if vertex == parent[vertex]:
        return vertex
    parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def main(derivative):
    # Account for 1-indexing
    derivative = list(map(lambda x : x - 1, derivative))
    N = len(derivative)
    # parent[i] stores the next free index after and including i
    parent = list(range(N))

    permutation = [None] * N
    for i, der in enumerate(derivative):
        count, j = 0, find(parent, 0)
        while count < der:
            j = find(parent, j + 1)
            count += 1
        permutation[j] = i + 1
        parent[j] += 1
        
    return permutation

