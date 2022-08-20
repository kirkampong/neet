# 2SUM - single pass
def twoSum(nums, target):
  # returns indices
  hashMap = {}
  for i, n in enumerate(nums):
    diff = target - n
    if diff in hashMap:
      return hashMap[diff] # return i too?
    hashMap[n] = i
  return


# TIME TO BUY AND SELL STOCK 
# Approach (sliding window): 
#   - Use 2 pointers starting on 1st and 2nd positions
#   - if R val < L val increment both else check profit, increment R and repeat
def maxProfit(prices):
  leftIdx,rightIdx = 0,1
  maxProfit = 0
  while rightIdx < len(prices):
    # profitable 
    if prices[leftIdx] < prices[rightIdx]:
      profit = prices[rightIdx] - prices[leftIdx]
      maxProfit = max(profit, maxProfit)
    else:
      leftIdx = rightIdx
    rightIdx += 1
  return maxProfit

# CONTAINS DUPLICATE
# return true if any value appears at least twice
def containsDuplicate(nums):
  hashset = set()
  for n in nums:
    if n in hashset:
      return True
    hashset.add(n)
  return False

# PRODUCT OF ARRAY EXCEPT SELF
# Given an array of nums return an array where answer[i] is a product of all elements
#   of nums except nums[i]
# Approach: 
# - Create 3 arrays: a prefix(cumulative multiples to right) and postfix arrays (vice versa), 
#   to save memory we can use the output array to store these 2.
# - use output array in each index store the pre/post fix product up till that idx (start from 1)
def productExceptSelf(nums):
  result = [1] * len(nums)
  prefix = 1
  for i in range(len(nums)):
    result[i] = prefix
    prefix = prefix * nums[i]
  postfix = 1
  for i in range(len(nums)-1,-1,-1):
    result[i] = result * postfix #result[i]*postfix?
    postfix = postfix * nums[i]
  return result

# MAXIMUM SUBARRAY SUM
# Approach: 
# (Sliding window): keep a left and right pointer, update left whenever we're at a negative prefix
# Edge case (handled): if all entries are negative just return the max of the array
def maxSubArraySum(nums):
    maxSub = nums[0]
    currSum = 0
    for num in nums:
      if currSum < 0:
        currSum = 0
      currSum += num
      maxSub = max(maxSub, currSum)
    return maxSub

# MAXIMUM SUBARRAY PRODUCT
# Approach: 
# IF we have all positives, we just multiply all, 2 negatives make positive so we must track
# both max and min subarray so far as we go along. Zero must also be handled by resetting 
# max and min to 1. We must init result as max(nums) as a good default and currMin, currMax = 1
def maxSubArrayProduct(nums):
    result = max(nums)
    currMin, currMax = 1,1
    for num in nums:
        if num == 0: # this if statement not rly needed
          currMin, currMax = 1,1
          continue
        temp = currMax*num
        currMax = max(num*currMax, num*currMin,num)
        currMin = min(temp, num*currMin,num)
        result = max(result,currMax)
    return result

# MINIMUM IN ROTATED SORTED ARRAY  -> O(logn) time 
# Approach: 
# Adjusted Binary search approach -> keep a left, right and middle pointer, assume 'm' points
# to pivot (currMinValue) to figure out to search leftSorted portion or right for the min,
# we will check left value so if nums[m] >= nums[l] the lowest is in our right sortedPortion
# so search right else search left
def findMinRotatedSorted(nums):
    result = nums[0] #random
    leftIdx, rightIdx = 0, len(nums)-1
    # ('or equal' is needed cos m == l is possible)
    while leftIdx <= rightIdx:
        # if subarray is already sorted return leftMost
        if nums[leftIdx] < nums[rightIdx]:
            result = min(result, nums[leftIdx])
            break
        midIdx = (leftIdx + rightIdx) // 2
        result = min(result,nums[midIdx])
        #if midVal >= leftVal search right else left
        if nums[midIdx] >= nums[leftIdx]:
            leftIdx = midIdx + 1
        else:
            rightIdx = midIdx - 1
    return result

# SEARCH IN ROTATED SORTED ARRAY  -> O(logn) time, return index of target
# Approach:
# Binary search; we have 2 sorted halves, maintain 3 pointers as usual.
# if mid >= left mid value belongs to left else mid value belongs to right
# if we are in the leftSorted half:
# if (target is less than first entry in leftSide), search right side else search leftSide
# if we are in the rightSorted half:
# if target is < mid search leftPortion, elif target > mid and <= rightMost search only after mid
def searchRotatedSorted(nums, target):
    leftIdx, rightIdx = 0, len(nums)-1
    # <= cos array could be [1]
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        if target == nums[midIdx]:
            return midIdx
        # In left sorted portion:
        # if target < mid or < leftmost nums val, search right portion
        if nums[leftIdx] <= nums[midIdx]:
            if target > nums[midIdx] or target < nums[leftIdx]:
                leftIdx = midIdx + 1
            else:
                # search left portion so update rightIdx
                rightIdx = midIdx - 1
        # In right sorted portion:
        else:
            if target < nums[midIdx] or target > nums[rightIdx]:
                # search left portion 
                rightIdx = midIdx - 1
            else:
                # search right portion
                leftIdx = midIdx + 1
    return -1

# 3SUM
# Given nums, return all the NON_DUPLICATE triplets that sum to target 0.
# Approach O(n^2):
#   - First sort array to find duplicates by adjacent starting point
#   - For each element, solve 2 sum for the remainder array, using pointers:
#   - Using l and r pointer, if currSum >target, shift l backwards else r forward
def threeSum(nums):
    # Note: target is 0
    result = []
    nums.sort()
    for i,num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue # duplicate found
        # now use 2 ptr 2sum to solve
        left, right = i+1, len(nums)-1
        while left < right:
            threeSum = num + nums[left] + nums[right]
            if threeSum > 0: #target = 0
                right -= 1
            elif threeSum < 0: #target = 0
                left += 1
            else:
                result.append([num, nums[left], nums[right]])
                # update pointers, conditions above will handle right ptr
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return result

# CONTAINER WITH MOST WATER
# Similar to maxArea rectangle histogram https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
# Given an array of heights, There are n vertical lines drawn of vertical height: height[i]).
# Find two lines that together with the x-axis form a container the  holds the most water.
# Return the maximum amount of water a container can store.
# Approach:
#   - For n^2 simply evaluate all combinations with2 loops, for linear time: 
#   - Use 2 pointers at l and r ends (max width to start), always shifting ptr at lower height 
def maxArea(height):
  right = len(height) - 1
  left = 0
  maxArea = -1
  while left < right:
    currArea = (right-left) * min(height[left],height[right])
    #print(currArea)
    if currArea > maxArea:
      maxArea = currArea
      # update pointers
      if height[left] < height[right]:
        left += 1
      elif height[left] >= height[right]:
        right -= 1
      else: # if they're equal shift either, shift right weirdly reduces performance
        left += 1
  return maxArea

# KTH SMALLEST ARRAY ELEM IN LINEAR TIME:
# https://www.tutorialspoint.com/program-to-find-kth-smallest-element-in-linear-time-in-python
