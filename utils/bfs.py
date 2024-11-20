from collections import deque



def bfs(graph,start):
    visited = set()
   
    queue = deque([start])
  
    while queue:
        node = queue.popleft()
        
        if node not in visited:
             print(node , end = " ")
             visited.add(node)
             queue.extend(graph[node])




def detect_cycle(graph, node, visited, stack):
     visited.add(node)
     stack.add(node)
     for neighbor in graph[node]:
        if neighbor not in visited:
            detect_cycle(graph,neighbor,visited,stack)
            return True
        elif neighbor in stack:
            return True
     stack.remove(node)
     return False

##bfs Tests
maze_graph = {
    "Start": ["A", "B"],
    "A": ["C"],
    "B": ["D"],
    "C": ["Finish"],
    "D": ["Finish"],
    "Finish": [],
}

bfs(maze_graph,"Start")

## cycle test
process_graph = {
    "P1": ["P2"],
    "P2": ["P3"],
    "P3": ["P1"],
}
visited = set()
stack = set()
has_cycle = detect_cycle(process_graph, "P1", visited, stack)
print("Cycle Detected:", has_cycle)
