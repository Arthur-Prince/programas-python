# -*- coding: utf-8 -*-
'''Implementação no para lista ligada dupla'''

class No (object):
    '''Implementação no para lista ligada dupla'''
    __slots__ = ('__dado', '__prox', '__ante')
    def __init__(self, dado = None, prox = None, ante = None):
        self.__dado = dado
        self.__prox = prox
        self.__ante = ante

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        self.__dado = dado
  
    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self, prox):
        self.__prox = prox
    
    @property
    def ante(self):
        return self.__ante
    
    @ante.setter
    def ante(self, ante):
        self.__ante = ante

