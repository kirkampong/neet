



# VALID ANAGRAM
# O(n) memory and time, 
# Note: For O(1) space -> return sorted(s) == sorted(t)
from collections import Counter
def isAnagramCheat(word1,word2):
  return Counter(word1) == Counter(word2)

def isAnagram(word1,word2):
  if len(word1) != len(word2):
    return False
  count1, count2 = {},{}
  for i in range(len(word1)):
    count1[word1[i]] = 1 + count1.get(word1[i],0)
    count2[word2[i]] = 1 + count2.get(word2[i],0)
  for c in count1:
    if count1[c] != count2.get(c,0):
      return False
  return True


# GROUP ANAGRAMS
# Given an array of strings strs, group the anagrams together. O(m*n) 
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict
def groupAnagrams(strs):
  result = defaultdict(list) # maps charCount to list of anagrams
  for s in strs:
    count = [0] * 26 # a...z
    for c in s:
      count[ord(c)-ord("a")] += 1
    result[tuple(count)].append(s)
  return result.values()


# VALID PARENTHESES:
# Given s containing just the chars '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
def isValidParentheses(s):
  stack = []
  closeToOpen = {")":"(","]":"[","}":"{"}
  for c in s:
    if c in closeToOpen:
      if stack and stack[-1] == closeToOpen[c]:
        stack.pop()
      else:
        return False
    else:
      stack.append(c)
  return True if not stack else False

# VALID PALINDROME:
# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward.
def isPalindrome(s): # O(n) memory
  newStr = ""
  for c in s:
    if c.isalnum():
      newStr += c.lower()
  return newStr == newStr[::-1]

def isPalindrome2(s): # O(1) memory : pointers
  l, r = 0, len(s) - 1
  while l < r:
    while l<r and not alphaNum(s[l]):
      l += 1
    while r > l and not alphaNum(s[r]):
      r-= 1
    if s[l].lower() != s[r].lower():
      return False
    l += 1
    r -= 1
  return True

def alphaNum(c):
  return (ord('A') <= ord(c) <= ord('Z') or
          ord('a') <= ord(c) <= ord('z') or
          ord('0') <= ord(c) <= ord('9'))


# LONGEST SUBSTRING W/OUT REPEATING CHARACTERS:
# Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
  # sliding window on window's charSet
  result = 0
  charSet = set()
  left = 0
  # write loop so l always trails r
  for right in range(len(s)):
    while s[right] in charSet:
      charSet.remove(s[left])
      left += 1
    charSet.add(s[right])
    result = max(result, right-left+1)
  return result

print(lengthOfLongestSubstring(s))


# LONGEST REPEATING CHARACTER REPLACEMENT:
# Given a string s and an integer k. You can choose any character of the string and 
# change it to any other uppercase English character. You can perform this operation 
# at most k times. Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.
# Approach:
#   - Use sliding window and map of letter freq's to track currentWindow occupants,
#   - while sliding check windowLen - maxFreq <= k
def characterReplacement(s,k):
  count = {}
  result = 0
  left = 0
  for right in range(len(s)):
    count[s[right]] = count.get(s[right],0) + 1
    while (right - left + 1) - max(count.values()) > k:
      count[s[left]] -= 1
      left += 1
    result = max(result, right - left + 1)
  return result

# MINIMUM WINDOW SUBSTRING:
# Given 2 strings s and t, return the minimum window substring of s such that every 
# character in t (including duplicates) is included in the window. 
# If there is no solution, return the empty string "".
# Approach:
#   - Use sliding window, tracking char maps of currWindow (s) in and needed (t)
#   - in O(n) pass, stretch and shrink window tracking matches and length
def minWindow(s,t):
  if len(t) == 0: return ""
  countT = {} # in t
  currWindow = {} # in s
  for c in t:
    countT[c] = countT.get(c,0) + 1
  have,need = 0,len(countT) # unique chars matched,needed
  result, resultLength = [-1,-1], float('infinity') # [l,r], length
  left = 0
  # SLIDING WINDOW
  for right in range(len(s)):
    c = s[right]
    currWindow[c] = currWindow.get(c,0) + 1

    # does new window now satisfy count?
    if c in countT and currWindow[c] == countT[c]:
      have += 1
    
    while have == need:
      # update result if needed
      if (right - left + 1) < resultLength:
        result = [left, right]
        resultLength = right - left + 1
      # shrink window from left -> popleft
      currWindow[s[left]] -= 1
      if s[left] in countT and currWindow[s[left]] < countT[s[left]]:
        have -= 1
      left += 1
  
  left,right = result
  return s[left:right+1] if resultLength != float("infinity") else ""

# LONGEST PALINDROMIC SUBSTRING:
# Given a string s, return the longest palindromic substring in s.
# Approach:
#   - O(n^2) solution: iterate thru the s for possible 'center' pos's of palindromes
#   - Expand outwards from center checking palindrome status and length
#   - Slight edge case for even-length strings
# NOTE:
#   - s[l:r+1] may be making a copy of s each iteration & degrading time to O(n^3)
def longestPalindromicSubstring(s):
  result = ""
  maxLength = 0
  # iterate thru potential center's
  for i in range(len(s)):
    # odd length palindrome (single start position)
    left, right = i,i
    # while valid palindrome
    while left >= 0 and right < len(s) and s[left] == s[right]:
      if (right - left + 1) > maxLength:
        result = s[left:right+1]
        maxLength = right - left + 1
      left -= 1
      right += 1

    # even length palindrome (double center position)
    left, right = i, i+1
    while left >= 0 and right < len(s) and s[left] == s[right]:
      if (right - left + 1) > maxLength:
        result = s[left:right+1]
        maxLength = right - left + 1
      left -= 1
      right += 1
  return result

# COUNT PALINDROMIC SUBSTRINGS:
# Given a string s, return the number of palindromic substrings in it.
# Approach:
#   - O(n^2)
#   - Similar to LongestPS, iterate through string for potential center position's
def countSubstrings(s):
  result = 0
  for i in range(len(s)):
    # odd length (single point center)
    left = right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
      result += 1
      left -= 1
      right += 1
    # even length
    left = i
    right = i + 1
    while left >= 0 and right < len(s) and s[left] == s[right]:
      result += 1
      left -= 1
      right += 1
  return result 

# ENCODE & DECODE STRINGS:
# Design an algorithm to encode a list of strings to a string. The encoded string 
# is then sent over the network and is decoded back to the original list of strings.
# Approach:
#   - An identifiable delimiter is crucial
#   - We can use something like: str([length of next string] + "#")
def encode(strs):
  result = ""
  for s in strs:
    result += str(len(s)) + "#" + s
  return result
def decode(str):
  result = []
  i = 0
  while i < len(str):
    # find delimiter
    j = i
    while str[j] != "#":
      j += 1
    length = int(str[i:j])
    result.append(str[(j + 1) : (j + 1 + length)])
    i = j + 1 + length
  return result


# COMPARE VERSION NUMBERS:
# Given two version numbers, version1 and version2, compare them.
# If v1 < v2, return -1, if v1 > v2, return 1. Otherwise, return 0.
# Eg: v1=7.5.2.4, v2=7.5.3 -> -1 | v1= 1.0.1,v2=1 -> 1 | v1=1.01, v2=1.001 -> 0 (ignore leading 0s)
def compareVersion(version1, version2):
  v1 = version1.split(".")
  v2 = version2.split(".")
  len1,len2 = len(v1),len(v2)

  for i in range(max(len1,len2)):
    n1 = 0 if  i>= len1 else int(v1[i])
    n2 = 0 if  i>= len2 else int(v2[i])

    if n1 > n2:
      return 1
    elif n1 < n2:
      return -1
  
  return 0

# LETTER COMBINATIONS OF A PHONE NUMBER:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.
def letterCombinations(digits):
  result = []
  digitToChar = {"2":"abc","3":"def","4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
  def dfs(i, curStr):
    if len(curStr) == len(digits):
      result.append(curStr)
      return
    for c in digitToChar[digits[i]]:
      dfs(i+i, curStr + c)
  
  if digits:
    dfs(o,"")
  
  return result