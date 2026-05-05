# STRINGS (DADOS DO TIPO TEXTO/STR)

# A MAIORIA DAS OPERAÇÕES QUE USAMOS EM LISTAS, TAMBÉM PODEM SER USADAS EM LISTAS

# EXEMPLOS USANDO STRINGS

print("\n----- CADASTRO DE NOME -----")
nome1 = input("Informe seu primeiro nome: ")
nome2 = input("Informe seu sobrenome: ")


print("\n\n----- OPERAÇOES COM SEU NOME -----")
comp_nome = len(nome1) #len() mostra o tamanho da lista
comp_sobrenome = len(nome2)
print(f"seu nome possui {comp_nome} letras")
print(f"seu sobrenome possui {comp_sobrenome} letras\n")


print("\nCONCATENACAO DE STRING ----------")
nome_completo = nome1 + " " + nome2 #concatenação: <str1> + <str2> - colar duas variaveis strings
print(f"e seu nome completo é {nome_completo}\n")


print("\nREPETICAO DE STRING ----------")
espaco_nome = nome1 + " "
repeticao_nome = espaco_nome * 10 # repetição: <str1> * <qtde> - quantas vezes eu quero que uma string apareça
print(repeticao_nome,"\n")


print("\nINDEXACAO DE STRING ----------")
indexacao_nome = nome1[1] # indexação: <string> [índice] - acessar um caracterer pelo índice
print(f"acessando letra do nome pelo indice: {indexacao_nome}\n")


print("\nPERTENCIMENTO DE STRING ----------")
nome3 = "maria"
nome_completo2 = "maria, eduarda, angelica, sofia, daniely, fernanda"

print(f"NOME ALEATORIO: {nome3}")
print(f"LISTA DE NOMES: {nome_completo2}")
print(f"o nome {nome3} esta na lista de nomes?")
if "maria" in nome_completo2: # pertencimento: if <substring> in <string> - se uma substring pertence a um texto maior
    print("ESTA SIM\n")
else:
    print("NÃO ESTA\n")
#OBS: pode procurar palavras, pedaços de uma palavras e até letras. atente-se a caracteres maiúsculos e minúsculos


print("\nIGUALDADE DE STRING ----------")
nome4 = "pedro"
nome5 = "pedro"
nome6 = "clara"
nome7 = "rosa"
print(f"o nome '{nome4}' e igual ao nome '{nome5}'")
print(nome4 == nome5)# igualdade: <str1> == <str2> - compara duas strings, e vê se são iguais
print(f"o nome '{nome6}' e igual ao nome '{nome7}'")
print(nome6 == nome7)


print("\n\nUSANDO UPPER ----------")
nome8 = "eduardo"
print(f"Nome original: {nome8}")
#nome_maiusculo = nome8.upper() - caso eu não queira transformar a variavel original em maiúsculo
print(f"Nome com upper {nome8.upper()},\n")#upper() - transforma tudo em maiúsculo


print("\nUSANDO LOWER ----------")
nome9 = "PEDRO"
print(f"Nome original: {nome9}")
print(f"Nome com lower: {nome9.lower()}\n")#lower() - trasforma tudo em minúsculo
#OBS: não altera a string, apenas deixa em Maiúsculo para uma situação


print("\nUSANDO STRIP ----------")
#bastante útil para usar com input
nome10 = "    Carlos Vincius Lopes    "
#usuario = input("Digite seu nome: ").strip() - caso queira usar com input
print(f"Nome original: {nome10}")
print(f"Nome sem espacos: {nome10.strip()}\n")#strip() - corta os espaços escedentes na string
#OBS: corta os espaços das bordas não do meio
#OUTRAS VARIAÇOES DO STRIP
#lstrip() - quebra os espaços da esquerda
#rstrip() - quebra os espaços da direita


print("\nUSANDO REPLACE ----------")
#Muito usado para limpeza de dados, correções e formatação.
nome11 = "Carlos Lopes"
print(f"Nome original: {nome11}")
nome12 = nome11.replace("Lopes", "Freitas")#replace(<str1>,<str2>) - substitui uma string por outra
print(f"Nome depois do replace: {nome12}\n")
#str1 = o que você quer encontrar
#str2 = o que vai entrar no lugar


print("\nUSANDO SPLIT ----------")
#transformando texto em lista.
#split(<separador>) - separa a string de acordo com o separador
nome13 = "Daniely e Dantas"
#print(texto.split("-", 2)) - você pode controlar a quantidade de quebras
palavras = nome13.split(" ")#split(<separador>) - separa a string de acordo com o separador (eu defino o tipo de separador. poder ser , ou 1 ou =...)
print(palavras)
print("\n")


print("\nUSANDO JOIN ----------")
#bom para criar lista, conforme dados são adicionados
#join(<itrerável>)
frase1 = ["só", "sei", "que", "nada", "sei"]
print(f": {frase1}")
frase2 = " ".join(frase1)# posso usar qualquer separador: " ","-","."
print(frase2)
print("\n")
#OBS: todos os elementos precism ser string


print("\nUSANDO STARTSWITH ----------")
#startswith(<prefixo>) verifica se uma string COMEÇA com um determinado prefixo.
nome14 = "Rosangela"
nome15 = "Iarley"
print(f"O nome Rosangela começa com R: {nome14.startswith("R")}")
print(f"O nome Iarley começa com P: {nome14.startswith("P")}\n")
#OBS: Sensível a minúsculo e maiúsculo


print("\nUSANDO ENDSWITH ----------")
#endswith(<sufixo>) verifica se uma string TERMINA com um determinado prefixo.
nome16 = "Camilly"
nome17 = "Batista"
print(f"O nome Camilly termina com y: {nome16.endswith("y")}")
print(f"O nome Batista termina com p: {nome17.endswith("p")}\n")
#OBS: Sensível a minúsculo e maiúsculo


print("\nUSANDO FIND ----------")
#find(<substring>) serve para procurar uma substring dentro de uma string e dizer em que posição ela aparece.
frase3 = "ok i pull up"
print(f"frase: {frase3}")
print(f"Em qual posição está a letra 'u': {frase3.find("u")}") #frase3.find("l", 2)
print(f"Em qual posição está a letra 'x': {frase3.find("x")}\n")
# -1, é quando a subtring não está na string, não existe
#OBS: não escontra palavras "pull", apenas caracteres únicos
#e é sempre a primeira ocorrencia, se tiver mais de um 'a', ele encontra apenas o pirmeiro


print("\nUSANDO COUNT ----------")
#count(<substring>) “quantas vezes essa substring aparece aqui?”
frase4 = "bananada de banana"
print(frase4)
print(f"Quantas letras 'a' tem na frase: {frase4.count("a")}")
print(f"Quantas letras 'x' tem na frase: {frase4.count("x")}\n")
#OBS: funciona tanto com caracteres quanto com palavras


print("\nUSANDO ISALPHA ----------")
#isalpha() verifica se todos os caracteres da string são LETRAS
#bom para usar com if else, para inserir apenas letras
frase5 = "python"
frase6 = "python17"
print(f"Todas os caracteres de '{frase5}' sao letras: {frase5.isalpha()}")
print(f"Todas os caracteres de '{frase6}' sao letras: {frase6.isalpha()}\n")
#OBS: ' ' ! espaço e símbolos são considerados caracter, então se tiver espaço ele vai retornar False, por não ser letra
#OBS: aceita letras com acentos "ação"


print("\nUSANDO ISDIGIT ----------")
#isdigit()verifica se todos os caracteres da string são NUMEROS
frase7 = "12345"
frase8 = "python17"
print(f"Todos os caracteres de '{frase7}' sao numeros: {frase7.isdigit()}")
print(f"Todos os caracteres de '{frase8}' sao numeros: {frase8.isdigit()}\n")
#OBS: tem que ser caracter, se for 'int' o programa não vai reconhecer
#OBS: as mesmas condições do isaplha se aplicam aqui


print("\nUSANDO ISALNUM ----------")
#isalnum() verifica se todos os caracteres da string são NUMEROS E/OU LETRAS
frase9 = "carlos1234"
frase10 = "carlos.1234-"
print(f"A frase '{frase9}' possui apenas letras e numeros: {frase9.isalnum()}")
print(f"A frase '{frase10}' possui apenas letras e numeros: {frase10.isalnum()}\n")
#OBS: as mesmas condiçoes do isdigit se aplicam aqui