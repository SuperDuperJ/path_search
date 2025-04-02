from path_search import path_search_dfs

path_graph = {
    'A': set(['B']),
    'B': set(['A', 'C']),
    'C': set(['B', 'D']),
    'D': set(['C', 'E']),
    'E': set(['D'])
}

fork_graph = {
    'A': set(['B']),
    'B': set(['A', 'C']),
    'C': set(['B', 'D', 'F']),
    'D': set(['C', 'E']),
    'E': set(['D']),
    'F': set(['C'])
}

star_graph = {
    'A': set(['B', 'C', 'D', 'E', 'F', 'G']),
    'B': set(['A']),
    'C': set(['A']),
    'D': set(['A']),
    'E': set(['A']),
    'F': set(['A']),
    'G': set(['A']) 
}

G = {
    'A': set(['B']),
    'B': set(['A', 'C', 'F']),
    'C': set(['B', 'D', 'F']),
    'D': set(['F', 'C', 'E']),
    'E': set(['D']),
    'F': set(['B', 'C', 'D'])
}

H = {
    'A': set(['B', 'F']),
    'B': set(['A', 'G', 'C']),
    'C': set(['B', 'G', 'D']),
    'D': set(['C', 'G', 'E']),
    'E': set(['D', 'G', 'F']),
    'F': set(['E', 'G', 'A']),
    'G': set(['B', 'D', 'F'])
}

