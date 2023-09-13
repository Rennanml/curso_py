import os
i = 0
lista_do_mercado = []

while i == 0:
    entrada = input('Escolha uma opção:\n[a]dicionar, [e]liminar, [l]istar, [f]echar: ')
    
    if entrada == 'a':
        os.system('cls')
        adicionar = input('Item a ser adicionado: ')
        lista_do_mercado.append(adicionar)
        adicionar = ""
        
    elif entrada == 'e':
        os.system('cls')
        
        try:
            eliminar = int(input('Índice do item a ser eliminado: '))
            del lista_do_mercado[eliminar]
            eliminar = ""
            
        except ValueError:
            print('Por favor digite úm número inteiro...')
            
        except IndexError:
            print('Esse número não existe na lista...')
            
        except Exception:
            print('Erro desconhecido...')
            
    elif entrada == 'l':
        os.system('cls')
        if len(lista_do_mercado) == 0:
            print('Não há nada para listar')
        print('Lista de compras:')
        for indice, item in enumerate(lista_do_mercado):
            print(indice, item)
            
    elif entrada == 'f':
        os.system('cls')
        print("Lista fechada.")
        i += 1
        
    else:
        os.system('cls')
        print('Por favor digite uma entrada válida!')