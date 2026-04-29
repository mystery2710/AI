class Graph:
    def __init__(self, vertices):
        self.V = vertices      
        self.edges = []         

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  
        return parent[i]

    def union(self, parent, rank, x, y):
        rx, ry = self.find(parent, x), self.find(parent, y)
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1

    def kruskal_mst(self):

        self.edges.sort()

        parent = list(range(self.V))   
        rank   = [0] * self.V
        mst    = []                    
        total  = 0

        print("\nProcessing edges (Greedy: smallest first):\n")

        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                self.union(parent, rank, root_u, root_v)
                mst.append((u, v, weight))
                total += weight
                print(f"Added edge {u}--{v}  (weight={weight})")
            else:
                print(f"Skipped edge {u}--{v} (weight={weight}) → would form a cycle")

            if len(mst) == self.V - 1:  
                break

        print("\nMinimum Spanning Tree:\n")
        print(f"  {'Edge':<12} {'Weight':>6}")
        print(f"  {'-'*20}")
        for u, v, w in mst:
            print(f"  {u} -- {v}     {w:>6}")
        print(f"  {'-'*20}")
        print(f"  Total MST weight: {total}\n")
        return mst, total


if __name__ == "__main__":
    print("=== Kruskal's Minimum Spanning Tree ===\n")

    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    g = Graph(V)

    print(f"\nEnter each edge as: u v weight  (vertices are 0 to {V-1})")
    for i in range(E):
        u, v, w = map(int, input(f"  Edge {i+1}: ").split())
        g.add_edge(u, v, w)

    g.kruskal_mst()
