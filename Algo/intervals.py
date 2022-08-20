'''
Notes:
  - Watch out for >= vs > depending on if we want overlaps to be inclusive or exclusive
'''

# NON-OVERLAPPING INTERVALS: 
# Find min number of intervals to remove so no intervals overlap
# Approach:
#   - Sort by start time
#   - Compare adjacent intervals, always removing the one with the later end time
# Complexity : O(nlogn)
def eraseOverlapIntervals(intervals):
  intervals.sort()
  result = 0
  prevEnd = intervals[0][1]
  for start,end in intervals[1:]:
    if start >= prevEnd:
        prevEnd = end
    else:
        result += 1
        prevEnd = min(end,prevEnd)
  return result


# INSERT INTERVAL: 
# insert an interval into a sorted list of intervals such that there
# are still no overlapping intervals, merge overlapping intervals if needed
# Approach:
#   - Iterate through intervals and Handle 3 cases :
#       interval goes before curr, after curr or overlaps, so merge.

def insertInterval(newInterval, intervals):
    result = []
    for i in range(len(intervals)):
        # if newInterval's end is before start of currInterval
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        # new interval goes after the currInterval
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        # Else we have an overlapping interval so merge intervals
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    result.append(newInterval)
    return result

# MERGE INTERVALS: 
# Merge all overlapping intervals, return an array of non overlapping 
# intervals covering all intervals of the input. (inclusive edges)
# Approach:
#   - Sort by start times, iterate over adjacent intervals, merging if needed
def mergeIntervals(intervals):
    # Sort by start values
    intervals.sort(key = lambda i: i[0])
    result = [intervals[0]] # add first interval for edge case
    for start,end in intervals[1:]:
        lastEnd = result[-1][1] # endTime of latest entry in results
        # overlap, merge
        if start <= lastEnd:
            result[-1][1] = max(lastEnd,end) 
        # no overlap
        else:
            result.append([start,end])
    return result

# MEETING ROOMS:
# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Approach:
#   - sort by start times
#   - if an overlap is detected return false
def canAttendMeetings(intervals):
    intervals.sort(key = lambda x: x[1])
    for i in range(1,len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]
        if  i1[1] > i2[0]: # if i1.end > i2.start
            return False
    return True

# MEETING ROOMS II: (max num of overlaps at any given time)
# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum num of rooms needed for the meetings.
# Approach:
#   - create 2 input arrays, a lis of sorted startTimes and a list of sorted endTimes
#   - iterate over both arrays always checking which is smaller, if a currStart < currEnd 
#     increment count and go to the next start if currEnd < currEnd, decrement count
#   - Stop when we get to end of startList
def minMeetingRooms(intervals):
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    maxCount, currCount = 0,0
    startIdx, endIdx = 0,0
    while startIdx < len(intervals):
        if starts[startIdx] < ends[endIdx]:
            startIdx += 1
            currCount += 1
        else:
            endIdx += 1
            currCount -= 1
        maxCount = max(maxCount, currCount)

    return maxCount