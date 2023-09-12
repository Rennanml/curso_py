# lista = ['rennan', "mamãe", 'papai']
# j = 0

# for i in lista:
#     print(i, f'Índice: {j} // ', end=" ")
#     j += 1
    
#Ou

lista = ['rennan', "mamãe", 'papai']
indices = range(len(lista))

for indice in indices:
    print(" // ", indice, lista[indice], " // ", end=" ")