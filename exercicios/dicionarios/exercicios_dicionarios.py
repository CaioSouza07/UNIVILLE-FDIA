#EXERCICIOS DE DICIONARIOS

"""
1) Retorne a lista de países presentes no dicionário `pib`.
"""

pib = {
    "china": 23120,
    "usa": 19360,
    "india": 9447,
    "japan": 5405,
    "germany": 4150,
    "russia": 4000,
    "indonesia": 3243,
    "brazil": 3219
}

print(pib.keys())


#--------------------------------------------------------------------------------------------

"""
2) Retorne a lista de pibs presentes no dicionário `pib`, some todos os valores e adicione ao dicionário a chave `total` com o valor obtido. Faça tudo isso de forma programática.
"""

pib = {
    "china": 23120,
    "usa": 19360,
    "india": 9447,
    "japan": 5405,
    "germany": 4150,
    "russia": 4000,
    "indonesia": 3243,
    "brazil": 3219
}

soma = 0
for pais in pib.values():
    soma += pais

pib["total"] = soma

#--------------------------------------------------------------------------------------------