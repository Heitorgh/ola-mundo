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
frase_inversa = ' '. join(lista.split()[::-1])
print(frase_inversa)
cont = input('Digite a letra que você quer contar: ')
cont2 = lista.count(cont)
print(cont2)


