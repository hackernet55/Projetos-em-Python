# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:53:54 2019

@author: Joao Vitor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:24:50 2019

@author: Joao Vitor
"""
#Exercicio Somar Quadrado +A+B
"""
def somaquadrada(j,v,m):
        return j*j+v+m
print(somaquadrada(2,5,7))

"""
#Se é vogal ou consoante: Exercicio
"""
def verificanome (a):
    if a=="a"or a=="e" or a=='i' or a=='o'or a=='u' or a=='A'or a=='E' or a=='I' or a=='O'or a=='U':
        print(1)
    else:
        print(0)
    return a

a=input("Digite nome:")
print (verificanome(a))
"""
#REcebe Consoante e Voagais
def tot(str1):
    vogais =[]
    consoantes =[]
    for i in str1:
       if i=="a" or i=="e" or i=='i' or i=='o'or i=='u':
           vogais.append(i)
       else:
           consoantes.append(i)
    letras=[vogais, consoantes] 
    return letras          
print(tot('aabbccddeeff'))       