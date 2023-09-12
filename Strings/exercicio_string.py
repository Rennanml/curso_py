nome = input('Digite seu nome:\n')
idade = input('Digite sua idade:\n')


if nome and idade:
    print(f'Seu nome é: {nome}\n')
    print(f'Seu nome invertido é: {nome[::-1]}\n')
    if " " in nome:
        print('Seu nome tem espaço!\n')
    else:
        print('Seu nome não tem espaço!\n')
    print(f'Seu nome tem {len(nome)} letras!\n')
    print(f'A primeira letra do seu nome é: {nome[0]}\n')
    print(f'A última letra do seu nome é; {nome[-1]}\n')
else:
    print('Desculpe! Você deixou os campos vazios...')