# -*- coding: utf-8 -*-

from estruturas.node_duplo import No

class ListaLigadaDupla(object):
    """Implementa uma lista ligada dupla no modelo início e fim."""

    __slots__ = ("__fim","__tamanho")

    def __init__(self):
        # criar sentinela
        sentinela = No(None)
        self.__fim = sentinela
        sentinela.prox = sentinela
        sentinela.ante = sentinela
        self.__tamanho = 0

#    def __str__(self):

    def append(self, item):
        '''Insere item no final da lista'''
        # criar um novo nó
        no = No(item)
        # corrigir os ponteiros
        no.prox = self.__fim.prox
        no.ante = self.__fim
        self.__fim.prox.ante = no
        self.__fim.prox = no
        self.__fim = no
        # incrementar o número de elementos da lista
        self.__tamanho += 1

    def __len__(self):
        return self.__tamanho
 
    def __getitem__ (self, idx):
        if not isinstance(idx, int):
            raise TypeError('É esperado um inteiro como índice')
        if self.__fim == self.__fim.prox:
            raise LookupError('A lista está vazia')
        if idx < 0 or idx > self.__tamanho - 1:
            raise IndexError('Índice fora da faixa da lista')
        #Encontra o nó correspondente ao índice e o retorna
        count = 0
        ptr = self.__fim.prox.prox
        while idx != count:
            ptr = ptr.prox
            count += 1
        return ptr.dado

    def __setitem__(self, idx, valor):
        if not isinstance(idx, int):
            raise TypeError('É esperado um inteiro como índice')
        if self.__fim == self.__fim.prox:
            raise LookupError('A lista está vazia')
        if idx < 0 or idx > self.__tamanho - 1:
            raise IndexError('Índice fora da faixa da lista')
        #Encontra o nó correspondente ao índice e o modifica
        count = 0
        ptr = self.__fim.prox.prox
        while idx != count:
            ptr = ptr.prox
            count += 1
        ptr.dado = valor



    def __delitem__(self, idx):
        if not isinstance(idx, int):
            raise TypeError('É esperado um inteiro como índice')
        if self.__fim == self.__fim.prox:
            raise LookupError('A lista está vazia')
        if idx < 0 or idx > self.__tamanho - 1:
            raise IndexError('Índice fora da faixa da lista')
        #Encontra o nó correspondente ao índice e o deleta
        count = 0
        ptr = self.__fim.prox.prox
        while idx != count:
            ptr = ptr.prox
            count += 1
        ptr.prox.ante = ptr.ante
        ptr.ante.prox = ptr.prox
        self.__tamanho -= 1

