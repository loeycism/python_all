# aula 3 parte 3
#usando IF, ELSE, ELIF e OR
#como usar os condicionais (IF, ELSE e ELIF) e os operadores lógicos (AND, OR e NOT)

a = int(input('entre com o primeiro valor: '))
b = int(input('entre com o segundo  valor: '))
resto_a = a % 2
resto_b= b % 2

if resto_a == 0 or resto_b == 0:
    print('foi digitado um número par')
else:
    print('nenhum número par foi digitado')
