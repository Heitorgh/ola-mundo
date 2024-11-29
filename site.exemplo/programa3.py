ListaDeNotas= []
Maximo = 0
Minimo = 10

Notas = float(input('Entre com uma nota de 0 a 10: '))

while 0 <= Notas <= 10 :
    ListaDeNotas.append(Notas)

    if Notas > Maximo:
    
        Maximo = Notas

    if Notas < Minimo:

        Minimo = Notas


    Notas = float(input('Entre com outra nota de 0 a 10: '))

print(ListaDeNotas)
print('A nota Máxima é: ', Maximo)
print('A nota Mínima é: ', Minimo)
