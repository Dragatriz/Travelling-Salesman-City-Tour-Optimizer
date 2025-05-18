def greedy_tour(dist, start):
    n = len(dist)
    visited = [False] * n
    path = [start]
    visited[start] = True
    for _ in range(n - 1):
        last = path[-1]
        next_city = min((i for i in range(n) if not visited[i]), key=lambda i: dist[last][i])
        path.append(next_city)
        visited[next_city] = True
    return path

def two_opt(route, dist):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                if dist[route[i - 1]][route[j - 1]] + dist[route[i]][route[j % len(route)]] < \
                   dist[route[i - 1]][route[i]] + dist[route[j - 1]][route[j % len(route)]]:
                    route[i:j] = reversed(route[i:j])
                    improved = True
    return route