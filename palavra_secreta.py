palavra_secreta = 'rennan'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!\n')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    if palavra_formada == palavra_secreta:
        print('Parabéns! Você venceu!')
        print(f'A palavra secreta é: "{palavra_formada.upper()}"!!')
        print(f'E o número de tentativas foi: {numero_tentativas}!')
        break
    else:
        print(palavra_formada)
    
    