graph = { 1 : [2,3] ,
        2 : [1,4,5],
        3 : [1,5],
        4 :[2,6,5],
        5 :[2,3,4,6],
        6 : [4,5]}


def dfs(graph,start,stack):

    adjNode = graph[start]
    
    

    if stack is None:
        stack = []
        stack.append(start)
    else:
        stack.append(start)

    for node in adjNode:
        if node not in stack:
            dfs(graph,node,stack)  
    
    print(stack)  

def bfs(graph,start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)
    top = 0
    

    
    print(start)

    while queue:
        adjNode = graph[queue[top]]
        for node in  adjNode:
            if node not in visited:
                queue.append(node)
                visited.append(node)
                print(node)
               
        del queue[top]
