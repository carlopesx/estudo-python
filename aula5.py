# LISTAS (LISTS)

# o primeiro elemento sempre será ZERO

# EXEMPLOS DE OPERAÇÕES MAIS USADAS
print("\n------ LISTAS E OPERAÇÕES COM LISTAS ------\n")

print("----------------------------------------------")
lista1 = [1, 2, 3, 4, 5]
print(f"elementos da lista: {lista1}")
print(f"elemento da posicao 1º da lista: {lista1[1]}")# imprimindo elemento da posição 1, que é 2
print("----------------------------------------------\n")


print("\n------------- USANDO APPEND ----------------")
lista2 = []
for i in range(5):
    dado = int(input("Elemento: "))
    lista2.append(dado)# append(<elemento>) - pendura um elemento no fim da lista
print(f"Os elementos da lista: {lista2}")
print("----------------------------------------------\n")


print("\n------------- USANDO SUM -------------------")
lista3 = [1, 3, 5, 7, 9]
print(f"elementos da lista: {lista3}")
somalista = sum(lista3)# sum() - mostra o somatório dos elementos da lista (numéricos)
#somalista = sum(list2, 5) - soma os elemetos da lista + 5
print(f"A soma dos elementos e: {somalista}")
print("----------------------------------------------\n")


print("\n------------- USANDO LEN -------------------")
# len() - mostra o tamanho da lista
lista4 = [2, 4, 6, 8, 10]
print(f"lista: {lista4}")
print(f"a lista possui {len(lista4)} elementos")
print("----------------------------------------------\n")


print("\n------------- USANDO REVERSE ---------------")
lista5 = [1, 2, 3, 4, 5, 6]
print(f"lista original: {lista5}")
# inverso = reversed(list2) - cria uma versão invertida sem alterar a original
lista5.reverse()
print(f"lista invertida: {lista5}\n")
# OBS: só funciona com números, palavras usa "v2 = v1[::-1]"
palavra = "lopes"
print(f"palavra: {palavra}")
inver = palavra[::-1]
print(f"palavra invertida: {inver}")
print("----------------------------------------------\n")


print("\n------------- USANDO SORT-------------------")
lista6 = [4, 6, 1 ,9, 3]
print(f"ordem original: {lista6}")
lista6.sort()# sort() - ordena a lista
#numeros.sort(reverse=True) - deixa em ordem decrescente
print(f"ordem ordenada: {lista6}")
# funciona com numeros e textos (texto é em ordem alfabética)
print("----------------------------------------------\n")


print("\n------------- USANDO CLEAR -----------------")
lista7 = [5, 10, 15, 20, 25]
print(f"lista atuat: {lista7}")
lista7.clear()# clear() - limpa a lista
print(f"lista clear: {lista7}")
#OBS: a lista não é deletada, só perde os elementos
print("----------------------------------------------\n")


print("\n------------- USANDO POP -------------------")
lista8 = [9, 4, 6, 1, 0]
lista9 = [9, 4, 6, 1, 0]
print(f"lista: {lista8}")
#valor = lista8.pop() - cria uma lista sem alterar a original
lista8.pop()# pop() - remove o elemento do topo da lista
print(f"lista atual: {lista8}\n")

print(f"lista 2: {lista9}")
valor2 = lista9.pop(1)# pop(<posição>) - remover elemento da posição arbitrária
print(f"elemento removido (indice): {valor2}")
print(f"lista atual: {lista9}")
print("---------------------------------------------\n")


print("\n------------- USANDO COUNT ------------------")
lista10 = [2, 3, 3, 4, 5]
print(lista10)
print("quantas vezes o '3' aparece na lista?:")
print(lista10.count(3))# count(<elemento>) - conta quantas vezes um elemento aparece na lista

nome2 = "banana"
print(f"\npalavra: {nome2}")
print(f"quantas letras: {len(nome2)}")
print(f"quantas letras 'a': {nome2.count("a")}")

print("-----------------------------------------------\n")


print("\n------------- USANDO INDEX ------------------")
# index(<elemento>) - saber a posição de um elemento
lista11 = [2, 3, 4, 5, 6]
print(f"lista: {lista11}")
print(f"posicao do elemento '4': {lista11.index(4)}")
print("-----------------------------------------------\n")


print("\n-------------- USANDO REMOVE -----------------")
# remove(<elemento>) - remover um elemento (remove pelo valor, não pela posição)
lista12 = [4, 6, 8, 1, 2]
print(lista12)
lista12.remove(8)
print(f"removendo o 8 da lista: {lista12}")
print("------------------------------------------------\n")


print("\n-------------- USANDO INSERT -----------------")
# insert(<pos>, <elem>) - iserir elemento em uma posição específica
lista13 = [9, 6, 2, 4, 5]
print(lista13)
lista13.insert(1, 10)
print("inserir o elemento '10' na posicao '1'")
print(lista13)
print("------------------------------------------------\n")


print("\n-------------- USANDO EXTEND -------------------")
# extend(<iterável>) - extender a lista (adicionar vários elementos de uma vez)
lista14 = [1, 2, 3]
mais = [5, 9, 20]
nome3 = ["l", "o", "p"]
print(f"lista original: {lista14}")
print(f"adicionar a lista: {mais}\n")
lista14.extend(mais)
print(f"lista atual: {lista14}")
print("-----------------------")
print(f"nome incompleto: {nome3}")
nome3.extend("es")
print(f"nome completo: {nome3}")
# OBS: só funciona se a palavra estiver em lista, não string
print("------------------------------------------------\n")