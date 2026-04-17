soma = 0
print("Digite as notas de 10 alunos:")
for i in range(1, 11):
    nota = float(input(f"Nota do aluno {i}: "))
    soma += nota

media = soma / 10
print(f"\nMédia da turma: {media:.2f}")
