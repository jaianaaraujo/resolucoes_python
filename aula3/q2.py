""" Lê uma lista de números inteiros e a retorna sem os números repetidos. """

tam_lista = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(tam_lista):
    lista.append(int(input("Digite um elemento: ")))
nova_lista = []

for numero in lista:
    if numero not in nova_lista:
        nova_lista.append(numero)

print("Sem números repetidos : ", nova_lista)