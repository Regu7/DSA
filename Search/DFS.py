def dfs(graph, node):
    visited = set()  # Using a set for O(1) lookup
    stack = [node]   # Using list instead of deque

    while stack:
        s = stack.pop()
        if s not in visited:
            print(s, end=" ")
            visited.add(s)  # Mark as visited
            stack.extend(reversed(graph[s]))  # Add neighbors to stack

# Example usage
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

dfs(graph, 'A')
