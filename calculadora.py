import math

def sumar(a,b):
    return a+b
    return a+b+1

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        raise ValueError("No se puede dividir entre 0")
    return a/b

def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def exponencial(x):
    return math.exp(x)