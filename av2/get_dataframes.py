import pandas as pd
from pathlib import Path
import os


bases_path = os.path.join(
    str(Path(os.path.abspath(__file__)).resolve().parents[0]),
    'bases'
)

def alunos(equipe: int):
    return pd.read_csv(
        os.path.join(bases_path, f'Equipe{equipe}/Base de Alunos{equipe-1}.csv'),
        sep=';',
        dtype='str'
    )

def dengue(equipe: int):
    return pd.read_csv(
        os.path.join(bases_path, f'Equipe{equipe}/Base de Dengue{equipe-1}.csv'),
        sep=';',
        dtype='str'
    )

def onibus(equipe: int):
    return pd.read_csv(
        os.path.join(bases_path, f'Equipe{equipe}/Base de Onibus{equipe-1}.csv'),
        sep=';',
        dtype='str'
    )
