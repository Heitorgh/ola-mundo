lista = []
frase = input('Digite sua frase: ')
lista.append(frase)
print(lista)
pa = input('Digite a palavra que você quer substituir: ')
pn = input('Digite a palavra nova: ')
lista= frase.replace(pa, pn)
print(lista)

