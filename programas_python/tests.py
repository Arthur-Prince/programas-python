from derivar import *
from estruturas.equacao import Equacao
from copy import copy

## Eprintuturando alguns exemplos de equações

#Equacao: 3x**2
eq = Equacao()
eq.append(3)
eq.append('x')
eq.append(2)
 
#Equação: 12y**2
eq2 = Equacao()
eq2.append(12)
eq2.append('y')
eq2.append(2)

#Equação: 27x**7
eq3 = Equacao()
eq3.append(27)
eq3.append('x')
eq3.append(7)

#Termo constante
#6x0
eq_const = Equacao()
eq_const.append(6)
eq_const.append('x')
eq_const.append(0)

#Para o Teste da soma
#3x**2 + 6 > 6x
eq_soma = Equacao()
eq_soma.append('+')
eq_soma.append(eq)
eq_soma.append(eq_const)

#3x**2 + 12y**2 > 6x 
eq_soma2 = Equacao()
eq_soma2.append('+')
eq_soma2.append(eq) 
eq_soma2.append(eq2)

#3x**2 + 6   +   3x**2 + 12y**2 > 6x + 6x
eq_soma3 = Equacao()
eq_soma3.append('+')
eq_soma3.append(eq_soma)
eq_soma3.append(eq_soma2)

#27x**7 + 3x**2 > 189x**6 + 6x
eq_soma5 = Equacao()
eq_soma5.append('+')
eq_soma5.append(eq3)
eq_soma5.append(eq)

#Para o Teste da multiplicação
#3x**2 * 3x**2 + 12y**2 > (3x**2 * 6x) + (6x * 3x**2 + 12y**2)
eq_mult = Equacao()
eq_mult.append('*')
eq_mult.append(eq)
eq_mult.append(eq_soma2)

#(3x**2 * 3x**2 + 12y**2) * (27x**7 + 3x**2) > (3x**2 * 3x**2 + 12y**2 |*| 189x**6 + 6x) + ((3x**2 * 6x) + (6x * 3x**2 + 12y**2) * 27x**7 + 3x**2))
eq_mult2 = Equacao()
eq_mult2.append('*')
eq_mult2.append(eq_mult)
eq_mult2.append(eq_soma5)

#Teste da divisão
eq_div = Equacao()
eq_div.append('/')
eq_div.append(eq)
eq_div.append(eq2)

#Teste exemplo da especificação
t1 = Equacao()
t1.append(5)
t1.append('x')
t1.append(3)

t2 = Equacao()
t2.append(6)
t2.append('x')
t2.append(1)

t3 = Equacao()
t3.append(1)
t3.append('y')
t3.append(1)

t4 = Equacao()
t4.append(-10)
t4.append('x')
t4.append(2)

t5 = copy(t3)
   
t6 = Equacao()
t6.append(100)
t6.append('None')
t6.append(0)

eq_1 = Equacao()
eq_1.append('/')
eq_1.append(t2)
eq_1.append(t3)

eq_2 = Equacao()
eq_2.append('*')
eq_2.append(t4)
eq_2.append(t5)

eq_3 = Equacao()
eq_3.append('+')
eq_3.append(t1)
eq_3.append(eq_1)

eq_4 = Equacao()
eq_4.append('+')
eq_4.append(eq_2)
eq_4.append(t6)

eq_final = Equacao()
eq_final.append('+')
eq_final.append(eq_3)
eq_final.append(eq_4)

           
# Teste derivar_generico

#print(derivar(eq, 'x')) deve imprimir '6x'
print(derivar(eq, 'x'))

#Caso termo for uma constante
#print(derivar(eq_const, 'x')) deve imprimir '0'
print(derivar(eq_const, 'x'))

#Espera-se entrar já com a equação formatada, sem variaveis iguais, corrigir?
#print(derivar(eq_soma3, 'x')) deve imprimir '6x + 6x'
print(derivar(eq_soma3, 'x')) 

# Teste derivar_simples
#print(derivar_simples(eq, 'x')) deve imprimir '6x'
print(derivar_simples(eq, 'x'))

#print(derivar_simples(eq2, 'y')) deve imprimir '24y'
print(derivar_simples(eq2, 'y'))
   
# Teste derivar_soma
#print(derivar_soma(eq_soma, 'x')) deve imprimir '6x'
print(derivar_soma(eq_soma, 'x'))

#print(derivar_soma(eq_soma2, 'x')) deve imprimir '6x'
print(derivar_soma(eq_soma2, 'x'))

# Teste derivar_mult
#print(derivar_mult(eq_mult, 'x')) deve imprimir '3x**2 * 6x + 6x * 3x**2 +
#12y**2'
print(derivar_mult(eq_mult, 'x'))

#print(derivar_mult(eq_mult2, 'x')) deve imprimir '3x**2 * 3x**2 + 12y**2 * 
#189x**6 + 6x + 3x**2 * 6x + 6x * 3x**2 + 12y**2 * 27x**7 + 3x**2')
print(derivar_mult(eq_mult2, 'x'))

# Teste derivar_div
#print(derivar_div(eq_div, 'x')) deve imprimir '(6x * 12y**2)/144y**4'
print(derivar_div(eq_div, 'x'))

# Teste especificacao
#print(derivar(eq_final, 'x')) deve imprimir '15x**2 + (6 * y + )/y**2 +
# -20x * y'
print(derivar(eq_final, 'x'))
