import "./styles.css";

// Setup

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

const dfsValues = (root) => {
  if (root === null) return [];
  const result = [];
  const stack = [root];
  while (stack.length > 0) {
    const currNode = stack.pop();
    result.push(currNode.val);
    // prints right side first
    if (currNode.right) stack.push(currNode.right);
    if (currNode.left) stack.push(currNode.left);
  }
  return result;
};

const dfsValues_r = (root) => {
  if (root === null) return [];
  const leftValues = dfsValues_r(root.left);
  const rightValues = dfsValues(root.right);
  return [root.val, ...leftValues, ...rightValues];
};

const bfsValues = (root) => {
  if (root === null) return [];
  const result = [];
  const queue = [root];
  while (queue.length > 0) {
    const currNode = queue.shift();
    result.push(currNode.val);
    if (currNode.left) queue.push(currNode.left);
    if (currNode.right) queue.push(currNode.right);
  }
  return result;
};

const treeIncludes_bfs = (root, target) => {
  if (root === null) return false;
  const queue = [root];
  while (queue.length > 0) {
    const currNode = queue.shift();
    if (currNode.val === target) return true;
    if (currNode.left) queue.push(currNode.left);
    if (currNode.right) queue.push(currNode.right);
  }
  return false;
};

const treeIncludes_dfs_r = (root, target) => {
  if (root === null) return false;
  if (root.val === target) return true;
  return (
    treeIncludes_dfs_r(root.left, target) ||
    treeIncludes_dfs_r(root.right, target)
  );
};

const treeSum = (root) => {
  if (root === null) return 0;
  return root.val + treeSum(root.left) + treeSum(root.right);
};

const treeMinValue_dfs_r = (root) => {
  if (root === null) return Number.POSITIVE_INFINITY;
  const leftMin = treeMinValue_dfs_r(root.left);
  const rightMin = treeMinValue_dfs_r(root.right);
  return Math.min(root.val, leftMin, rightMin);
};

const treeMinValue_dfs = (root) => {
  let minValue = Number.POSITIVE_INFINITY;
  const stack = [root];
  while (stack.length > 0) {
    const currNode = stack.pop();
    if (currNode.val < minValue) minValue = currNode.val;
    if (currNode.right) stack.push(currNode.right);
    if (currNode.left) stack.push(currNode.left);
  }
  return minValue;
};

const treeMinValue_bfs = (root) => {
  let minValue = Number.POSITIVE_INFINITY;
  const queue = [root];
  while (queue.length > 0) {
    const currNode = queue.shift();
    if (currNode.val < minValue) minValue = currNode.val;
    if (currNode.right) queue.push(currNode.right);
    if (currNode.left) queue.push(currNode.left);
  }
  return minValue;
};

const maxRootToLeafPathSum = (root) => {
  // base case
  if (root === null) return -Infinity;
  if (root.left === null && root.right === null) return root.val;

  const maxChildPathSum = Math.max(
    maxRootToLeafPathSum(root.left),
    maxRootToLeafPathSum(root.right)
  );
  return root.val + maxChildPathSum;
};

export default function App() {
  console.log(treeIncludes_dfs_r(a, "b"));
  return (
    <div className="App">
      <h2>Trees</h2>
    </div>
  );
}
