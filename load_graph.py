def load_graph_from_file(filename):
    edges = []
    vertices = set()

    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                u, v, w = line.strip().split()
                w = int(w)
                edges.append((u, v, w))
                vertices.update([u, v])

    return sorted(vertices), edges