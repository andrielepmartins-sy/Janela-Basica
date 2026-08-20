notas = []

for i in range(3):
    nome = input("Digite o nome do seu aluno:").strip()
    nota = float(input("Digite a nota do seu aluno:"))
    notas.append(nota)


def calcular_media(notas):

    media = sum(notas) / len(notas)
    return media


media = calcular_media(notas)

print(f"\nMédia da turma: {media:.2f}")

maior = max(notas)

print(f"A maior nota: {maior}")

menor = min(notas)

print(f"A menor nota: {menor}")



