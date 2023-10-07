import get_dataframes
import pandas as pd
import gerar_relatorios
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

relatorios = []

print(f"GERANDO RELATÓRIOS DA EQUIPE {equipe}\n")
print(f"{'RELATÓRIO 1':-^80}")
relatorio1 = gerar_relatorios.relatorio1(alunos, dengue)
relatorios.append(relatorio1)
print(f"Colunas do DataFrame resultante: {tuple(relatorio1['DataFrame'].columns)}")
print(f"Número de alunos: {len(alunos)}, Número de dengues: {len(dengue)}")
print(f"Número de alunos que não tiveram dengue: {len(relatorio1['DataFrame'])}")

print(f"{'RELATÓRIO 2':-^80}")
relatorio2 = gerar_relatorios.relatorio2(dengue, onibus)
relatorios.append(relatorio2)
print(f"Colunas do DataFrame resultante: {tuple(relatorio2['DataFrame'].columns)}")
print(f"Número de pacientes: {len(dengue)}, Número de passageiros: {len(onibus)}")
print(f"Número de pacientes que não utilizam ônibus: {len(relatorio2['DataFrame'])}")
print()

print(f"{'RELATÓRIO 3':-^80}")
relatorio3 = gerar_relatorios.relatorio3(onibus, dengue)
relatorios.append(relatorio3)
print(f"Colunas do DataFrame resultante: {tuple(relatorio3['DataFrame'].columns)}")
print(f"Número de passageiros: {len(onibus)}, Número de pacientes: {len(dengue)}")
print(f"Número de passageiros que não pegaram dengue: {len(relatorio3['DataFrame'])}")
print()

if '-w' in sys.argv:
    for relatorio in relatorios:
        write_to_excel.write(relatorio['DataFrame'], f'relatorio_equipe{equipe}.xlsx', sheet_name=relatorio['Nome'])
