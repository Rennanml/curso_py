frase = input('Escreva a frase que deseja analisar:\n')

contador = 0
letra_mais_frequente = ""

for letra in frase:
    letra_apareceu = frase.count(letra)
    
    if letra == ' ':
        continue
    
    if letra_apareceu > contador:
        contador = letra_apareceu
        letra_mais_frequente = letra
        
print(f'A letra que mais apareceu foi a letra "{letra_mais_frequente}" que apareceu {contador}x\n')