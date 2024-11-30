Maximo = 0
Minimo = 10
SDN = 0
NN = 0
SQ = 0


Notas = float(input('Entre com uma nota de 0 a 10: '))

while 0 <= Notas <= 10 :
    SDN += Notas
    NN += 1
    SQ += Notas **2


    if Notas > Maximo:
    
        Maximo = Notas

    if Notas < Minimo:

        Minimo = Notas
    


    Notas = float(input('Entre com outra nota de 0 a 10: '))

if NN > 0:
    Media = SDN / NN

    V = (SQ / NN) - (Media ** 2)

    DP = V ** 0.5 
 
print(f'Soma das Notas: {SDN}')
print(f'Número de Notas: {NN}')
print(f'A média dos alunos é: {Media:.2f}')
print(f'A nota Máxima é: {Maximo}')
print(f'A nota Mínima é: {Minimo}')
print(f'O desvio padrão é: {DP:.2f}')
