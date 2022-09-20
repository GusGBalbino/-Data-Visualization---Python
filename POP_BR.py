#Crescimento da população brasileira 1980 - 2016 - Datasus

import matplotlib.pyplot as plt

data = open("populacao_brasileira.csv").readlines()

x = []

y = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))
        
plt.bar(x,y, color = "#e4e4e4")
plt.plot(x,y, color = "k", linestyle="-.")

plt.title("Crescimento da População Brasileira 1980 -2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

plt.show()
#plt.savefig("pop_br.pdf")
        
