from gerar_relatorios import format_date
import get_dataframes
import matplotlib
import matplotlib.pyplot as plt
import map_dates as md
import numpy as np
import os
import pandas as pd
from pathlib import Path
import sys

matplotlib.use('TkAgg')
base_path = str(Path(os.path.abspath(__file__)).resolve().parents[0])

output_path = os.path.join(
    base_path,
    'output/graphs' if sys.platform.startswith("linux") else 'output\\graphs'
)
if not os.path.exists(output_path):
    try:
        os.mkdir(
            os.path.join(base_path, 'output')
        )
    except:
        pass
    os.mkdir(output_path)

def hist_anos(src: callable, show_graph: bool = True, output_name: str = '') -> None:
    anos = []
    for i in range(1, 11):
        data = src(i)
        data = format_date(data, "Data de Nascimento")
        data = md.add_sep(data)
        curr_anos = list(map(lambda x: int(x.split('-')[2]), data["Data de Nascimento"].to_list()))
        for j in curr_anos:
            anos.append(j)
    
    fig, ax = plt.subplots()

    ax.hist(anos, bins=20, edgecolor='black')
    ax.set(
        mouseover=True,
        xticks=np.arange(0, 10000, 500),
        yticks=np.arange(0, 1501, 50),
        title="Distribuição de anos",
        xlabel='Ano',
        ylabel="Ocorrências do ano"
    )
    ax.tick_params(
        axis='x',
        labelrotation=-45
    )

    fig.savefig(
        os.path.join(
            output_path,output_name
        )
    )
    if show_graph:
        plt.show()

def hist_meses(src: callable, show_graph: bool = True, output_name: str = '') -> None:
    meses = []
    for i in range(1, 11):
        data = src(i)
        data = format_date(data, "Data de Nascimento")
        data = md.add_sep(data)
        curr_meses = list(map(lambda x: int(x.split('-')[1]), data["Data de Nascimento"].to_list()))
        for j in curr_meses:
            meses.append(j)
    
    fig, ax = plt.subplots()
    ax.hist(
        meses,
        bins=100,
        edgecolor='black',
    )
    ax.set(
        title='Distribuição de meses',
        xlabel='Mês',
        ylabel='Ocorrências do mês',
    )
    plt.xticks(ticks=[0, 12] + [i for i in range(20, 100, 10)])

    fig.savefig(
        os.path.join(
            output_path,output_name
        )
    )
    if show_graph:
        plt.show()

def hist_dias(src: callable, show_graph: bool = True, output_name: str = '') -> None:
    dias = []
    for i in range(1, 11):
        data = src(i)
        data = format_date(data, "Data de Nascimento")
        data = md.add_sep(data)
        curr_dias = list(map(lambda x: int(x.split('-')[1]), data["Data de Nascimento"].to_list()))
        for j in curr_dias:
            dias.append(j)
    
    fig, ax = plt.subplots()
    ax.hist(
        dias,
        bins=100,
        edgecolor='black'
    )
    ax.set(
        title='Distribuição de dias',
        xlabel='Dia',
        ylabel='Ocorrências do dia'
    )
    plt.xticks(ticks=np.arange(0, 101, 10))

    fig.savefig(
        os.path.join(
            output_path,output_name
        )
    )
    if show_graph:
        plt.show()

if __name__ == "__main__":
    import sys

    alunos = get_dataframes.alunos
    dengue = get_dataframes.dengue
    onibus = get_dataframes.onibus
    arg = sys.argv[1]

    match arg:
        case 'aa':
            hist_anos(alunos)
        case 'am':
            hist_meses(alunos)
        case 'ad':
            hist_dias(alunos)
        case 'da':
            hist_anos(dengue)
        case 'dm':
            hist_meses(dengue)
        case 'dd':
            hist_dias(dengue)
        case 'oa':
            hist_anos(onibus)
        case 'om':
            hist_meses(onibus)
        case 'od':
            hist_dias(onibus)
        case 'all':
            hist_anos(alunos, False, 'alunos_anos.png')
            hist_anos(dengue, False, 'dengue_anos.png')
            hist_anos(onibus, False, 'onibus_anos.png')
            hist_meses(alunos, False, 'alunos_meses.png')
            hist_meses(dengue, False, 'dengue_meses.png')
            hist_meses(onibus, False, 'onibus_meses.png')
            hist_dias(alunos, False, 'alunos_dias.png')
            hist_dias(dengue, False, 'dengue_dias.png')
            hist_dias(onibus, False, 'onibus_dias.png')
            