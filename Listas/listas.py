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

lista_2 = [8, 9, 10]

lista.extend(lista_2) #Concatena lista (também pode ser usado o "+")
print(lista)

lista_2 = lista.copy() #Copia a lista para outra lista
print(lista_2)

