import networkx as nx
import matplotlib.pyplot as plt
import csv

#FUNCIONES:
def find_in_list(target, py_list):
  #busca el indice de un elemento
  for i in range(len(py_list)):
    if py_list[i] == target:
      return i
    
def simplificar_reacciones(lista, l):
    new_list = [['id_r', 'name', 'reactivos', 'productos', 'lower_bound', 'upper_bound']]

    for i in range(1,len(lista)):
        row = lista[i]
        new_list.append([row[0], row[1],[],[],row[-2], row[-1]])
        for j in range(2,1670):
            dato = float(row[j])
            if dato == -1:
                new_list[i][2].append(l[j])
            elif dato == 1:
                new_list[i][3].append(l[j])
            elif dato != 0:
                print(type(dato), dato)
                #1/(6-(2*3))
    return new_list





#LISTAS DE NODOS
metabolitos = []
reacciones = []



#leer los metabolitos
with open('bases\metabolitos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        metabolitos.append(row[0].split(sep=";"))

#leer las reacciones
with open('bases\prueba_reac.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='$', quotechar='|')
    for row in spamreader:
        row[0] = row[0].replace(';;', ';0;').replace(';;', ';0;')
        reacciones.append(row[0].split(sep=";"))


reacciones = simplificar_reacciones(reacciones[0:],reacciones[0])

metabolitos[0][0]='id_m'
datos_meta = metabolitos.pop(0)
datos_reac = reacciones.pop(0)


#CREAR GRAFO
G = nx.DiGraph()

#crear nodos. metabolitos
for info_met in metabolitos:
    G.add_node(info_met[0])

#crear nodos. reacciones
for info_rea in reacciones:
    G.add_node(info_rea[0])


#crear aristas dirigidas
for i in range(len(reacciones)):
    for j in range(len(reacciones[i][2])):
        G.add_edge(reacciones[i][2][j], reacciones[i][0])

    for j in range(len(reacciones[i][3])):
        G.add_edge(reacciones[i][0], reacciones[i][3][j])

print(reacciones)

print(list(nx.center(G)))



nx.draw_shell(G, with_labels=True)
plt.show()