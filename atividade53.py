# Cadastre pares nome e nota (0–10) repetidamente até o usuário digitar fim no nome.
# Ao final:
# mostre a quantidade de alunos;
# a média da turma;
# o melhor e o pior aluno (nome e nota).
# Desconsidere cadastros vazios e valide notas fora do intervalo.

nomes = []
notas = []

while True:
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    
    nomes.append(nome)
    notas.append(nota)

    opcao = input("Deseja continuar? (S/N): ")
    if opcao == 'N':
        break

if notas:
    media = sum(notas) / len(notas)
    melhor_aluno = nomes[notas.index(max(notas))]
    pior_aluno = nomes[notas.index(min(notas))]

    print(f"Quantidade de alunos: {len(nomes)}")
    print(f"Média da turma: {media:.2f}")
    print(f"Melhor aluno: {melhor_aluno} ({max(notas)})")
    print(f"Pior aluno: {pior_aluno} ({min(notas)})")
else:
    print("Nenhum aluno cadastrado.")
