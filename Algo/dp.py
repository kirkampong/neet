
# CLIMBING STAIRS:
# You are climbing a staircase. It takes n steps to reach the top. Each time you 
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Approach:
#   - At each step we have 2 options, think of it as a decision tree, it can be brute-forced
'''   BRUTE FORCE O(2^n)
      def decisionTrue(n):
        def dfs(currSteps):
          if currSteps == n: return 1
          if currSteps > n: return 0
          return dfs(currSteps+1) + dfs(currSteps+2)
        return dfs(0)
'''
#   - We'll have many duplicate subtrees in our decision tree. We can use memoization O(n)
#   - DP: Use a bottom-up approach : initialize an array dp of length n+1 (0 is start, index = currStep)
#   - We'll go right --> left. Fill last elem with 1, then going backwards ask how many ways
#     we can reach the destination from currStep and fill in with that:
#     Eg: n=5 -> [8,5,3,2,1,1] (NOTE: last 2 entries are ALWAYS 1,1)
#     Intuitively, we see that each entry is the sum of the 2 entries to its right
#     So we can store only the 2 values (one,two)to the right of curr, not the whole dp array
#
# NOTE: if you consider the base cases of dp[n] = 0, dp[n-1] = 1, dp[n-2] = 2, 
#     there is no confusion regarding why dp[n] = 1.
def climbStairs(n):
  one,two = 1,1
  for i in range(n-1):
    temp = one
    one = one + two
    two = temp
  return one


# COIN CHANGE:
# Given an int array of coin denominations and an integer for total amount of money, Return the fewest 
# number of coins that you need to make up that amount. If that amount of money cannot be made up by any 
# combination of the coins, return -1. Assume that you have an infinite number of each kind of coin.
# Approach:
#   - A Greedy approach taking the largest coin first as many times as we can, then going progressively
#     lower, actually DOES NOT work
#   - We can brute force using decision Tree DFS with backtracking.
#   - Root is target Amount, Each child branch is a choice of denomination, 
#     each node value is the remaining based on choice: eg:[1,3,4,5]; Amt:7
#                                    7*
#                               1/ 3/ 4\  5\ 
#                               /  /    \   \
#                              6  4     3    2
#   - Use a bottom-up approach:
#   - DP[0] = 0 -> 0 is the min number of coins to sum to 0
#   - DP[1] = 1; DP[2] = DP[1] + 1 = 2 (we just add a coin value '1')
#   - DP[3] = 1; DP[4] = 1; DP[5]=1; DP[6] = 2;
#   - DP[7] = (1 + DP[6] = 1+2 = 3) or (1 + DP[4] = 2) or (1 + DP[3] = 2)  or (1 + DP[2] = 3)
# Time Complexity : O(amount * len(coins))
def coinChange(coins, amount):
  # default value couls be infinity of math.max
  dp = [amount+1]*(amount+1) #for target 7:dp[0],dp[1]...dp[7]
  dp[0] = 0

  for a in range(1,amount+1):
    for coin in coins:
      if a - coin >= 0:
        #eg; coin:4,a:7 => dp[7] = 1+dp[3]
        dp[a] = min(dp[a], 1 + dp[a - coin])
  
  # if dp[amount] is still default value return -1
  if dp[amount] != amount+1:
    return dp[amount] 
  return -1


# LONGEST INCREASING SUBSEQUENCE:
# Given an array nums, return the length of the longest strictly increasing subsequence
# A subsequence can be derived by DELETING some or no elements without changing the order of 
# the remaining elements. Eg; [3,6,2,7] is a subsequence of [0,3,1,6,2,2,7].
# Approach O(n^2):
#   - A brute force dfs has 2 choices for each num so O(2^n). let's try a dfs decision tree.
#   - We can cache the longest increasing subSeq starting at each index using DP
#   - DP: eg: [1,2,4,3] => Start from last index (3) w/length of sequence 1
#   - dp[3] = 1 , dp[2] = max(1, 1+dp[3]) but increase condition is failed so = 1
#   - dp[1] = max(1, 1+dp[3])= 2 ; dp[0] = max(1, 1+dp[1]) = 3
def lengthOfLIS(nums):
  LIS = [1] * len(nums)
  # go right to left, 
  # inner loop going to choose or delete any num
  for i in range(len(nums)-1, -1, -1):
    for j in range(i+1, len(nums)):
      if nums[i] < nums[j]:
        LIS[i] = max(LIS[i], 1+LIS[j])
  
  return max(LIS)


# LONGEST COMMON SUBSEQUENCE:
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string with some or no characters deleted without changing the 
# order of the remaining characters. Eg; "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# Approach O(n*m):
#   -  SEE LCS.PNG!!: go from left to right, bottom to top.
#   -  For each cell if there's a match set it to (1 + value of cell to south-east/bottom-right diag), 
#         else set it to max of cells below and to the right
def longestCommonSubsequence(text1,text2):
  dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

  # nested loop to fo thru grid in reverse (starting bottom right)
  for i in range(len(text1)-1, -1, -1):
    for j in range(len(text2)-1, -1, -1):
      if text1[i] == text2[j]:
        dp[i][j] = 1 + dp[i+1][j+1]
      else:
        dp[i][j] = max(dp[i][j+1], dp[i+1][j])
  
  # ans in topLeft
  return dp[0][0]


# WORD BREAK:
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
# space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Complexity:  O(n*m..*n(check for match)) => O(m*n^2)
# Approach:
#   - Would be O(n^2) JUST to get every possible substring of s :/
#   - Instead, decisionTree: Check every dict word and using its length L check first L chars in string
#   - Eg: S = "neetcode"  ; dict = ['neet','leet','code']
#
#                                    i=0 (index)
#                                 /   |   \
#                         (i=4)neet  leet  code
#                         /   |    \
#                     neet   leet  (i=8)code
#                                     DONE!
#
#   - Also if we notice there is no solution from a given index eg(i=5) store that so if it appears in 
#     the tree again we know its a dead end
#
#   - REVERSE ORDER OF ABOVE EXAMPLE:
#       DP[8] = True (base case, empty string)                            ->   ""
#       DP[7] = False (not enough characters to match any words in dict)  ->   "e"  
#       DP[6] = DP[5] = False                                             ->   "de", "ode" 
#       DP[4] = True (matches code)                                       ->   "code" 
#       DP[3] = DP[2] = DP[1] = False                                     ->   "tcod", "etco", "eetc"
#       DP[0] = True (matches neet, so return DP[0+len(w)] = DP[4] = True)
def wordBreak(s, wordDict):
  dp = [False] * (len(s)+1)
  dp[len(s)] = True # basecase

  for i in range(len(s)-1,-1,-1):
    for w in wordDict:
      if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
        dp[i] = dp[i + len(w)]
      if dp[i]:
        break
  
  return dp[0]


# COMBINATION SUM:
# Given an array of distinct integers 'candidates' and an integer target, return a list of ALL
# unique combinations of candidates where the chosen numbers sum to target.
# NOTE: The same number may be chosen from candidates an unlimited number of times. 
# 2 combinations are unique if the frequency of at least one of the chosen numbers is different.
# Approach:
#   - SEE CombSum.PNG!
#   - It's important to eliminate duplicate combinations while using a decision tree
#   - Each branching in our tree represents a decision not to include a given number
#   - We will maintain a pointer, every num at ptr and to its left is excluded from our selection
def combinationSum(candidates, target):
  result = []
  # i:exclusionPtr, curr:currCombination, total:currTotal
  def dfs(i,curr,total):
    if total == target:
      result.append(curr.copy()) # reference issues
      return
    if i >= len(candidates) or total > target:
      return
    
    curr.append(candidates[i])
    dfs(i,curr,total+candidates[i]) # include candidate at idx i
    curr.pop() #cleanup/backtrack
    dfs(i+1, curr,total) #exclude candidate at idx i

  dfs(0,[],0)
  return result


# COMBINATION SUM II:
# Same as above, but each number in candidates may only be used ONCE in the combination
# Approach:
#   - Similar decision tree as above, however...
#   - When we decide to exclude a num eg: 1, we're deciding to exclude ALL 1's (eliminates duplicates)
#   - We will shift our exclusionPtr until we reach a different value
def combinationSum2(candidates, target):
  candidates.sort()
  result = []
  # i:exclusionPtr, curr:currCombination, target:remainderToTarget
  def backtrack(pos,curr,target):
    if target == 0:
      result.append(curr.copy()) # reference issues
    if target <= 0:
      return
    
    prev = -1
    for i in range(pos,len(candidates)):
      if candidates[i] == prev: # skip duplicates
        continue
      curr.append(candidates[i])
      backtrack(i+1, curr, target-candidates[i])
      curr.pop() #cleanup/backtrack
      prev = candidates[i]
  
  backtrack(0,[],target)
  return result


# HOUSE ROBBER:
# You are planning to rob houses along a street, but you CANNOT ROB ADJACENT HOUSES!
# Given an integer array nums: the amount of money of each house, return the maximum amount 
# of money you can rob tonight.
# Approach O(N):
#   - Decision Tree/Subproblem: starting with a decision to rob the 1st house or not gives us:
#       rob = max(arr[0]+rob[2:n], rob[1:n]).
#   - Go through the array, at each index, figure out what the MAX value of robbing possible 
#       up until that index. We may or may not include the current index.
#   - We actually only need to tracks the previous 2 rob values which will be 
#       our 2 maximums so far
def rob(nums):
  # prev 2 rob values
  rob1, rob2 = 0, 0
  for n in nums:
    newRob = max(n + rob1,rob2) #(include n, exclude n)
    rob1 = rob2
    rob2 = newRob
  return rob2


# HOUSE ROBBER II (CIRCULAR STREET):
# Same as above, except the houses are arranges in a circle so the 1st house is next 
# to the last house
# Approach:
#   - We will re-use the solution from House Robber I
#   - We can run House Robber I on the array EXCLUDING the first value, and then run it 
#       on the array EXCLUDING the last value, then return the max of the 2
def rob2(nums):
  # consider nums[0] since we could have a single element in nums
  return max(nums[0], rob(nums[1:]), rob(nums[:-1]))


# DECODE WAYS:
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A'->"1"...'Z'->"26". To decode a message, all digits must be grouped then mapped back to letters
# Eg; "11106" can be mapped into: "AAJF" w/grouping (1 1 10 6) OR "KJF" w/grouping (11 10 6)
# Given a string s containing only digits, return the number of ways to decode it.
def numDecodings(s):
  # Memoization - DFS
  dp = {len(s): 1}
  def dfs(i):
      if i in dp: return dp[i]
      if s[i] == "0": return 0

      res = dfs(i + 1)
      if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
          res += dfs(i + 2)
      dp[i] = res
      return res
  return dfs(0)
# OR USE Dynamic Programming
def numDecodings2(s): 
  dp = {len(s): 1}
  for i in range(len(s) - 1, -1, -1):
      if s[i] == "0":
          dp[i] = 0
      else:
          dp[i] = dp[i + 1]

      if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
          dp[i] += dp[i + 2]
  return dp[0]

# UNIQUE PATHS:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner 
# (i.e., grid[0][0]). It tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right.
#
# GIVEN the two integers m and n, return the number of possible unique paths that the robot 
# can take to reach the bottom-right corner.
# Approach o(NxM):
#   - SEE UniquePaths.png
#   - We always have 2 decisions, go down or go right. 
#   - We will keep a cache to store the result (numPaths) for positions we have explored
#   - For every pos(r,c) the numWays is a sum of the numWays of cells to its right and bottom
#   - Bottom up approach, START from the destination itself, theres 1 PATH for that cell itself
#   - Going row by row leftward and upward, (it'll fill our bottom row with 1's)
def uniquePaths(m,n):
  row = [1] * n # bottom row
  for i in range(m - 1): #other rows
    newRow = [1] * n
    #go through every column except rightmost since its also filled with 1's
    for j in range(n - 2, -1, -1):
      newRow[j] = newRow[j + 1] + row[j]
    row = newRow

  return row[0] 

# JUMP GAME:
# Given an integer array nums. You are initially positioned at the first index, and each element 
# in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
def canJump(nums):
  goal = len(nums) - 1

  for i in range(len(nums) - 2, -1, -1):
      if i + nums[i] >= goal:
          goal = i
  return goal == 0