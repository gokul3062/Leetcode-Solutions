from collections import defaultdict, deque

def topological_sort_kahn(prerequisites):

    dependentCount = defaultdict(int)
    graph = defaultdict(list)

    for courses in prerequisites:
        if not courses in dependentCount:
            dependentCount[courses] = 0
        
        for dependent in prerequisites[courses]:
            graph[dependent].append(courses)
            dependentCount[courses] += 1
            if not dependent in dependentCount:
                dependentCount[courses] = 0
        
    queue = deque([course for course ,count in dependentCount.items() if count == 0])

    if not queue:
        return 'CYCLE'

    res = []

    while queue:
        course = queue.popleft()
        res.append(course)

        for c in graph[course]:
            dependentCount[c] -= 1
            if dependentCount[c] == 0:
                queue.append(c)
            
    return res


# Example: Course Prerequisites
prerequisites = {
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

print("Topological Order of Courses:")
order = topological_sort_kahn(prerequisites)
for i, course in enumerate(order):
    print(f"{i+1}. {course}")