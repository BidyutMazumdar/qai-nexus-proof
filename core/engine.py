class Node:
    def __init__(self, E, C, L):
        self.E = E
        self.C = C
        self.L = L

def sync(nodes):
    return sum(n.E * n.C * n.L for n in nodes)
