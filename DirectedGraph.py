class DirectedGraph:
    def __init__(self):
       self.graph = {}
    def add_edge(self,v,e):
        self.graph.setdefault(v,[]).append(e)
    def display(self):
        for node,neighbors in self.graph.items():
            print(f"{node} ==> {neighbors}")


directedG =  DirectedGraph()
directedG.add_edge("Alice","Bo")
directedG.add_edge("Alice","Charlie")
directedG.add_edge("Bob","Charlie")

directedG.display()
