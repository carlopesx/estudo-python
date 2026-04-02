#EXPRESSÕES ARITIMÉTICAS------------------------------------------------

print("\n----- OPERADORES MATEMÁTICOS -----\n")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(10)
id = float()

soma = num1 + num2
sub = num1 - num2

divi = id #transformando a variável divi em float

mult = num1 * num2
divi = num1 / num2

print(f"\nRESULTADOS\n"
      
      f"\nSOMA: {soma}\n"
      f"SUBTRACAO: {sub}\n"
      f"MULTIPLICACAO: {mult}\n"
      f"DIVISAO: {divi: .2f}\n")

total = float(soma + sub + mult + divi)

print(f"A soma total de todos esses numeros e: {total}\n")

num3 += 1 #num3 = num3 + 1 (11)
print(num3)
num3 -= 1 #num3 = num3 - 1 (10)
print(num3)
num3 *= 2 #num3 = num3 * 2 (20)
print(num3)
num3 /= 2 #num3 = num3 / 1 (10)
print(num3)

print("\n------------------------------------")