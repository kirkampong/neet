# ListNode
class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next

# REVERSE A LINKED LIST
# Given the head of a singly linked list, reverse the list, and return the reversed list.
def reverseList(self, head: ListNode) -> ListNode:
  prev, curr = None, head
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

# DETECT CYCLE IN A LINKED LIST:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
def hasCycle(self, head: ListNode) -> bool:
  slow, fast = head, head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          return True
  return False


# REMOVE Nth NODE FROM END OF LINKED LIST
# Given the head of a linked list, remove the nth node from the end and return its head.
# Approach:
#   - Use 2 pointers: place left at head and right n places after, then shift the two
#       until right pointer reaches the end, then delete left pointer's value
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
  dummy = ListNode(0, head)
  left = dummy
  right = head

  while n > 0:
    right = right.next
    n -= 1

  while right:
    left = left.next
    right = right.next

  # delete
  left.next = left.next.next
  return dummy.next

# REORDER LINKED LIST
# Given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln                  ... Reorder the list as follows:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …    ... Eg: In= [1,2,3,4] , Out: [1,4,2,3]
def reorderList(self, head: ListNode) -> None:
  # find middle
  slow, fast = head, head.next
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

  # reverse second half
  second = slow.next
  prev = slow.next = None
  while second:
      tmp = second.next
      second.next = prev
      prev = second
      second = tmp

  # merge two halfs
  first, second = head, prev
  while second:
      tmp1, tmp2 = first.next, second.next
      first.next = second
      second.next = tmp1
      first, second = tmp1, tmp2


# MERGE 2 SORTED LINKED LISTS
# Given the heads of two sorted linked lists list1 and list2,
# Merge the two lists in a one sorted list
def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
  dummy = ListNode()
  tail = dummy

  while list1 and list2:
    if list1.val < list2.val:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next
    tail = tail.next

  if list1:
    tail.next = list1
  elif list2:
    tail.next = list2

  return dummy.next
  
# MERGE K SORTED LINKED LISTS
# Merge an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Don't brute force O(k*n), use a mergeSort approach:
# Take pairs of linked lists at a time and merge them
def mergeKLists(self, lists):
  if not lists or len(lists) == 0:
      return None

  while len(lists) > 1:
      mergedLists = []
      for i in range(0, len(lists), 2):
          l1 = lists[i]
          l2 = lists[i + 1] if (i + 1) < len(lists) else None
          mergedLists.append(self.mergeTwoLists(l1, l2)) # see above for definition
      lists = mergedLists
  return lists[0]



