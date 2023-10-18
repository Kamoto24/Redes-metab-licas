import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#nodos por listas
nodes = ["a","b","c","d"]
G.add_nodes_from(nodes)

#nodos por item
G.add_node("e")

G.add_nodes_from(["f", "g", "h"])

#eliminar el nodo g
G.remove_node("g")

#nx.draw_shell(G, with_labels=True)

#unir grafos
#grafo camino
H = nx.path_graph(3)
H.add_nodes_from(G)

#nx.draw_shell(H, with_labels=True)


#aristas
G.add_edge("a", "b")

e = ("b", "c")
G.add_edge(*e)

G.add_edges_from([("f","g"), ("f","f"), ("a","f")])

#limpiar grafo
#G.clear()

#nx.draw_shell(G, with_labels=True)

#numero de nodos y aristas
print(f"Numero de nodos: {G.number_of_nodes()}\nNumero de aristas: {G.number_of_edges()}")
#vecinos de a
print(f'vecino: {list(G.adj["f"])}')
#numero de aristas incidentes en a
print(f'numero de aristas incidentes en a: {G.degree["a"]}')



#digrafo
DG = nx.DiGraph()
DG.add_edge("b", "a")
DG.add_edge("a", "c")
DG.add_edge("b", "d")
DG.add_edge("a", "c")
DG.add_edge("a", "d")

#los nodos a los que sale a
print(f'sucesores: {list(DG.successors("a"))}')
#aristas y numero de incidencia
print(G.degree(["a","f"]))



#imprimir las aristas (al ser dirigido, importa el orden)
print(f'aristas con orden: {list(DG.edges)}')

nx.draw_shell(DG, with_labels=True)


plt.show()