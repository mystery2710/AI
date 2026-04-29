# Graph Coloring — Backtracking + B&B

def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(node, num_colors, assignment, graph, nodes):
    if len(assignment) == len(nodes):
        return True

    for color in range(1, num_colors + 1):
        if is_safe(node, color, assignment, graph):
            assignment[node] = color

            next_nodes = [n for n in nodes if n not in assignment]
            if not next_nodes:
                return True

            if backtrack(next_nodes[0], num_colors, assignment, graph, nodes):
                return True

            del assignment[node]

    return False

def solve_graph_coloring(graph, num_colors, nodes):
    assignment = {}
    if backtrack(nodes[0], num_colors, assignment, graph, nodes):
        return assignment
    return None

def print_solution(assignment, num_colors):
    color_names = ["", "Red", "Green", "Blue", "Yellow",
                   "Orange", "Purple", "Pink", "Cyan"]
    print("\n Graph Coloring Solution:")
    print("-" * 30)
    for node, color in sorted(assignment.items()):
        name = color_names[color] if color < len(color_names) else f"Color-{color}"
        print(f"  Node {node:>3}  →  {name} (Color {color})")
    print("-" * 30)
    print(f"  Colors used : {num_colors}")
    print(f"  Nodes colored: {len(assignment)}\n")

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    e = int(input("Enter number of edges: "))

    graph = {i: [] for i in range(1, n + 1)}
    nodes = list(range(1, n + 1))

    for i in range(e):
        u, v = map(int, input(f"Edge {i+1}: ").split())
        graph[u].append(v)
        graph[v].append(u)

    k = int(input("Enter number of colors: "))
    result = solve_graph_coloring(graph, k, nodes)

    if result:
        print_solution(result, k)
    else:
        print("No valid coloring found.")
