alunos = []
notasG1 = []
notasG2 = []
frequencias = []
passou = []
nao_passou_por_frequencia = []
fez_af_e_passou = []
fez_af_e_reprovou = []

def calculo_media(nota1, nota2):
    return (nota1 + nota2 * 2) / 3

def input_aluno():
    aluno = input('Digite o nome do aluno (digite SAIR para encerrar): ')
    return aluno

def input_notas_frequencia():
    notaG1 = float(input('Digite sua nota da G1: '))
    notaG2 = float(input('Digite sua nota da G2: '))
    frequencia = int(input('Digite a frequencia do aluno: '))
    return notaG1, notaG2, frequencia

def process_aluno(aluno, notaG1, notaG2, frequencia):
    resultado = calculo_media(notaG1, notaG2)
    
    if resultado >= 6.0:
        passou.append(aluno)
    elif resultado < 6.0 and frequencia >= 75:
        notaAF = float(input('Digite a nota da AF: '))
        resultado2 = calculo_media(notaAF, resultado)
        if resultado2 >= 6:
            fez_af_e_passou.append(aluno)
        else:
            fez_af_e_reprovou.append(aluno)
    elif frequencia < 75:
        nao_passou_por_frequencia.append(aluno)

while True:
    aluno = input_aluno()
    
    if aluno == 'SAIR':
        break

    notas = input_notas_frequencia()
    
    alunos.append(aluno)
    notasG1.append(notas[0])
    notasG2.append(notas[1])
    frequencias.append(notas[2])
    
    process_aluno(aluno, notas[0], notas[1], notas[2])

# Final Output
print(f'Os alunos mostrados foram: {alunos}')
print(f'Os alunos que passaram direto foram: {passou}')
print(f'Os alunos que nao passaram pois nao atingiram 75% de frequencia foram: {nao_passou_por_frequencia}')
print(f'Os alunos que fizeram a AF e passaram foram: {fez_af_e_passou}')
print(f'Os alunos que fizeram a AF e nao passaram foram: {fez_af_e_reprovou}')
print(f'Total de notas G1: {notasG1}')
print(f'Total de notas G2: {notasG2}')
print(f'Total de frequencias dos alunos da Ulbra Palmas: {frequencias}')
