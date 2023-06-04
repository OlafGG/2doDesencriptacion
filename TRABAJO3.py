# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:45:36 2023

@author: Olaf
"""
import numpy as np
import random

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arregloNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

print(alfabeto)    
print(arregloNumeros)



textoPlano = 'HELLOWORLD'
clave = 'FACUTADDEI'


def textoClaveAleatorio (textoPlano, alfabeto, clave, numerosAleatorios) : 
    cifradoTA = []
    cifradoCA = []
    for j in range(len(textoPlano)):
        letra1 = textoPlano[j]
        letra2 = clave[j]
        textoplanonumerido = alfabeto.index(letra1)
        textoclave = alfabeto.index(letra2)
        Numerotexto = listaNumerosAleaotiros[textoplanonumerido]
        numeroClave = listaNumerosAleaotiros[textoclave]
        cifradoTA.append(Numerotexto)
        cifradoCA.append(numeroClave)
    print ("Texto: ", textoPlano)
    print("Aleatorio texto: ", cifradoTA)
    print("Texto clave: ", clave)
    print("Cifrado clave aleatoridad: ", cifradoCA)
    return cifradoCA, cifradoTA


def numerosAleatorios (arregloNumeros):
    listaNumerosAleaotiros = random.sample(range(1, len(arregloNumeros) + 1), len(arregloNumeros))

    print("lista aleatoria",listaNumerosAleaotiros)  
    return listaNumerosAleaotiros 

def cifradoSuma (cifradoTA, cifradoCA): 
    cifradoSumaA = []
    flag = []
    for i in range(len(textoPlano)): 
        suma = cifradoTA[i] + cifradoCA[i]
        if (suma > 27): 
            flag.append(1)
            suma = suma - 27
        else: 
            flag.append(0)
        cifradoSumaA.append(suma)
    print("Suma aleatoria", cifradoSumaA)
    print ("flag", flag)
    return flag, cifradoSumaA



def desifradoTexto(clave, cifradoSumaA, cifradoTA, cifradoCA):
    valoresPalabras = []
    for i in range(len(clave)): 
        if (flag[i] == 1): 
            valorR = cifradoSumaA[i] + 27
            valorR = valorR - cifradoCA[i]
            valoresPalabras.append(valorR)
        else: 
            valorR = cifradoSumaA[i] - cifradoCA[i]
            valoresPalabras.append(valorR)
    
    print("Valores palabra desifrados: ", valoresPalabras)
    print("Valores reales palabra: ", cifradoTA)
    return valoresPalabras


listaNumerosAleaotiros = numerosAleatorios(arregloNumeros)
(cifradoCaN, cifradoTaN) = textoClaveAleatorio(textoPlano, alfabeto, clave, listaNumerosAleaotiros)
(flag, sumaAN) = cifradoSuma(cifradoTaN, cifradoCaN)
valoresPalabras = desifradoTexto(clave, sumaAN, cifradoTaN, cifradoCaN)

