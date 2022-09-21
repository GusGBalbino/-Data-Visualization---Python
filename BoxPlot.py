#Estudo de Caso - Bio informática

from re import A, T


entrada = open("bacteria.fasta").read()
saida = open("bacteria.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace(">R_024570.1 Escherichia coli strain U 5/41 16S ribosomal RA, partial sequence", "")
entrada = entrada.replace(">M10098.1 Human 18S rRA gene, complete", "")
entrada = entrada.replace("\n", "")

for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1

#Parte em HTML

i = 1

for valor in cont:
    transparence = cont[valor]/max(cont.values())
    saida.write("<div style ='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparence)+"')>"+valor+"</div>")
    
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i+=1
saida.close()
