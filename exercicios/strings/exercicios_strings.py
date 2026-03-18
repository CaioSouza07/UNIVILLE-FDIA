#EXERCICIOS DE STRINGS

"""
1) Extraia a substring "Univille" e "Joinville" da seguinte String:
"""

s = "Curso de graduação Universidade Univille Campus - Joinville!"

s = s.replace("Joinville", "")
s = s.replace("Univille", "")

print(s)


#--------------------------------------------------------------------------------------------

"""
2) Qual é o resultado de aplicar o seguinte *slicing* `[::-1]`:
"""

s = "Curso de graduação Universidade Univille Campus - Joinville!"

s = s[::-1]

print(s)

#Imprimiu o contrario, tope demais


#--------------------------------------------------------------------------------------------