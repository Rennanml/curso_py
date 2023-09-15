import os
import sys
import re
import random

mult1 = 10
mult2 = 11
lista_mult = []
lista_mult2 = []
aux_soma = 0
aux_soma2 = 0
cpf_entrada = ''

try:
    print('Gerador de cpf!!')
    for i in range(9):
        cpf_entrada += str(random.randint(0, 9))
    cpf_entrada = cpf_entrada.replace('.', '').replace('-', '')
    
    entrada_e_sequencial = cpf_entrada == cpf_entrada * len(cpf_entrada)
    if entrada_e_sequencial:
        sys.exit()
    
    if len(cpf_entrada) > 9:
        print('Por favor, digite apenas os 9 primeiros dígitos do CPF para validação!')
    else:
        #Primeiro dígito do cpf
        cpf_int = [int(digito) for digito in cpf_entrada]  #Converte em inteiro
        for numero1 in cpf_int:
            lista_mult.append(numero1 * mult1)
            mult1 -= 1
        for iter in lista_mult:
            aux_soma += iter
        digito1 = (aux_soma * 10) % 11
        digito1 = digito1 if digito1 <= 9 else 0
        
        #Segundo dígito do cpf
        cpf2 = cpf_int
        cpf2.append(digito1)
        cpf2_int = (int(digit) for digit in cpf2)
        for numero2 in cpf2_int:
            lista_mult2.append(numero2 * mult2)
            mult2 -= 1
        for iter2 in lista_mult2:
            aux_soma2 += iter2
        digito2 = (aux_soma2 * 10) % 11
        digito2 = digito2 if digito2 <= 9 else 0
        
        print('------------------------------------------')
        print(f'O resultado final do cpf é: {cpf_entrada[:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{str(digito1) + str(digito2)}')
        print('------------------------------------------')    
            
except ValueError:
    ...
