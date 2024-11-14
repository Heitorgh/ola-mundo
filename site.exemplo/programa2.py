lista = []
frase = input('Digite sua frase: ')
frase.split()
qtd = len(frase.split())
lista.append(frase)
print(qtd)
print(lista)
pa = input('Digite a palavra que você quer substituir: ')
pn = input('Digite a palavra nova: ')
lista= frase.replace(pa, pn)
print(lista)


