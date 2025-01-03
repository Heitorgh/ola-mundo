from time import sleep
# função para que seja lido apenas numeros inteiros na escolha do menu
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero flutuante valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n

#função para criar uma linha oara deicar o menu mais bonito para o usuário
def linha(tam = 42):
    return '-' * tam

# função para fixar a linha no centro
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# função para conseguir organizar o menu 
def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('sua opção: ')
    return opc



while True:
    resposta = menu(['Inserir dados de sensores', 'Exibir resultados de relatórios', 'Salvar relatório', 'Sair'])
    
    if resposta == 1:
        cabeçalho('Opção 1 selecionada: Inserir dados de sensores.')
        # Lista para armazenar os valores
        valores = []

        print("Digite os valores. Quando terminar, digite 'sair'.")

        while True:
            entrada = input("Digite um valor: ")
            
            if entrada.lower() == 'sair':  # Verifica se o usuário quer encerrar
                break
            
            try:
                valor = float(entrada)  # Tenta converter a entrada para número
                valores.append(valor)  # Adiciona o valor à lista
            except ValueError:
                print("Entrada inválida. Por favor, insira um número ou 'sair' para encerrar.")

        print("\nValores digitados:")
        print(valores)

        matriz_tensoes = []

        # Coletar os valores para dois dias consecutivos
        for dia in range(1, 3):  # Dois dias (1 e 2)
            print(f"\nInsira os valores de tensões para o Dia {dia}. Digite 'sair' para finalizar.")
            tensoes_dia = []
            while True:
                entrada = input(f"Tensão para o Dia {dia}: ")
                if entrada.lower() == 'sair':  # Encerra a entrada de dados para o dia
                    break
                try:
                    valor = float(entrada)
                    tensoes_dia.append(valor)  # Adiciona o valor à lista do dia
                except ValueError:
                    print("Valor inválido. Por favor, insira um número ou 'sair' para encerrar.")
            matriz_tensoes.append(tensoes_dia)  # Adiciona a lista do dia à matriz


    elif resposta == 2:
        cabeçalho('Opção 2 selecionada: Exibir resultados de relatórios.')
        # Lista para armazenar os valores
        media = sum(valores) / len(valores)
        minimo = min(valores)
        maximo = max(valores)

        print("\nResultados da Análise:")
        print(f"Valor Médio: {media:.2f}")
        print(f"Valor Mínimo: {minimo:.2f}")
        print(f"Valor Máximo: {maximo:.2f}")

        if maximo > 50:
            print('Alerta! consumo elevado!')
        else:print('Consumo dentro do limite.')

        # Exibir a matriz de tensões
        print("\nMatriz de Tensões Coletadas:")
        for i in range(len(matriz_tensoes)):
            print(f"Dia {i + 1}: {matriz_tensoes[i]}")

        if len(matriz_tensoes[0]) == len(matriz_tensoes[1]):
            soma_sensores = [matriz_tensoes[0][i] + matriz_tensoes [1][i] for i in range(len(matriz_tensoes[0]))]
            print('\nSoma das tensoes de cada sensor ao longo dos 2 dias')
            for i, soma in enumerate(soma_sensores, start=1):
                print(f'sensor {i}: {soma:.2f}')
        else:
            print('Erro: os dois dias possuem números diferentes de sensores')
                
    elif resposta == 3:
        cabeçalho('Opção 3 selecionada: Salvar relatório.')
    elif resposta == 4:
        cabeçalho('Consulta encerrada.')
        break
    else:
        print('\033[31mERRO: Opção inválida. Escolha entre 1 e 4.\033[m')
    sleep(2)
