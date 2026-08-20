# ============================================================
# 🐍 COLA PYTHON — PROVA
# Tudo aqui funciona no TERMINAL
# ============================================================


# ============================================================
# 1. PRINT
# ============================================================

print("Olá mundo!")

nome = "Mit"
idade = 17

print("Nome:", nome)
print("Idade:", idade)

# f-string
print(f"Meu nome é {nome} e tenho {idade} anos.")


# ============================================================
# 2. INPUT
# ============================================================

# input() SEMPRE recebe texto
nome = input("Digite seu nome: ")

# Número inteiro
idade = int(input("Digite sua idade: "))

# Número decimal
altura = float(input("Digite sua altura: "))

# Converter para texto
numero = 123
texto = str(numero)


# ============================================================
# 3. OPERADORES MATEMÁTICOS
# ============================================================

a = 10
b = 3

print(a + b)   # SOMA
print(a - b)   # SUBTRAÇÃO
print(a * b)   # MULTIPLICAÇÃO
print(a / b)   # DIVISÃO
print(a // b)  # DIVISÃO INTEIRA
print(a % b)   # RESTO
print(a ** b)  # POTÊNCIA


# ============================================================
# 4. COMPARAÇÕES
# ============================================================

# ==  igual
# !=  diferente
# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual

idade = 18

print(idade == 18)
print(idade >= 18)


# ============================================================
# 5. IF / ELIF / ELSE
# ============================================================

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")

elif idade >= 16:
    print("Tem 16 ou 17 anos")

else:
    print("Menor de idade")


# ============================================================
# 6. AND / OR / NOT
# ============================================================

idade = 20

# AND → as duas condições precisam ser verdadeiras
if idade >= 18 and idade <= 60:
    print("Está entre 18 e 60")

# OR → pelo menos uma condição verdadeira
if idade < 18 or idade > 60:
    print("Não está entre 18 e 60")

# NOT → inverte True/False
if not idade == 10:
    print("A idade não é 10")


# ============================================================
# 7. FOR
# ============================================================

for i in range(5):
    print(i)

# Resultado:
# 0
# 1
# 2
# 3
# 4


# Começar em 1 e terminar em 5
for i in range(1, 6):
    print(i)

# range(início, fim)
# O último número NÃO entra!


# De 2 em 2
for i in range(0, 11, 2):
    print(i)

# 0, 2, 4, 6, 8, 10


# ============================================================
# 8. WHILE
# ============================================================

contador = 0

while contador < 5:
    print(contador)
    contador += 1

# CUIDADO:
# Se a condição nunca ficar False,
# o while vira um loop infinito!


# ============================================================
# 9. BREAK
# ============================================================

while True:

    nome = input("Digite seu nome (ou sair): ")

    if nome == "sair":
        break

    print(f"Olá, {nome}!")

# break → para o loop


# ============================================================
# 10. CONTINUE
# ============================================================

for i in range(10):

    if i == 5:
        continue

    print(i)

# continue → pula aquela repetição


# ============================================================
# 11. LISTAS
# ============================================================

nomes = ["Ana", "João", "Maria"]

print(nomes)

print(nomes[0])  # Ana
print(nomes[1])  # João
print(nomes[2])  # Maria

# Último elemento
print(nomes[-1])

# A primeira posição é 0!


# ============================================================
# 12. APPEND
# ============================================================

nomes = []

nomes.append("Ana")
nomes.append("João")
nomes.append("Maria")

print(nomes)

# append() → adiciona no final


# ============================================================
# 13. REMOVE
# ============================================================

nomes = ["Ana", "João", "Maria"]

nomes.remove("João")

print(nomes)

# remove() → remove pelo VALOR


# ============================================================
# 14. LEN
# ============================================================

nomes = ["Ana", "João", "Maria"]

quantidade = len(nomes)

print(quantidade)

# len() → quantidade de elementos


# ============================================================
# 15. SUM
# ============================================================

numeros = [10, 20, 30, 40]

total = sum(numeros)

print(total)

# sum() → soma os números


# ============================================================
# 16. MÉDIA
# ============================================================

notas = [7, 8, 9, 10]

soma = sum(notas)
quantidade = len(notas)

media = soma / quantidade

print(f"Média: {media:.2f}")


# ============================================================
# 17. PERCORRER UMA LISTA
# ============================================================

nomes = ["Ana", "João", "Maria"]

for nome in nomes:
    print(nome)


# ============================================================
# 18. FUNÇÕES
# ============================================================

def saudacao():
    print("Olá!")

saudacao()


# ============================================================
# 19. FUNÇÃO COM PARÂMETRO
# ============================================================

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Mit")
saudacao("Ana")


# ============================================================
# 20. RETURN
# ============================================================

def somar(a, b):

    resultado = a + b

    return resultado


resultado = somar(10, 5)

print(resultado)

# return → devolve um valor
# print() → mostra na tela


# ============================================================
# 21. FUNÇÃO COM CÁLCULO
# ============================================================

def calcular_media(nota1, nota2):

    media = (nota1 + nota2) / 2

    return media


media = calcular_media(8, 10)

print(f"Média: {media:.2f}")


# ============================================================
# 22. VALOR PADRÃO
# ============================================================

def saudacao(nome="Visitante"):

    print(f"Olá, {nome}!")


saudacao("Mit")
saudacao()


# ============================================================
# 23. STRIP
# ============================================================

nome = input("Nome: ").strip()

# strip() → remove espaços do começo e do final


# ============================================================
# 24. LOWER / UPPER
# ============================================================

nome = input("Nome: ")

print(nome.lower())
print(nome.upper())

# lower() → minúsculas
# upper() → MAIÚSCULAS


resposta = input("Continuar? ").lower()

if resposta == "sim":
    print("Continuando...")


# ============================================================
# 25. IN
# ============================================================

nomes = ["Ana", "João", "Maria"]

if "Ana" in nomes:
    print("Ana está na lista")


nome = "Maria"

if "a" in nome.lower():
    print("Tem a letra A")


# ============================================================
# 26. ARQUIVOS — LER
# ============================================================

# "r" = read = ler

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:

    conteudo = arquivo.read()

print(conteudo)


# ============================================================
# 27. ARQUIVOS — ESCREVER
# ============================================================

# "w" = write = escrever
# ATENÇÃO: w pode apagar o conteúdo anterior!

with open("arquivo.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("Olá!\n")
    arquivo.write("Python é legal!")


# ============================================================
# 28. ARQUIVOS — ADICIONAR
# ============================================================

# "a" = append = adicionar

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:

    arquivo.write("\nNova linha!")


# ============================================================
# 29. LER ARQUIVO LINHA POR LINHA
# ============================================================

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        print(linha.strip())


# ============================================================
# 30. TRY / EXCEPT
# ============================================================

try:

    idade = int(input("Digite sua idade: "))

except ValueError:

    print("Digite apenas números!")


# ============================================================
# 31. CONTADOR
# ============================================================

contador = 0

for i in range(5):

    contador += 1

print(contador)


# ============================================================
# 32. ACUMULADOR
# ============================================================

total = 0

for i in range(5):

    numero = int(input("Digite um número: "))

    total += numero

print(f"Total: {total}")


# ============================================================
# 33. MAIOR NÚMERO
# ============================================================

numeros = [10, 25, 7, 40, 15]

maior = max(numeros)

print(maior)


# ============================================================
# 34. MENOR NÚMERO
# ============================================================

numeros = [10, 25, 7, 40, 15]

menor = min(numeros)

print(menor)


# ============================================================
# 35. ESTRUTURA BÁSICA
# ============================================================

# 1. RECEBER

nome = input("Nome: ")
idade = int(input("Idade: "))


# 2. PROCESSAR

if idade >= 18:

    resultado = "Maior de idade"

else:

    resultado = "Menor de idade"


# 3. MOSTRAR

print(f"{nome}: {resultado}")


# ============================================================
# 🔥 MODELO — MÉDIA DE VÁRIAS NOTAS
# ============================================================

notas = []

for i in range(3):

    nota = float(input("Digite a nota: "))

    notas.append(nota)


media = sum(notas) / len(notas)

print(f"Média: {media:.2f}")


# ============================================================
# 🔥 MODELO — MÉDIA + APROVAÇÃO
# ============================================================

notas = []

for i in range(3):

    nota = float(input("Digite a nota: "))

    notas.append(nota)


media = sum(notas) / len(notas)


if media >= 7:

    print(f"Média: {media:.2f}")
    print("Aprovado!")

else:

    print(f"Média: {media:.2f}")
    print("Reprovado!")


# ============================================================
# 🔥 MODELO — MAIOR E MENOR
# ============================================================

numeros = []

for i in range(5):

    numero = int(input("Digite um número: "))

    numeros.append(numero)


print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")


# ============================================================
# 🔥 MODELO — CONTAR
# ============================================================

contador = 0

for i in range(5):

    numero = int(input("Digite um número: "))

    if numero > 10:

        contador += 1


print(f"Quantidade maior que 10: {contador}")


# ============================================================
# 🔥 MODELO — SOMAR
# ============================================================

total = 0

for i in range(5):

    numero = int(input("Digite um número: "))

    total += numero


print(f"Total: {total}")


# ============================================================
# 🔥 MODELO — FUNÇÃO + LISTA + MÉDIA
# ============================================================

def calcular_media(notas):

    return sum(notas) / len(notas)


notas = []

for i in range(3):

    nota = float(input("Digite a nota: "))

    notas.append(nota)


media = calcular_media(notas)

print(f"Média: {media:.2f}")


# ============================================================
# 🚨 LEMBRETES
# ============================================================

# input()       → recebe TEXTO
# int()         → INTEIRO
# float()       → DECIMAL
# str()         → TEXTO
#
# =             → ATRIBUI
# ==            → COMPARA
# !=            → DIFERENTE
# >             → MAIOR
# <             → MENOR
# >=            → MAIOR OU IGUAL
# <=            → MENOR OU IGUAL
#
# if            → condição
# elif          → outra condição
# else          → caso contrário
#
# for           → repetição
# while         → repetição
# break         → PARA
# continue      → PULA
#
# []            → lista
# append()      → adiciona
# remove()      → remove
# len()         → quantidade
# sum()         → soma
# max()         → maior
# min()         → menor
#
# def           → cria função
# return        → devolve valor
#
# .strip()      → remove espaços
# .lower()      → minúsculas
# .upper()      → MAIÚSCULAS
#
# in            → verifica se está dentro
#
# open()        → abre arquivo
# "r"           → ler
# "w"           → escrever
# "a"           → adicionar


# ============================================================
# 🧠 MODELO MENTAL
# ============================================================

# 1. O que o usuário precisa DIGITAR?
#    ↓
#    input()
#
# 2. É número?
#    ↓
#    int() ou float()
#
# 3. Precisa tomar uma DECISÃO?
#    ↓
#    if / elif / else
#
# 4. Precisa REPETIR?
#    ↓
#    for ou while
#
# 5. Precisa guardar VÁRIOS valores?
#    ↓
#    lista []
#
# 6. Precisa ADICIONAR valores?
#    ↓
#    append()
#
# 7. Precisa CONTAR?
#    ↓
#    contador += 1
#
# 8. Precisa SOMAR?
#    ↓
#    total += numero
#
# 9. Precisa calcular MÉDIA?
#    ↓
#    sum(lista) / len(lista)
#
# 10. Precisa reutilizar código?
#     ↓
#     def + return
#
# ============================================================
# 🐍 FIM DA COLA
# ============================================================