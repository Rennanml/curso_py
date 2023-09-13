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

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

#ou 

for indice, nome in enumerate(lista):
    print(indice, nome)

#Tuples (listas imutáveis)

tupla = ('rennan', 'é', 'Legal')
print(tupla)

# Funções 

frase = 'Olha só, que interessante!'
lista_frase = frase.split(',')
print(lista_frase) 


frases_unidas = '-'.join('abc')
print(frases_unidas)
frases_unidas_2 = '-'.join(lista_frase)
print(frases_unidas_2)


