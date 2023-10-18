#leer un csv y guardar los ID de los metabolitos
import csv

metabolitos = []

with open('bases\metabolitos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        metabolitos.append(row[0].split(sep=";")[0])

print(metabolitos)