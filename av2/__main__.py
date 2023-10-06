import get_dataframes
import pandas as pd
import relatorios
import sys
import write_to_excel

equipe = 1
try:
    _equipe = int(sys.argv[1])
    if 1 <= _equipe <= 10:
        equipe = _equipe
except:
    print("Equipe não especificada. Por padrão, a equipe foi definida como 1.\n")

alunos = get_dataframes.alunos(equipe)
dengue = get_dataframes.dengue(equipe)
onibus = get_dataframes.onibus(equipe)

print(f"GERANDO RELATÓRIOS DA EQUIPE {equipe}\n")
print("RELATÓRIO 1")
relatorio1 = relatorios.relatorio1(alunos, dengue)
print(f"Colunas do DataFrame resultante: {tuple(relatorio1['DataFrame'].columns)}")
print(f"Número de alunos: {len(alunos)}, Número de dengues: {len(dengue)}")
print(f"Número de alunos que não tiveram dengue: {len(relatorio1['DataFrame'])}")

if '-w' in sys.argv:
    write_to_excel.write(relatorio1['DataFrame'], f'relatorio_equipe{equipe}.xlsx', sheet_name=relatorio1['Nome'])
