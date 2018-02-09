with open("arquivo.txt","r+") as arq:
    for linha in arq.readlines():
        print(linha.upper())
        
    arq.write("Uma nova linha")
    
