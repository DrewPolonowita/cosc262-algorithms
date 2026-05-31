from cosc262 import *



acyclic_graph = [
    [(1,None), (2,None)],
    [(2,None)],
    []
]
print(is_acyclic(acyclic_graph))

cyclic_graph = [
    [(1,None)],
    [(2,None)],
    [(0,None)]
]

print(is_acyclic(cyclic_graph))