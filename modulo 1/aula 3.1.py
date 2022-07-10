#Como criar um código em Python que funcione de acordo com a relação das variáveis

#como usar os condicionais (IF, ELSE e ELIF) e os operadores lógicos (AND, OR e NOT)

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))


if a > b and a > c:
    print('o maior número é {}' .format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}' . format(c))
print('Final do programa')