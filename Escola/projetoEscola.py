def linha():
    print('=' * 40)

turma = []

while True:
    aluno = dict()
    notas = []

    aluno['nome'] = input('Nome: ')

    while True:
        try:
            tot = int(input(f'Quantas provas o {aluno["nome"]} realizou? '))
            break
        except ValueError:
            print('Digite números inteiros válidos')

    for c in range(tot):
        while True:
            try:
                nota = float(input(f'Nota {c + 1}: '))
                notas.append(nota)
                break
            except ValueError:
                print("Digite um número válido.")

    aluno['notas'] = notas
    aluno['media'] = sum(notas) / len(notas)

    if aluno['media'] >= 60:
        print('Aprovado')
    elif aluno['media'] >= 40:
        print('Recuperação')
    else:
        print('Reprovado')

    turma.append(aluno)

    while True:
        res = input('Deseja continuar [s/n]? ').strip().upper()
        if res and res[0] in 'SN':
            break
        print('ERRO! Responda novamente com S ou N.')

    if res[0] == 'N':
        break

linha()
print(f'{"Matrícula":<10}{"Nome":<15}{"Notas":<25}{"Média":<6}')
linha()
for i, aluno in enumerate(turma):
    print(f'{i:<10}{aluno["nome"]:<15}{str(aluno["notas"]):<25}{aluno["media"]:.2f}')
linha()

# Relatório
while True:
    try:
        inf = int(input('Mostrar os dados de qual aluno? [Digite 99 para sair]: '))
    except ValueError:
        print("Digite um número válido.")
        continue

    if inf == 99:
        break
    if inf >= len(turma) or inf < 0:
        print(f'ERRO! Não existe nenhum aluno com a matrícula {inf}')
    else:
        print(f'\nINFORMAÇÕES SOBRE O ALUNO {turma[inf]["nome"]}')
        for i, nota in enumerate(turma[inf]["notas"]):
            print(f' Na prova {i + 1} tirou nota {nota}')
        print(f' Média final: {turma[inf]["media"]:.2f}')
    linha()

print('<<<< RELATÓRIO DO ALUNO CONCLUÍDO! >>>>')

# Comparação
while True:
    comp = input('Deseja iniciar uma comparação entre os alunos? [s/n]: ').strip().upper()
    if not comp:
        print('Digite S ou N.')
        continue

    if comp[0] == 'N':
        break
    elif comp[0] == 'S':
        try:
            aluno1 = int(input('Digite o código do primeiro aluno: '))
            aluno2 = int(input('Digite o código do segundo aluno: '))

            if aluno1 < 0 or aluno1 >= len(turma) or aluno2 < 0 or aluno2 >= len(turma):
                print('Código(s) inválido(s)!')
                continue

            nome1 = turma[aluno1]["nome"]
            nome2 = turma[aluno2]["nome"]
            media1 = turma[aluno1]["media"]
            media2 = turma[aluno2]["media"]

            print(f'\nComparando {nome1} e {nome2}:')
            print(f'{nome1} - Média: {media1:.2f}')
            print(f'{nome2} - Média: {media2:.2f}')

            if media1 > media2:
                print(f'{nome1} tem média maior.')
            elif media2 > media1:
                print(f'{nome2} tem média maior.')
            else:
                print('Ambos têm a mesma média.')
        except ValueError:
            print('Digite um número válido.')

linha()
print('<<< FIM DO PROGRAMA >>>')
