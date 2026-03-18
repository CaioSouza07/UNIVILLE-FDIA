#EXERCICIOS DE OPERADORES E COMPARACOES

"""
1) Defina a variável `x = 7`:
* `x * 2` é maior que `10`?
* `x / 3` é menor que `5`?
* `x` ao quadrado é igual a `49`?
"""

x = 7

print(x * 2 > 10)
print(x / 3 < 5)
print(x**2 == 49)


#--------------------------------------------------------------------------------------------

"""
2) Defina a variável `y = 3`:
* `y` é menor que `10` e `x` é maior que `10`?
* `y` é maior ou igual a `3` ou `x` é igual a `8`?
* `y` não é igual a `4`?
"""

y = 3

print(y < 10 and x > 10)
print(y >= 3 or x == 8)
print(not y == 4)


#--------------------------------------------------------------------------------------------

"""
3) Verifique se seu [Índice de Massa Corporal (IMC)](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal) está dentro do padrão recomendado pela OMS:
"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

match imc:
    case i if i < 16:
        print("Magreza grave")
    case i if i >= 16 and i <17:
        print("Magreza moderada")
    case i if i >= 17 and i < 18.5:
        print("Magreza leve")
    case i if i >= 18.5 and i < 25:
        print("Saudavel")
    case i if i >= 25 and i < 30:
        print("Sobrepeso")
    case i if i >= 30 and i < 35:
        print("Obesidade Grau I")
    case i if i >= 35 and i < 40:
        print("Obesidade Grau II (severa)")
    case i if i >= 40:
        print("Obesidade Grau III (morbida)")




#--------------------------------------------------------------------------------------------