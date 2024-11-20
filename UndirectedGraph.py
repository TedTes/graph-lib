class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v,u):
        self.graph.setdefault(v,[]).append(u)
        self.graph.setdefault(u,[]).append(v)

    def display(self):
        for node,neighbors in self.graph.items():
            print(f"{node} ==> {neighbors}")


g = UndirectedGraph()

g.add_edge("Alice","Bo")
g.add_edge("Alice","Charlie")
g.add_edge("Bob","Charlie")

g.display()
