class DynamicGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        self.graph.setdefault(u,[]).append((v,weight))
    
    def update_weight(self,u,v,new_weight):
          for i , (neighbor,weight) in enumerate(self.graph[u]):
               if neighbor == v:
                    self.graph[u][i] = (v,new_weight)
    def display(self):
         for node, neighbors in self.graph.items():
              print(f"{node} ==> {neighbors}")


dg = DynamicGraph()
dg.add_edge("A","B",4)
dg.display()
dg.update_weight("A","B",10)
dg.display()
