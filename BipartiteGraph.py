class BipartiteGraph:
    def __init__(self):
        self.graph = {}
    def add_edge(self,worker,job):
        self.graph.setdefault(worker,[]).append(job)
    def display(self):
        for worker, jobs in self.graph.items():
            print(f"{worker} ==> {jobs}")





bg = BipartiteGraph()
bg.add_edge("w1","JobA")
bg.add_edge("w1", "JobB")
bg.add_edge("w2","JobA")

bg.display()