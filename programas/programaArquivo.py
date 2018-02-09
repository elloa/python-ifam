file = open("arquivo.txt","r+")

linha = file.readline()
while (linha):
    print(linha)
    linha = file.readline()
    
    



file.write("Escrever isso!")

file.close()