import os
from pathlib import Path
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
print()

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

print(f"{'RELATÓRIO 4':-^80}")
relatorio4 = gerar_relatorios.relatorio4(alunos, dengue)
relatorios.append(relatorio4)
print(f"Colunas do DataFrame resultante: {tuple(relatorio4['DataFrame'].columns)}")
print(f"Número de alunos: {len(alunos)}, Número de pacientes: {len(dengue)}")
print(f"Número de alunos que pegaram dengue: {len(relatorio4['DataFrame'])}")
print()

print(f"{'RELATÓRIO 5':-^80}")
relatorio5 = gerar_relatorios.relatorio5(alunos, onibus)
relatorios.append(relatorio5)
print(f"Colunas do DataFrame resultante: {tuple(relatorio5['DataFrame'].columns)}")
print(f"Número de alunos: {len(alunos)}, Número de passageiros: {len(onibus)}")
print(f"Número de alunos que usam transporte público: {len(relatorio5['DataFrame'])}")
print()

print(f"{'RELATÓRIO 6':-^80}")
relatorio6 = gerar_relatorios.relatorio6(dengue, onibus)
relatorios.append(relatorio6)
print(f"Colunas do DataFrame resultante: {tuple(relatorio6['DataFrame'].columns)}")
print(f"Número de pacientes: {len(dengue)}, Número de passageiros: {len(onibus)}")
print(f"Número de pacientes que usam transporte público: {len(relatorio6['DataFrame'])}")
print()

print(f"{'RELATÓRIO 7':-^80}")
relatorio7 = gerar_relatorios.relatorio7(alunos, dengue, onibus)
relatorios.append(relatorio7)
print(f"Colunas do DataFrame resultante: {tuple(relatorio7['DataFrame'].columns)}")
print(f"Número de alunos: {len(alunos)}, Número de pacientes: {len(dengue)}, Número de passageiros: {len(onibus)}")
print(f"Número de alunos pacientes que usam transporte público: {len(relatorio7['DataFrame'])}")
print()

print(f"{'RELATÓRIO 8':-^80}")
relatorio8 = gerar_relatorios.relatorio8(dengue, onibus)
relatorios.append(relatorio8)
print(f"Colunas do DataFrame resultante: {tuple(relatorio8['DataFrame'].columns)}")
print(f"Número de pacientes: {len(dengue)}, Número de passageiros: {len(onibus)}")
print(f"Número de alunos pacientes que usam transporte público: {len(relatorio8['DataFrame'])}")
print()

print(f"{'RELATÓRIO 9':-^80}")
relatorio9 = gerar_relatorios.relatorio9(dengue, alunos)
relatorios.append(relatorio9)
print(f"Colunas do DataFrame resultante: {tuple(relatorio9['DataFrame'].columns)}")
print(f"Número de pacientes: {len(dengue)}, Número de alunos: {len(alunos)}")
print(f"Número de pacientes que frequentaram a escola: {len(relatorio9['DataFrame'])}")
print()

print(f"{'RELATÓRIO 10':-^80}")
relatorio10 = gerar_relatorios.relatorio10(alunos, dengue, onibus)
relatorios.append(relatorio10)
print(f"Colunas do DataFrame resultante: {tuple(relatorio10['DataFrame'].columns)}")
print(f"Número de pacientes: {len(dengue)}, Número de alunos: {len(alunos)}, Número de passageiros: {len(onibus)}")
print(f"Número de pacientes que não frequentaram a escola nem usaram transporte público: {len(relatorio10['DataFrame'])}")
print()

if '-v' in sys.argv:
    import venn
    venn.venn1(equipe)
    venn.venn2(equipe)
    venn.venn3(equipe)
    venn.venn4(equipe)
    venn.venn5(equipe)
    venn.venn6(equipe)
    venn.venn7(equipe)
    venn.venn8(equipe)
    venn.venn9(equipe)
    venn.venn10(equipe)

base_path = str(Path(os.path.abspath(__file__)).resolve().parents[0])
venn_path = os.path.join(
    base_path,
    'output/venn' if sys.platform.startswith("linux") else 'output\\venn'
)

if '-w' in sys.argv:
    for i, relatorio in enumerate(relatorios):
        write_to_excel.write(relatorio['DataFrame'], f'relatorio_equipe{equipe}.xlsx', relatorio['Nome'], f'equipe{equipe}-relatorio{i + 1}.png')
