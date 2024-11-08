# Olá, Mundo
idade = int(input('digite sua idade entre 10 e 19'))
peso = float(input('digite seu peso'))
altura = float(input('digite sua altura em metros'))
sexo = input('digite seu sexo')
imc = peso/(altura*altura)
while sexo == 'masculino':
    if idade == 10:
        if imc < 14.42:
            print('baixo peso')
        elif  14.42 <= imc < 19.60:
            print('peso adequado')
        elif imc >= 19.60:
            print('sobrepeso')
    if idade == 11:
        if imc < 14.83:
            print('baixo peso')
        elif  14.83 <= imc < 20.35:
            print('peso adequado')
        elif imc >= 20.35:
            print('sobrepeso')
    if idade == 12:
        if imc < 15.24:
            print('baixo peso')
        elif  15.24 <= imc < 21.12:
            print('peso adequado')
        elif imc >= 21.12:
            print('sobrepeso')   
    if idade == 13:
        if imc < 15.73:
            print('baixo peso')
        elif  15.73 <= imc < 21.93:
            print('peso adequado')
        elif imc >= 21.93:
            print('sobrepeso')   
    if idade == 14:
        if imc < 16.18:
            print('baixo peso')
        elif  16.18 <= imc < 22.77:
            print('peso adequado')
        elif imc >= 22.77:
            print('sobrepeso')
    if idade == 15:
        if imc < 16.59:
            print('baixo peso')
        elif  16.59 <= imc < 23.63:
            print('peso adequado')
        elif imc >= 23.63:
            print('sobrepeso')
    if idade == 16:
        if imc < 17.01:
            print('baixo peso')
        elif  17.01 <= imc < 24.45:
            print('peso adequado')
        elif imc >= 24.45:
            print('sobrepeso')
    if idade == 17:
        if imc < 17.31:
            print('baixo peso')
        elif  17.31 <= imc < 25.28:
            print('peso adequado')
        elif imc >= 25.28:
            print('sobrepeso')
    if idade == 18:
        if imc < 17.54:
            print('baixo peso')
        elif  17.54 <= imc < 25.95:
            print('peso adequado')
        elif imc >= 25.95:
            print('sobrepeso')
    if idade == 19:
        if imc < 17.80:
            print('baixo peso')
        elif  17.80 <= imc < 26.36:
            print('peso adequado')
        elif imc >= 26.36:
            print('sobrepeso')
    break
while sexo == 'feminino':
    if idade == 10:
        if imc < 14.23:
            print('baixo peso')
        elif  14.23 <= imc < 20.19:
            print('peso adequado')
        elif imc >= 20.19:
            print('sobrepeso')
    if idade == 11:
        if imc < 14.60:
            print('baixo peso')
        elif  14.60 <= imc < 221.18:
            print('peso adequado')
        elif imc >= 21.18:
            print('sobrepeso')
    if idade == 12:
        if imc < 14.98:
            print('baixo peso')
        elif  14.98 <= imc < 22.17:
            print('peso adequado')
        elif imc >= 22.17:
            print('sobrepeso')
    if idade == 13:
        if imc < 15.36:
            print('baixo peso')
        elif  15.36 <= imc < 23.08:
            print('peso adequado')
        elif imc >= 23.08:
            print('sobrepeso')
    if idade == 14:
        if imc < 15.67:
            print('baixo peso')
        elif  15.67 <= imc < 23.88:
            print('peso adequado')
        elif imc >= 23.88:
            print('sobrepeso')
    if idade == 15:
        if imc < 16.01:
            print('baixo peso')
        elif  16.01 <= imc < 24.29:
            print('peso adequado')
        elif imc >= 24.29:
            print('sobrepeso')
    if idade == 16:
        if imc < 16.37:
            print('baixo peso')
        elif  16.37 <= imc < 24.74:
            print('peso adequado')
        elif imc >= 24.74:
            print('sobrepeso')
    if idade == 17:
        if imc < 16.59:
            print('baixo peso')
        elif  16.59 <= imc < 25.23:
            print('peso adequado')
        elif imc >= 25.23:
            print('sobrepeso')
    if idade == 18:
        if imc < 16.71:
            print('baixo peso')
        elif  16.71 <= imc < 25.56:
            print('peso adequado')
        elif imc >= 25.56:
            print('sobrepeso')
    if idade == 19:
        if imc < 16.87:
            print('baixo peso')
        elif  16.87 <= imc < 25.85:
            print('peso adequado')
        elif imc >= 25.85:
            print('sobrepeso')
    break