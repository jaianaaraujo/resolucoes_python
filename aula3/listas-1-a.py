
""" Lê uma lista qualquer e retorna uma lista com os caracteres não númericos
separados ao inicio e na ordem original, e os númericos no final, na ordem inversa. """

tam_lista = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(tam_lista):
    lista.append(input("Digite um elemento: "))

nao_numericos = []
numericos = []

for caractere in lista:
    if caractere.isdigit():
        numericos.append(caractere)
    else:
        nao_numericos.append(caractere)

# adiciona os numericos ao final da lista de não númericos
# em ordem inversa       
nao_numericos.extend(numericos[::-1])

print("Lista formatada: ", nao_numericos)
