# B-TREE ALGOS : https://docs.google.com/document/d/1oRIgLia-ql64gUyh1J8ExcXq-MmEokKdMsmkknFJoSI/edit

'''
# SWAP NODES:
https://www.hackerrank.com/challenges/swap-nodes-algo/problem
Search & Insertion:
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
Insert into BST:
https://www.hackerrank.com/challenges/binary-search-tree-insertion/forum
Print All root to leaf paths in BST:
https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
Sorted Array to BST:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35224/Python-optimal-solution
Trie impl - search and insert:
https://www.geeksforgeeks.org/trie-insert-and-search/
'''


import collections
class Node:
   def __init__(self, data=0,left=None,right=None):
      self.left = left
      self.right = right
      self.data = data

  #Insert Node
   def insert(self, data):
      if self.data:
        if data < self.data:
          if self.left is None:
             self.left = Node(data)
          else:
            self.left.insert(data)
        elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data

root = Node(27), root.insert(14), root.insert(35), root.insert(10)
root.insert(19), root.insert(31), root.insert(42), print(root.inOrderTraversal(root)) 

# ===========================================================================

# TREE MAX DEPTH:
# iterative: Iterative:https://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/?ref=lbp
def maxDepth(node):
   if node is None:
      return -1 ; 
   else :
      lDepth = maxDepth(node.left)
      rDepth = maxDepth(node.right)
      if (lDepth > rDepth):
         return lDepth+1
      else:
         return rDepth+1

# INORDER & PREORDER TRAVERSAL: 
# Left -> Root -> Right
def inOrderTraversal(self, root):
   res = []
   if root:
      res = self.inOrderTraversal(root.left)
      res.append(root.data)
      res = res + self.inOrderTraversal(root.right)
      '''PRE-ORDER:
      res.append(root.data)
      res = res + inOrderTraversal(root.left)
      res = res + inOrderTraversal(root.right)
      '''
   return res

# VALIDATE BST:
def validateBST(node):
   return (validateBSTUtil(node, INT_MIN, INT_MAX))
def validateBSTUtil(node, mini, maxi):      
   # An empty tree is BST
   if node is None:
      return True
   if node.data < mini or node.data > maxi:
      return False
   return (validateBSTUtil(node.left, mini, node.data -1) and
            validateBSTUtil(node.right, node.data+1, maxi))

# ===========================================================================

# SAME TREE:
# Given 2 b-trees p and q, check if they are the same or not
def isSameTree(tree1, tree2):
  if not tree1 and not tree2:
    return True
  if not tree1 or not tree2:
    return False
  if tree1.val != tree2.val:
    return False
  return isSameTree(tree1.left, tree2.left) and \
    isSameTree(tree1.right, tree2.right)

# INVERT BINARY TREE:
# Given the root of a binary tree, invert the tree horizontally, and return its root.
def invertTree(root):
  if not root:
    return None
  # swap children
  tmp = root.left
  root.left = root.right
  root.right = tmp

  invertTree(root.left)
  invertTree(root.right)

# B-TREE LEVEL ORDER TRAVERSAL
# Given the root of a binary tree, return its level order traversal
# Approach: BFS
def levelOrder(root):
   result = []
   q = collections.deque()
   q.append(root)
   while q:
      level = []
      for i in range(len(q)):
         node = q.popleft()
         if node:
            level.append(node.val)
            q.append(node.left)
            q.append(node.right)
   if len(level) > 0:
      result.append(level)
   return result

# SERIALIZE/DE-SERIALIZE BINARY TREE
# Design an algorithm to serialize and deserialize a binary tree
# Approach:
#  -  Serialize to str using a dfs preorder, use 'N' for null child
#  -  Deserialize: split by delimiter(,) first elem is root.
#  =  Recursively create left and right subtree
def serializeTree(root):
  # preorder dfs
  result = []
  def dfs(node):
    if not node:
      result.append("N")
      return
    result.append(str(node.val))
    dfs(node.left)
    dfs(node.right)
  dfs(root)
  return ",".join(result)

def deserializeTree(data):
  values = data.split(",")
  ptr = 0
  def dfs():
    if values[ptr] == "N":
      ptr += 1
      return None
    n = Node(int(values[ptr]))
    ptr += 1
    n.left = dfs()
    n.right = dfs()
    return n
  
  return dfs()

# SUBTREE OF ANOTHER TREE:
# Given the roots of two binary trees root and subRoot, return true if there is a 
# subtree of root with the same structure and node values of subRoot.
# Approach - BruteForce - O(N1*N2):
#  -  Traverse main tree(root), 
#  -  At each node, recursively check for total subtree matches from subRoot->l->r
def isSubtree(root, subRoot):
  # if subtree is empty return true
  if not subRoot: return True
  if not root: return False # already checked subRoot
  if sameTree(root,subRoot):
    return True
  
  return (isSubtree(root.left, subRoot) \
          or isSubtree(root.right, subRoot))

def sameTree(tree1, tree2):
  if not tree1 and not tree2:
    return True
  if tree1 and tree2 and tree1.val == tree2.val:
    return (sameTree(tree1.left, tree2.left) and \
            sameTree(tree1.right, tree2.right))
  return False

# BINARY TREE FROM PREORDER & INORDER TRAVERSAL:
# Construct Binary Tree from 2 Arrays: Preorder and Inorder Traversal
# Approach:
#    - Recursive approach: first elem in pre-order is root. Then check in-order arr:
#    - In-order Array: All nodes to left of first elem go to left, and vice versa
#    - Repeat for remaining part of array(pre)
def buildTree(preorder, inorder):
  if not preorder or not inorder:
    return None

  root = Node(preorder[0])
  mid = inorder.index(preorder[0])
  root.left = buildTree(preorder[1:mid+1], inorder[:mid])
  root.right = buildTree(preorder[mid+1:],inorder[mid+1:])
  return root

# KTH SMALLEST ELEMENT IN BST:
# Given the root of a bst, and an int k, return the kth smallest value (1-indexed) 
# of all the values of the nodes in the tree.
# Approach:
#  -  If we traverse a bst IN-ORDER we will get a SORTED array, find kth smallest
#
# {ITERATIVE SOLUTION}
def kthSmallest(root,k):
  numNodesVisited = 0 
  stack = []
  currNode = root
  while currNode and stack:
    while currNode:
      stack.append(currNode)
      currNode = currNode.left
    # process currNode
    currNode = stack.pop()
    numNodesVisited += 1
    if numNodesVisited == k:
      return currNode.val
    # check right
    currNode = currNode.right
# RECURSIVE : <<<<<<<<<<<<>>>>>>>>>>>>
def kthSmallestRecursive(root, k):
   nodes = []
   solve(root,nodes)
   return nodes[k-1]
def solve(self, root,nodes):
   if root == None:
      return
   solve(root.left,nodes)
   nodes.append(root.data)
   solve(root.right,nodes)


# LOWEST COMMON ANCESTOR OF BST:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST.
# Approach O(log n):
#  - Given nodes p and q starting at root, check if they are both less than val
#  - If both lower than currVal, go left else right
def lowestCommoneAncestor(root,p,q):
  currNode = root
  while currNode: #infinite loop
    if p.val > currNode.val and q.val > currNode.val:
      currNode = currNode.right
    elif p.val < currNode.val and q.val < currNode.val:
      currNode = currNode.left
    # split occurs or we find result
    else:
      return currNode

# IMPLEMENT TRIE (Prefix Tree):
# Implement the Trie class: (only consider lowercase words):
#  - Trie() Initializes the trie object.
#  - Insert(String word) Inserts the string word into the trie.
#  - Search(String word) Returns true if word is in trie else false.
#  - StartsWith(String prefix) Returns true if trie contains a word with the prefix.
# Approach:
#  - Insert a word by adding all chars to trie, marking the end of each word
class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False
    #eg children['a'] = TrieNode

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self,word):
    currNode = self.root
    for ch in word:
      if ch not in currNode.children:
        currNode.children[ch] = TrieNode()
      currNode = currNode.children[ch]
  
  def search(self,word):
    currNode = self.root
    for ch in word:
      if ch not in currNode.children:
        return False
      currNode = currNode.children[ch]
    return currNode.endOfWord
  
  def startsWith(self,prefix):
    currNode = self.root
    for ch in prefix:
      if ch not in currNode.children:
        return False
      currNode = currNode.children[ch]
    return True


# DESIGN ADD AND SEARCH WORDS DATA STRUCTURE:
# Design a data structure that supports adding new words and finding 
# if a string matches any previously added string.
# Implement the WordDictionary class:
#  - WordDictionary() Initializes the object.
#  - AddWord(word) Adds word to the data structure, it can be matched later.
#  - Search(word) Returns true if we have a string matching the word else false.
#  - (Word may contain dots '.' where dots can be matched with any letter.)
# Approach:
#  - Use a TRIE!
class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    currNode = self.root
    for ch in word:
      if ch not in currNode.children:
        currNode.children[ch] = TrieNode()
      currNode = currNode.children[ch]
    currNode.endOfWord = True
        
  def search(self, word):
    def dfs(idx, node):
      currNode = node
      for i in range(idx, len(word)):
        ch = word[i]
        if ch == '.':
          # recursive backtracking, not following 26 paths!
          for child in currNode.children.values():
            if dfs(i+1, child):
              return True
          return False
        else:
          if ch in currNode.children:
            return False
          currNode = currNode.children[ch]
      return currNode.endOfWord
    
    dfs(0,self.root)


# WORD SEARCH II (Prefix Tree)
# Given an m x n board of characters and a list of strings words, return 
# all words on the board.
# Approach:
#  - Its mad inefficient to start a dfs from each pos for each word we want one pass(m*n)
#  - We'll check all words simultaneously as we go through the grid
#  - We'll create a TRIE DS to store our words so we don't have to keep checking the entire list
'''
   NOTE: Use 'TrieNode' constructor and 'addWord' method defined above
'''
def findWords(board,words):
  root = TrieNode()
  for word in words:
    root.addWord(word)
  numRows,numCols = len(board), len(board[0])
  result,visited = set(), set()

  def dfs(row,col,node,word):
    if (row<0 or col<0 or 
        row == numRows or col == numCols or
        (row,col) in visited or 
        board[row][col] not in node.children):
        return

    visited.add((row,col))
    node = node.children[board[row][col]]
    word += board[row][col]
    if node.endOfWord:
      result.add(word)

    dfs(row + 1, col, node, word)
    dfs(row - 1, col, node, word)
    dfs(row, col + 1, node, word)
    dfs(row, col - 1, node, word)
    visited.remove((row,col)) # backtrack
  
  for row in range(numRows):
    for col in range(numCols):
      dfs(row,col,root,"")
  
  return list(result)