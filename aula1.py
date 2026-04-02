# SAÍDA DE DADOS---------------------------------------------------------------------------------

num2 = float(25.12345)
num = int(100)

print("\n-------------------------------------")

# OBS: F-string formata variaveis dentro da string
print(f"valor com casas decimais: {num2:.2f}", end='') #eu especifico quantos casas usando 2f (3f, 4f...)

print(f"\nvalor em decimal: {num: d}", end='') #formata num para decimal

print(f"\nvalor em binario: {num: b}", end='') #formata num para binário

#OBS: o end='' é usado para evitar a quebra de linha após a impressão.

print("\n-------------------------------------")

# ENTRADA DE DADOS--------------------------------------------------------------------------------

print("\nDADOS PESSOAIS")

nome = input("\nDigite seu nome: ") #input é usado para receber dados do usuário
idade = int(input("Informe sua idade: "))
tel = int(input("Informe seu telefone: "))

#OBS: o input sempre retorna uma string, então é necessário converter para o tipo desejado (int, float, etc)

print(f"\nSeu nome é {nome},", f"voce tem {idade} anos,", f"e seu telefone é {tel}", end='')

print("\n-------------------------------------\n")

#VARIÁVEIS E TIPOS DE DADOS-----------------------------------------------------------------------

print("INFORME OUTROS DADOS\n")

num3 = int(input("Quantos anos de experiência você tem? ")) #variável do tipo inteiro
pet = str(input("Qual o nome do seu pet? ")) #variável do tipo string, texto
dinheiro = float(input("Quanto tem em dinheiro? ")) #número com casas decimais
solteiro = True #tipo booleano, pode ser True ou Falso

print("\n-------------------------------------")

print(f"\nSEUS DADOS SÃO:\n\n"
      f"NOME: {nome}\n"
      f"IDADE: {idade}\n"
      f"TELEFONE: {tel}"
      f"ANOS DE EXPERIENCIA: {num3}\n"
      f"NOME DO PET: {pet}\n"
      f"SOLDO EM CONTA: {dinheiro}")

print("-------------------------------------\n")