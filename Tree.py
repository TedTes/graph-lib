class Tree:
    def __init__(self):
       self.tree = {}
    def add_relationship(self,parent,child):
         self.tree.setdefault(parent,[]).append(child)
        
    def display(self):
        for parent , children in self.tree.items():
            print(f"{parent} ==> {children}")


t = Tree()

t.add_relationship("parent","child1")
t.add_relationship("parent","child2")

t.display()
