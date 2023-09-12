#Guia básico sobre listas:

lista = ["rennan", 1, 2, 3, 4, "olá!"]
print(lista)

#Funções das listas: 

lista.append("Adicionado!") #Adiciona um termo ao último índice
print(lista)

removido = lista.pop() #Remove o último termo (quando não é passado nenhum parâmetro)
print(lista, "Removido: ", removido)

lista.insert(0, "Oi!") #Adiciona um termo ao índice indicado
print(lista)

sortido = lista.sort()
print(sortido)