#IF - ELIF - ELSE

# OPERADORES RELACIONAIS
# > maior
# >= maior ou igual
# < menor
# <= menor ou igual 
# == igual 
# != diferente

# OPERADORES LÓGICOS
# not: negação/inversão
# and: conjunção (e)
# or: disjunção (ou)

print("----- SISTEMA DE NOTAS -----")

nota1 = float(input("Nota N1: "))
nota2 = float(input("Nota N2: "))
media = float()

media = (nota1 + nota2) / 2

# Em Python é muito importatnte a indentação (espaçamento), fique atento.
if media >= 7.0 and media < 10.0:
    print(f"\nA media final do aluno e: {media}")
    print("Aluno aprovado!")
elif media < 7.0 and media >= 3.0:
    print(f"\nA media final do aluno e: {media}")
    print("Aluno em recuperacao!")
elif media < 3.0 and media >= 0.0:
    print(f"\nA media final do aluno e: {media}")
    print("Aluno reprovado!")
else:
    print("\nNota inexistente!")

print("----------------------------")