# LAÇOS DE REPETIÇÃO

# WHILE --------------------------------------------------------------------------

print("\n----- CONTAGEM DE 1 A 10 (com while) -----")

num = 1 # atribuo um valor na variável

while num <= 10: # While executa conforme a condição (enquanto for menor que 10)
    print(num, end=' ') # Exibe o 'num' na tela
    num += 1 # Operador de atribuição (incrementa 1, evitando o loop infinito)
print("\n-------------------------------------------\n")

# FOR / RANGE() ------------------------------------------------------------------

print("----- CONTAGEM DE 1 A 10 (com for e range) -----")

for i in range(1, 11, 1):
    print(i, " ", end="")
print("\n------------------------------------------------\n")

# QUANDO USAR WHILE OU FOR/RANGE
# 'while' não sei quantas vezes o loop deve repetir, deve parar quando atender uma condição específica
# 'for/range' sei exatamente quantas vezes o loop deve repetir

# TESTE DE MENU USANDO WHILE

opc = int(1)

while opc == 1:

    print("----- MENU -----")
    print("1 - CALCULADORA")
    print("0 - SAIR")
    opc2 = int(input(":"))

    while opc2 == 1:
        divi = float()
        n1 = int(input("\nDigite um numero: "))
        n2 = int(input("Digite outro numero: "))

        soma = n1 + n2
        sub = n1 - n2
        multi = n1 * n2
        divi = n1 / n2

        print (f"\nSoma: {soma}\n"
           f"Subtracao: {sub}\n"
           f"Multiplicacao: {multi}\n"
           f"DIvisao: {divi: .2f}")
        opc2 = int(input("\n1 - continuar\n"
                         "0 - sair: "))
    
    opc = int(input("\n1 - Retornar ao menu\n"
                    "0 - Sair: "))

print("\nAte a proxima ;)")
print("---------------------")