# CONVERT INT TO BINARY:
binary = bin(19)
print(binary)
print("{0:08b}".format(19)) # => full binary output 8 places
print("{0:016b}".format(19)) # => full binary output 16 places

# NUMBER OF 1 BITS:
# Given an unsigned integer(32-bit) return the number of '1' bits it has (Hamming weight).
# eg: Input: n = 00000000000000000000000000001011 -> ans: 3
# Approach:
#   - Brute: manually count all bits, mod with 2 to count 0/1
#   - Bit-shift(equivalent to integer division by 2 [//2]
#   = Repeatedly bit-shift right by 1, mod by 2 to check if rightmost is 0/1
def hammingWeight(num):
  result = 0
  while num: #(num > 0)
    result += num % 2 # if rightmost 1 increment result
    num = num >> 1  # in while loop we can do (n&=(n-1);res+=1) instead
  return result

# MISSING NUMBER:
# Given an array of n distinct numbers in the range [0,n] find the missing number
# eg [3,0,1] | ans: 2
# Approach:
#   - if we can use O(n) space we can simply use a hashSet
#   - We can use expected sum for a O(1) space solution
#   - for O(1) space, we can use XOR. Remember any [num^num = 0, num^0 = num]
#   - if we do XOR [0..n] ^ [inputArr] we'll get the missing number
def missingNumberXOR(nums):
  res = len(nums)
  for i in range(len(nums)):
    res ^= i ^ nums[i]
  return res
def missingNumberSum(nums):
  res = len(nums)
  for i in range(len(nums)):
    res += (i-nums[i])
  return res

# REVERSE BITS:
# Reverse bits of a given 32 bits unsigned integer.
def reverseBits(n):
  res = 0
  for i in range(32):
    bit = (n >> i) & 1 # extract last bit?
    res | (bit << (31-i))  # res | bit updates only 1s place
  return res

# COUNTING BITS:
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.
def countBirs(n):
  ans = [0]*(n+1)
  offset = 1 #current power of 2
  for i in range(1, n+1):
    if offset * 2 == i:
      offset = i
    ans[i] = 1 + ans[i-offset]
  return ans

# SUM OF 2 INTEGERS:
# Given two integers, return the sum without using the operators + and -.
def getSum(self, a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    mask = 0xffffffff
    # in Python, every integer is associated with its two's complement and its sign.
    # However, doing bit operation "& mask" loses the track of sign. 
    # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask # must be one-liner else use tmp

    # a is negative if the first bit is 1
    if (a >> 31) & 1:
        return ~(a ^ mask)
    else:
        return a

