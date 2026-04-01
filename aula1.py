# AULA 1 - FUNDAMENTOS

# saída de dados---------------------------------------------------------------------------------

num2 = float(25.12345)
num = int(100)

print("\n-------------------------------------")

# OBS: F-string formata variaveis dentro da string
print(f"valor com casas decimais: {num2:.2f}", end='') #eu especifico quantos casas usando 2f (3f, 4f...)

print(f"\nvalor em decimal: {num: d}", end='') #formata num para decimal

print(f"\nvalor em binario: {num: b}", end='') #formata num para binário

#OBS: o end='' é usado para evitar a quebra de linha após a impressão.

print("\n-------------------------------------")

# entrada de dados--------------------------------------------------------------------------------

print("DADOS PESSOAIS")

nome = input("\nDigite seu nome: ") #input é usado para receber dados do usuário
idade = int(input("Informe sua idade: "))
tel = int(input("Informe seu telefone: "))

#OBS: o input sempre retorna uma string, então é necessário converter para o tipo desejado (int, float, etc)

print(f"\nSeu nome é {nome},", f"voce tem {idade} anos,", f"e seu telefone é {tel}", end='')

print("\n-------------------------------------\n")

#variáveis e tipos de dados-----------------------------------------------------------------------

