def bellman_ford(vertices, edges, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            raise ValueError("Graf obsahuje záporný cyklus")

    return distance