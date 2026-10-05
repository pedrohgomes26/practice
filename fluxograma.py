import json

# 1. Abrir Diário de Classe
with open("diario.json", "r", encoding="utf-8") as arquivo:
    turma = json.load(arquivo)

# Loop: "Há mais alunos na turma?" -> "Selecionar o próximo aluno da lista"
for aluno in turma:
    nome = aluno["nome"]

    # 2. Calcular Média e % de Presença
    media = sum(aluno["notas"]) / len(aluno["notas"])
    pct_presenca = (aluno["aulas_presentes"] / aluno["total_aulas"]) * 100

    # 3. Presença >= 75%?
    if pct_presenca < 75:
        status = "Reprovado por Falta"
    else:
        # 4. Média >= 7?
        if media >= 7:
            status = "Aprovado"
        else:
            status = "Exame de Recuperação"

    # Exibe o resultado do aluno processado
    print(
        f"Aluno: {nome:<12} | Média: {media:.1f} | Presença: {pct_presenca:.0f}% | Status: {status}"
    )

# Quando o loop encerra (Não há mais alunos na turma)
print("\nConcluído")