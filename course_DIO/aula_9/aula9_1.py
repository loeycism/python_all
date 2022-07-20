#módulos são os arquivos .py

"""
no console:
import aula9_01

pelo módulo dá pra conectar em qualquer coisa

from aula9_01 import Televisão
importando apenas a classe
"""
from aula9_01 import Televisão
from aula9_02 import Calculadora

televisao = Televisão()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5, 10)
print(calculadora.soma())
