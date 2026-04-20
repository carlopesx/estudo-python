# MATRIZES (LISTS MULTIDIMENSIONAIS)

matriz = [
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13]
]

# exibindo matriz
for elem in matriz:
    print(elem)

print("\n")

# exibindo matriz de forma "bonita"
for elem in matriz:
    for valor in elem:
        print(valor, end=" ")
    print()

#EXEMPLO USANDO MATRIZ

assentos = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

opc1 = 1
opc2 = 1

while opc1 == 1:
    print("\n----- ASSENTOS DE CINEMA -----")
    opc1 = int(input("1 - escolher assento: \n"
                     "0 - sair: "))
    print("\n")

    while opc2 == 1:
        for linha in assentos:
            print(linha)

        print("\n----- ESCOLHA UM ASSENTO -----")
        linha = int(input("Ecolha uma coluna (0 a 10): "))
        coluna = int(input("escolha uma coluna (0 a 10): "))

        assentos[linha][coluna] = 1


        print("\n")
        for linha in assentos:
            print(linha)

        opc2 = int(input("\n1 - esolher outro assento: \n"
                        "0 - sair: "))