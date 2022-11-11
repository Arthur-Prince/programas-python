# -*- coding: utf-8 -*-

'''
Implementação de programa que resolve derivação em função de uma 
variável usando técnicas de derivação 
'''

from estruturas.equacao import Equacao
from copy import copy

def derivar(equacao, em_funcao):
    '''
    Função base, que identifica a derivada e executa recursivamente
    a derivação de acordo com a regra aplicável a derivação do termo.
    '''
    assert isinstance(equacao, Equacao), 'É esperado um objeto do\
						   tipo Equacao'
    assert isinstance(em_funcao, str),'É esperado um objeto do tipo str'
    #Condicional definido para a regra 4 - derivar_simples
    if isinstance(equacao[0], (int, float)):
        return derivar_simples(equacao, em_funcao)
    #Condicional definido para a regra 2, derivada de uma soma
    elif equacao[0] == '+':
        return derivar_soma(equacao, em_funcao)
    #Condicional definido para a regra 1, derivada de uma multiplicação
    elif equacao[0] == '*':
        return derivar_mult(equacao, em_funcao)
    #Condicional definido para  a regra 3, derivada de um quociente.
    elif equacao[0] == '/':
        return derivar_div(equacao, em_funcao)

def derivar_simples(equacao, em_funcao):
    '''
    Aplica a derivação de acordo com a Regra 4
    O índice 0 corresponde ao multiplicador.
    O índice 1 corresponde a variável.
    O índice 2 corresponde ao valor da exponencial.
    '''
    #Deriva, se a derivada está em função da função fornecida.
    if equacao[1] == em_funcao:
        eq_aux = Equacao()
        eq_aux.append(equacao[0]*equacao[2])
        eq_aux.append(equacao[1] if equacao[0]*equacao[2] !=0 else 'del')
        eq_aux.append(equacao[2]-1)
        return eq_aux
    else:
        eq_aux = Equacao()
        eq_aux.append(0)
        eq_aux.append(equacao[1])
        eq_aux.append(equacao[2])
        return eq_aux 


def derivar_soma(equacao, em_funcao):
    '''
    Aplica a derivação de acordo com a regra 2 e aplica recursivamente
    a função derivar, para derivar os termos, de acordo com respectiva
    técnica de derivação.
    O índice 0 corresponde ao valor da operação, no caso sempre será '+'
    O índice 1 corresponde ao primeiro termo da soma.
    O índice 2 corresponde ao segundo termo da soma.
    '''
    eq_aux = Equacao()
    eq_aux.append(equacao[0])
    eq_aux.append(derivar(equacao[1], em_funcao))
    eq_aux.append(derivar(equacao[2], em_funcao))
    return eq_aux


def derivar_mult(equacao, em_funcao):
    '''
    Aplica a derivação de acordo com a regra 1 e aplica recursivamente
    a funçao derivar, para derivar os termos, de acordo com respectiva
    técnica de derivação.
    '''
    eq_aux = Equacao()
    eq_aux.append('+')

    #Define equação formada pelo primeiro termo
    #O primeiro termo vezes a derivada do segundo termo
    eq_termo1_aux = Equacao()
    eq_termo1_aux.append('*')
    eq_termo1_aux.append(equacao[1])
    eq_termo1_aux.append(derivar(equacao[2], em_funcao))

    #Define equação formaa pelo segundo termo
    #A derivada do primeiro termo vezes o segundo termo
    eq_termo2_aux = Equacao()
    eq_termo2_aux.append('*')
    eq_termo2_aux.append(derivar(equacao[1], em_funcao))
    eq_termo2_aux.append(equacao[2])

    #Adiciona os termos a equação resultante
    eq_aux.append(eq_termo1_aux)
    eq_aux.append(eq_termo2_aux)

    return eq_aux
    
def derivar_div(equacao, em_funcao):
    '''
    Aplica a derivação de acordo com a regra 3 e efetua recursivamente
    a funçao derivar, para derivar os termos, de acordo com respectiva
    técnica de derivação.
    '''
    #Define o primeiro termo da derivada, derivada do primeiro termo vezes o 
    #segundo
    eq_termo1a_aux = Equacao()
    eq_termo1a_aux.append('*')
    eq_termo1a_aux.append(derivar(equacao[1], em_funcao))
    eq_termo1a_aux.append(equacao[2])

    #Define a segunda parte do primeiro termo. 
    eq_termo1b_aux = Equacao()
    eq_termo1b_aux.append('*')
    #Torna o primeiro termo negativo, para a operação '+' ser usada mesmo se
    #tratando de uma subtração
    termo_aux = copy(equacao[1]) #Necessário?
    termo_aux[0] *= -1
    eq_termo1b_aux.append(termo_aux)
    eq_termo1b_aux.append(derivar(equacao[2], em_funcao))

    eq_termo1_aux = Equacao()
    eq_termo1_aux.append('+')
    eq_termo1_aux.append(eq_termo1a_aux) 
    eq_termo1_aux.append(eq_termo1b_aux)   
    
    #Define o termo 2 da divisão, o segundo termo da divisão ao quadrado
    eq_termo2_aux = Equacao()
    #Tratar caso que o quociente for uma equação
    if isinstance(equacao[2][0], str):
        eq_termo2_aux.append('*')
        eq_termo2_aux.append(equacao[2])
        eq_termo2_aux.append(copy(equacao[2]))
    else:
        eq_termo2_aux.append(equacao[2][0]*equacao[2][0])
        eq_termo2_aux.append(equacao[2][1])
        eq_termo2_aux.append(equacao[2][2]*2)

    #Define a equacão resultande
    eq_aux = Equacao()
    eq_aux.append('/')
    eq_aux.append(eq_termo1_aux)
    eq_aux.append(eq_termo2_aux)

    return eq_aux

