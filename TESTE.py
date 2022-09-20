import matplotlib.pyplot as plt

#Gráfico de linhas

x1 = [0,18,60]
y1 = [0,50,100]

title = "Gráfico em Python"
eixox = "Eixo X"
eixoy = "Eixo Y"


#Gráfico de barras

x2 = [1,3,5,7,9]#Quantidade de barras

y2 = [2,3,5,7,3] #Tamanho das barras

#Comparando gráficos de barras

comp_x = [2,4,6,8,10]
comp_y = [4, 6, 10, 14, 6]


plt.title(title)

plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x1, y1)
#plt.bar(x2,y2, label = "Grupo 1")
#plt.bar(comp_x, comp_y, label = "Grupo  2")
#plt.legend()
plt.scatter(x2,y2, label = "Pontos de ocorrência", color = 'red', marker = '.', s = 100)
plt.plot(x2,y2, color = 'black', linestyle = "-.")
#plt.legend()

#plt.show()