# Program to find Bi-Connected Components in a graph

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BCCUtil(self, u, parent, disc, low, st):
        children = 0
        self.time += 1
        disc[u] = low[u] = self.time

        for v in self.graph[u]:
            if disc[v] == -1:
                parent[v] = u
                children += 1
                st.append((u, v))
                self.BCCUtil(v, parent, disc, low, st)
                low[u] = min(low[u], low[v])

                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                    bcc = []
                    while st[-1] != (u, v):
                        bcc.append(st.pop())
                    bcc.append(st.pop())
                    print("BCC:", bcc)

            elif v != parent[u] and disc[v] < disc[u]:
                low[u] = min(low[u], disc[v])
                st.append((u, v))

    def BCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.BCCUtil(i, parent, disc, low, st)

            if st:
                bcc = []
                while st:
                    bcc.append(st.pop())
                print("BCC:", bcc)


# -------- Main Program --------
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Bi-Connected Components in the given graph are:")
g.BCC()
