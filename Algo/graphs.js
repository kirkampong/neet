import './styles.css'


const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: []
};

const graph_p = {
  f: ["g", "i"],
  g: ["h"],
  h: [],
  i: ["g", "k"],
  j: ["i"],
  k: []
};

//====================== BASIC DAG ====================

const dfs = (graph, source) => {
  const stack = [source];
  while (stack.length > 0) {
    const curr = stack.pop();
    console.log(curr);
    for (let neighbour of graph[curr]) {
      stack.push(neighbour);
    }
  }
};

const bfs = (graph, source) => {
  const queue = [source];
  while (queue.length > 0) {
    const curr = queue.shift();
    console.log(curr);
    for (let neighbour of graph[curr]) {
      queue.push(neighbour);
    }
  }
};

const dfs_r = (graph, source) => {
  console.log(source);
  for (let neighbour of graph[source]) {
    dfs_r(graph, neighbour);
  }
};

const hasPath_dfs = (graph, src, dest) => {
  if (src === dest) {
    return true;
  }
  for (let neighbour of graph[src]) {
    if (hasPath_dfs(graph, neighbour, dest)) {
      return true;
    }
  }
  return false;
};

const hasPath_bfs = (graph, src, dest) => {
  const queue = [src];
  while (queue.length > 0) {
    const curr = queue.shift();
    if (curr === dest) {
      return true
    }
    for (let neighbour of graph[curr]) {
      queue.push(neighbour);
    }
  }
  return false;
};

// ==================== UNDIRECTED (CYCLIC) ====================
const edges= [
  ['i','j'],
  ['k','i'],
  ['m','k'],
  ['k','l'],
  ['o','n'],
]

const buildGraph = (edges) => {
  let graph = {}
  for( let edge of edges) {
    const[a, b] = edge
    if (!(a in graph)) graph[a] = []
    if (!(b in graph)) graph[b] = []
    graph[a].push(b)
    graph[b].push(a)
  }
  return graph
}

const undirectedHasPath_dfs = (graph, start, end) => {
  const graph_ = buildGraph(edges)
  return u_HasPath_dfs(graph_, start, end, new Set())
}

const u_HasPath_dfs = (graph, src, dest, visited) => {
  if(visited.has(src)) return false
  if(src === dest) return true
  visited.add(src)

  for(let neighbour of graph[src]){
    if(u_HasPath_dfs(graph,neighbour,dest)){
      return true
    }
  }
  return false
}

// =============== CONNECTED COMPONENTS =====================
const graph_c = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

const connectedComponentsCount_dfs = (graph) => {
  let visited = new Set()
  let count = 0
  for(let node in graph) {
    if(explore(graph,node,visited)){
      count += 1
    }
  }
  return count
}

const explore = (graph,currNode,visited) => {
  // JS quirk casts object keys as strings
  if(visited.has(String(currNode))) return false
  visited.add(String(currNode))
  for(let neighbour of graph[currNode]){
    explore(graph, neighbour,visited)
  }
  return true;
}

const largestComponent_dfs = (graph) => {
  let visited = new Set()
  let largest = 0
  for(let node in graph){
    const size = exploreSize(graph,node,visited)
    if(size > largest) largest = size
  }
  return largest
}

const exploreSize = (graph,currNode,visited) => {
  if(visited.has(currNode)) return 0;
  visited.add(currNode)
  let size = 1
  for(let neighbour of graph[currNode]){
    size += exploreSize(graph,neighbour,visited)
  }
  return size;
}

const count = connectedComponentsCount_dfs(graph_c); // -> 2

//============== shortestPath ===================
const edges_sp = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];

const shortestPath_bfs_undirected = (edges,src,dest) => {
  const graph_sp = buildGraph(edges_sp)
  const visited = new Set([src])
  const queue = [[src,0]]
  while(queue.length > 0) {
    const [currNode, distance] = queue.shift()
    if(currNode === dest) return distance
    for(let neighbour of graph[currNode]){
      if(!visited.has(neighbour)){
        visited.add(neighbour)
        queue.push([neighbour,distance+1])
      } 
    }
  }
  return -1 // NO PATH
}

//================ GRID GRAPHS ===================

// island count
const grid_island = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

// alt: python bfs : https://github.com/neetcode-gh/leetcode/blob/main/python/200-Number-of-Islands.py
const islandCount = (grid) => {
  let count = 0
  const visited = new Set()
  for(let r = 0; r < grid.length; r+=1){
    for(let c = 0; c < grid[0].length; c+=1){
      if(exploreIsland(grid,r,c,visited)) count += 1
    }
  }
  return count
}

const exploreIsland = (grid,r,c,visited) => {
  const rowInbounds = 0 < r && r < grid.length
  const colInbounds = 0 < c && c < grid[0].length
  if(!rowInbounds || !colInbounds) return false

  if(grid[r][c] === 'W') return false

  const pos = r +',' + c // Set() can only lookup primitives(String)
  if(visited.has(pos)) return false
  visited.add(pos)

  //traverse on unvisited land
  exploreIsland(grid,r-1,c,visited)
  exploreIsland(grid,r+1,c,visited)
  exploreIsland(grid,r,c-1,visited)
  exploreIsland(grid,r,c+1,visited)

  return true
}

// minimum island
const minimumIsland = (grid) => {
  let minSize = Infinity
  const visited = new Set()
  for(let r = 0; r < grid.length; r+=1){
    for(let c = 0; c < grid[0].length; c+=1){
      const size = exploreMinSize(grid,r,c,visited)
      if(size > 0 && size < minSize) minSize = size
    }
  }
  return count
}

const exploreMinSize = (grid,r,c,visited)=> {
  const rowInbounds = 0 < r && r < grid.length
  const colInbounds = 0 < c && c < grid[0].length
  if(!rowInbounds || !colInbounds) return 0

  const pos = r +',' + c // Set() can only lookup primitives(String)
  if(visited.has(pos)) return false
  visited.add(pos)

  //traverse on unvisited land
  let size = 1
  size += exploreMinSize(grid,r-1,c,visited)
  size += exploreMinSize(grid,r+1,c,visited)
  size += exploreMinSize(grid,r,c-1,visited)
  size += exploreMinSize(grid,r,c+1,visited)

  return size
}



export default function App() {
  //bfs(graph, "a");
  const ans = hasPath_bfs(graph_p, "f", "k");
  return (
    <div className="App">
      <h2>Graphs</h2>
      {ans && <h4>PATH</h4>}
    </div>
  );
}