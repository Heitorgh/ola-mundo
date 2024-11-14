lista = []
frase = input('Digite sua frase: ')
frase.split()
qtd = len(frase.split())
lista.append(frase)
pa = input('Digite a palavra que você quer substituir: ')
pn = input('Digite a palavra nova: ')
lista= frase.replace(pa, pn)
frase_inversa = ' '. join(lista.split()[::-1])
cont = input('Digite a letra que você quer contar: ')
cont2 = lista.count(cont)
print('\n--- Resumo das Informações ---')
print(f'Frase original: {frase}')
print(f'a quantidade de palavras é: {qtd}')
print(f'Palavra substituída: {pa} por {pn}')
print(f'Frase após substituição: {lista}')
print(f'Frase invertida (palavras): {frase_inversa}')
if cont2 == 1:
    print(f'a letra {cont} aparece {cont2} vez!')
else:
    print(f'a letra {cont} aparece {cont2} vezes!')
print('\n-------------------------------')


