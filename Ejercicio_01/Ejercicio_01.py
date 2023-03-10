'''
Ejercicio 1: Sucesor de un DÍA de la semana





El tipo DÍA define por enumeración un día de la semana. En el ejercicio que determina el día del 1 de mayo de un año dado, también se ha especificado una función sucesor para un día de la semana. Falta dar una definición de esta función.

Dar una definición completa de la función sucesor para un día de la semana.

Todavía no disponemos de las herramientas que nos permitirán dar una definición «elegante» de esta función. Lo haremos más adelante.
'''
import itertools
from enum import Enum #vincular el conjunto de miembros a valore

DIA = Enum('DIA', ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO'])

def sucesor(dia_actual):
    ciclo = itertools.cycle(DIA)
    siguiente = next(ciclo)
    while siguiente != dia_actual:
        siguiente = next(ciclo)
    return next(ciclo)

if __name__ == '__main__':
    dia_actual = DIA.LUNES
    print('El dia de la semana siguiente a {} es {}'.format(dia_actual.name, sucesor(dia_actual).name))
