# -*- coding: utf-8 -*-

'''Implementação do TAD equação para representar equações matemáticas'''

from estruturas.lista_duplamente_ligada_com_sentinela import ListaLigadaDupla

class Equacao(ListaLigadaDupla):
    '''Subclasse que implementa uma equação usando Lista Duplamente Ligada'''
    def __str__(self):
        #Se o primeiro nó é um inteiro, é um termo do tipo: [mult, var, exp]
        if isinstance(self[0], (int, float)):
            #Imprimir tratando as exceções
            #Exceção 1, caso o valor seja a constante 0 
            if self[0] == 0 or self[1] == 'del':
                return '0'
            temp = ''
            #Exceção 2, imprimir caso o valor da constante multiplicativa
            #seja diferente de 1
            if self[0] != 1:
                temp += str(self[0])
            #Exceção 2,Imprimir a variável caso o valor o expoente for
            #diferente de zero
            if self[2] != 0:
                #Caso o valor da exponencial for igual a 1, imprimir somente
                #a variável, caso contrário imprimir variável e o sinal de
                #exponenciação
                if self[2] == 1:
                    temp += self[1]
                else:
                    temp += self[1] + '**'
		#Exceção 3: Imprimir o valor do expoente caso o valor do expoente for
                # diferente de 0 e diferente de 1
                if self[2] != 1:
                    temp += str(self[2])
            return temp
        #Se o primeiro nó é uma string, se trata de uma equação na forma
        #[operador,[termo_1],[termo_2]]
        #A condição recorre cada termo, afim de receber sua forma linear.
        elif isinstance(self[0], str):
            term_aux_1 = str(self[1])
            term_aux_2 = str(self[2])
            #Tratamento de caso que não imprime valor nulo
            if self[0] == '*':
                if term_aux_1 == '0' or term_aux_2 == '0':
                    return '0'
            temp = ''
            #Condicional para caso os termos sejam constante nula, não 
            #imprimir. Caso for uma divisão, colocar parênteses para melhor
            # visualização
            if self[0] != '/':	
                if term_aux_1 != '0':
                    temp += term_aux_1
                if term_aux_1 !='0' and term_aux_2 != '0':
                    temp += ' ' +  self[0] + ' ' 
                if term_aux_2 != '0':
                    temp += term_aux_2
                return temp
            else:
                if term_aux_1 != '0':
                    temp += '(' + term_aux_1 + ')'
                if term_aux_2 != '0':
                    temp += self[0] + term_aux_2
                return temp


