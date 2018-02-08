d = {"elloa": "111-111", "sergio": "222-222", "emerson":"333-4444","miguel": "444-4444"}
print(d)
print(len(d))

agenda = {"elloa": {"telefone":"111-111","email":"elloalalala"},
"miguel": {"telefone":"222-222","email":"emailmiguel"},
"jucimar": {"telefone":"333-333","email":"emailjucimar"}}
print(agenda["elloa"])
print(agenda.keys())

#impressao chaves
for contato in agenda.keys():
    print(agenda[contato]['email'])

#inclusao    
agenda['antonio'] = {'telefone': '555-555','email':'antonio@ifam'}

#Busca
nome = input("Informe um nome:")
if nome in agenda.keys():
    print(True)
else:
    print(False)
# Delecao    
agenda.pop("elloa")
# Sobrescrita
agenda['antonio'] = {'telefone': '9999-999','email':'zzzantonio@ifam'}

print(agenda)

# Impressao ordenada
chavesOrdenada = list(agenda.keys())
chavesOrdenada.sort()
for chave in chavesOrdenada:
    print(agenda[chave])