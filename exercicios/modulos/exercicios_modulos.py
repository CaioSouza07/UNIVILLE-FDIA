#EXERCICIOS DE MODULOS

"""
1) Após importar o módulo [math](http://docs.python.org/3/library/math.html) calcule:

* `x = cos(pi/2) + sin(pi/2)`
* `x = √3`
* `x = log2 10`
"""

import math

x = math.cos(math.pi / 2) + math.sin(math.pi / 2)
x = math.sqrt(3)
x = math.log(10, 2)

#--------------------------------------------------------------------------------------------

"""
2) Importe o módulo `calendar` e descubra:

* 2018 é um ano bissexto (leap year)?
* Dia 22 de Maio de 1992 foi que dia da semana?
* O mês de Julho de 2000 começou em que dia da semana?
"""

import calendar

dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

calendar.isleap(2018)
dias[calendar.weekday(1992, 5, 22)]
dias[calendar.weekday(2000, 7, 1)]