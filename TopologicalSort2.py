from collections import defaultdict

def topological_sort_dfs(prerequisites):
    graph = defaultdict(list)

    for key , values in prerequisites.items():
        if key not in graph:
            graph[key] = []
        for value in values:
            if value not in graph:
                graph[value] = []
            graph[value].append(key)
        
    
    
    visited = set()
    path_visited = set()
    result = []

    def dfs(node):

        if node in visited: return True

        if node in path_visited: return False

        path_visited.add(node)

        for nextNode in graph[node]:
            if not dfs(nextNode):
                return False
        
        path_visited.remove(node)
        visited.add(node)

        result.append(node)

        return True

    
    for parentNode in graph.keys():
        if parentNode not in visited:
            if not dfs(parentNode):
                return 'Cycle Detected'
    
    return result[::-1]


# Example: Software Package Dependencies
dependencies = {
    "Calculus I": [],
    "Calculus II": ["Calculus I"],
    "Physics I": ["Calculus I"],
    "Physics II": ["Physics I"],
    "Programming Basics": ["Calculus II"],
    "Data Structures": ["Programming Basics"],
    "Algorithms": ["Data Structures"],
    "Statistics": [],
    "Machine Learning": ["Algorithms", "Statistics"]
}

print("Topological Order of Software Components:")
order = topological_sort_dfs(dependencies)
for i, component in enumerate(order):
    print(f"{i+1}. {component}")