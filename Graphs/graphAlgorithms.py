# The default start node for the algorithms is node 0


# Depth First Search >> explore a graph

def Dfs(edges):
    n_nodes = len(edges)
    visited = [False for _ in edges]
    path = []

    def recursiveDFS(current): # at is the current node
        path.append(current)
        if visited[current]: return
        else:
            visited[current] = True
            current_connects = edges[current]
            current_neighbs = [index for index, value in enumerate(current_connects) if value == 1]
            for at in current_neighbs: recursiveDFS(at)

    start_node = 0
    recursiveDFS(start_node)
    return path


# Breadth First Search >> find the minimum path

def Bfs(edges, end_node, start_node = 0):

    def bfs(start, end):
        queue = []
        queue.append(start)
        visited = [False for _ in edges]
        visited[start] = True
        fathers = [None for _ in edges]
        while len(queue) > 0:
            node = queue.pop(0)
            neighbs = [i for i, v in enumerate(edges[node]) if v == 1]
            for nb in neighbs:
                if not visited[nb]:
                    queue.append(nb)
                    visited[nb] = True
                    fathers[nb] = node
        return fathers


    def reconstructPath(start, end, fathers):
        path = []
        curr_nod = end
        while curr_nod != None:
            path.append(curr_nod)
            curr_nod = fathers[curr_nod]
        path.reverse()
        return path

    fathers = bfs(start_node, end_node)
    return reconstructPath(start_node, end_node, fathers)

print Bfs([[0,1,0,1,1,0], [1,0,1,1,0,0], [0,1,0,0,1,0], [1,1,0,0,0,1], [0,1,1,0,0,0], [0,0,0,1,0,0]], 5)
































