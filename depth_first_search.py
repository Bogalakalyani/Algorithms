graph = {
    '60': ['20', '70'],
    '20': ['30'],
    '70': ['80'],
    '30': ['40'],
    '80': [],
    '40': ['50'],
    '50': []
}

visited1 = []
stack1 = []


def dfs(graph, visited, node):
    visited.append(node)
    stack1.append(node)   

    while stack1:
        value = stack1.pop()
        print(value,end = " ")
        for next in graph[value]:
            if next not in visited:
                visited.append(next)
                stack1.append(next)

# with rescursion

visited2 = []


def DFS(graph,visited,node):
    if node not in visited:
        print(node,end= " ")
        visited2.append(node)
        for i in graph[node]:
            DFS(graph,visited,i)   


dfs(graph, visited1, '60')
print()
DFS(graph,visited2,'60')
