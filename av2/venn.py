from get_dataframes import alunos, dengue, onibus
import matplotlib
import matplotlib.pyplot as plt
import matplotlib_venn as plt_venn
import os
import pandas as pd
from pathlib import Path
import sys


matplotlib.use('TkAgg')
base_path = str(Path(os.path.abspath(__file__)).resolve().parents[0])

output_path = os.path.join(
    base_path,
    'output/venn' if sys.platform.startswith("linux") else 'output\\venn'
)
if not os.path.exists(output_path):
    try:
        os.mkdir(
            os.path.join(base_path, 'output')
        )
    except:
        pass
    os.mkdir(output_path)

def venn1(show_graph: bool = False):
    plt_venn.venn2(
        [
            set(alunos(1)["Nome"].to_list()),
            set(dengue(1)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue')
    )
    plt.savefig(
        os.path.join(
            output_path, 'venn1.png'
        )
    )
    if show_graph: plt.show()
