class WeightedGraph:
    def __init__(self):
        self.graph = {}
    def add_edge(self,v,e,weight):
        self.graph.setdefault(v,[]).append((e,weight))
        self.graph.setdefault(e,[]).append((v,weight))
    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node} ==> {neighbors}")



w = WeightedGraph()
w.add_edge("Alice","Bob",4)
w.add_edge("Alice","charlie",40)
w.add_edge("john","cb",14)
w.add_edge("x","y",14)

w.display()