from collections import deque

# path_search_dfs is a modification of the standard recursive depth-first path search
# algorithm (given below) that returns the visited list if a path is found.
# Since this visited list may or may not explicitly give the path, path_search_dfs 
# is stronger than the standard recursive dfs path search algorithm.
# If at least one path exists, path_search_dfs will find one path, though this path
# may not be the shortest path.
# The output of path_search_dfs is of the form: visited, path.  
# If no path exists, the output will be None, path where path will be nonsense.  
def path_search_dfs(graph, current_vertex, target_value, visited = None, walk = None):
    if visited is None:
        visited = []
	
    if walk is None:
        walk = []

    visited.append(current_vertex)
    walk.append(current_vertex)
  
    if current_vertex == target_value:
        return visited, walk
        
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            X, Y = path_search_dfs(graph, neighbor, target_value, visited, walk)
            if X:
                return X, Y
            else:
                Y.pop()
    return None, walk 

# This is the standard recursive depth-first path search algorithm that may or may
# not actually return a path in the graph.
def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
	
    visited.append(current_vertex)
  
    if current_vertex == target_value:
        return visited
        
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            walk = dfs(graph, neighbor, target_value, visited)
            if walk:
                return walk

# path_search_bfs is the standard breadth-first path search that returns a shortest path
# provided such a path exists.
def path_search_bfs(graph, start, target):
    if start == target:
        return [start]
    visited = set()
    queue = deque()
    queue.appendleft([start,[start]])

    while queue:
        current, path = queue.pop()
        visited.add(current)
        for neighbor in (graph[current] - visited):
            if neighbor == target:
                return path + [neighbor]
            else:
                queue.appendleft([neighbor, path + [neighbor]])
    return None