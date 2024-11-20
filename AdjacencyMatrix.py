import numpy as np 

class AdjacencyMatrix:
    def __init__(self,size):
        self.matrix = np.zeros((size,size),dtype=int)
    
    def add_edge(self,u,v,weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def display(self):
        print(self.matrix)




am = AdjacencyMatrix(4)

am.add_edge(0,1,2)
am.add_edge(3,2,4)
am.add_edge(0,3,8)

am.display()