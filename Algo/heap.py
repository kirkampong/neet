
# KTH SMALLEST ARRAY ELEM IN LINEAR TIME:
# https://www.tutorialspoint.com/program-to-find-kth-smallest-element-in-linear-time-in-python

# TOP K FREQUENT ELEMENTS (Bucket Sort):
# We can get a O(k*logN) solution with a heap but we can do even better:
# Approach O(N):
#   - First create a hashmap to count the num occurrences of each value
#   - Trick: Create a 2D arr freq of counts to values. eg: from [1,1,1,2,2,7,100]
#       each index will be a count and the value will be all nums with THAT freq count
#       we get: [[],[100,7],[2],3] NOTE: len(map) <= len(inputNums)
#   - After building map, traverse it backwards, starting with highest count
#       and populate the 2 highest freq nums
def topKFrequent(nums,int):
  count = {}
  freq = [[]for i in range(len(nums)+1)]
  # build count hashmap
  for n in nums:
    count[n] = 1 + count.get(n,0)
  # build trick freq hashmap
  for n, c in count.items():
    freq[c].append(n)
  
  result = []
  for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
      result.append(n)
      if len(result) == k:
        return result
  
