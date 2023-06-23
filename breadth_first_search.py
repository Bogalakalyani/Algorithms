graph = {
    '60' : ['20','70'],
    '20' : ['30'],
    '70' : ['80'],
    '30' : ['40'],
    '80' : [],
    '40' : ['50'],
    '50' : []

}
visited = []
queue = []

def bfs(graph,visited,node):
    visited.append(node)
    queue.append(node)   

    while queue:
        value = queue.pop(0)
        print(value,end = " ")
        for next in graph[value]:
            if next not in visited:
                visited.append(next)
                queue.append(next)



bfs(graph,visited,'60')

