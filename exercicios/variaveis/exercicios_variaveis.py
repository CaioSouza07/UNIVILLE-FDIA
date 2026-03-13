#EXERCICIOS DE VARIAVEIS

"""
1) Defina as variáveis `x = 1`, `y = 2.3` e `z = x+y`. Qual o tipo de `x`, `y` e `z`?
"""

x = 1
y = 2.3
z = x+y

type(x)
type(y)
type(z)

#--------------------------------------------------------------------------------------------

"""
2) Defina as variáveis `x = 1`, `y = 4` e `z = x/y`. Qual o valor de `z`?
"""

x = 1
y = 4
z = x/y

print(f'O valor de z é: {z}')

#--------------------------------------------------------------------------------------------

"""
3) Defina as variáveis `x = 1.0`, `y = 4` e `z = x/y`. Qual o valor de `z`?
"""

x = 1.0
y = 4
z = x/y

print(f'O valor de z é: {z}')

#--------------------------------------------------------------------------------------------

"""
4) Calcule seu [Índice de Massa Corporal (IMC)](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal).
"""

import math

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

print(imc)