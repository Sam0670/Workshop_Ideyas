print("Insira os lados do Triangulo")

# Salvando valores

a = (float(input('Lado a: ')))
b = (float(input('Lado b: ')))
c = (float(input('Lado c: ')))

# Verificando

if (a == b) and (a == c):
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isosceles')
elif (a != b) and (b != c) and ( c !=a):
    print('Escaleno')
else:
    print('Nao e um triangulo')
