import random
import math

def generar_notas():
    return [random.randint(1, 10) for _ in range(5)]

def calcular_promedio(notas):
    return math.fsum(notas) / len(notas)
