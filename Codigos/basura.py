import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#nodos por listas
nodes = ["aasdf","basdf","caaaaaaaaaaaaaasdfvdsxc bfdsxcfd","d"]
G.add_nodes_from(nodes)

#nodos por item
G.add_node("e")

G.add_nodes_from(["f", "g", "h"])

#eliminar el nodo g
G.remove_node("g")

nx.draw_shell(G, with_labels=True)


plt.show()
