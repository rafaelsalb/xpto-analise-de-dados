import pandas as pd


def fix_date(df: pd.DataFrame, column_label: str) -> pd.DataFrame:
    for index, _ in df.iterrows():
        df.at[index, column_label] = df.at[index, column_label].split(" ")[0]
    return df

def diff(A: pd.DataFrame, B: pd.DataFrame, output_columns: tuple[str]):
    merged = pd.merge(A, B, how='outer', on=['Nome'], indicator=True, suffixes=['', '_y'])
    merged = merged.loc[lambda x: x['_merge'] == 'left_only']
    merged = merged.drop(
        [i for i in list(merged.columns)
         if i.lower() not in (j.lower() for j in output_columns)],
        axis=1
    )
    return merged

def result(nome: str, DataFrame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {'Nome': nome, 'DataFrame': DataFrame}

def relatorio1(alunos: pd.DataFrame, dengue: pd.DataFrame) -> dict[str, pd.DataFrame]:
    '''
    Exclui do DataFrame "alunos" todos os cidadãos registrados no DataFrame "dengue"
    O DataFrame resultante preserva apenas as colunas ID, Nome e Data de Nascimento.
    '''
    merged = diff(alunos, dengue, ("nome", "id", "data de nascimento"))
    merged = fix_date(merged, "Data de Nascimento")
    return result('Relatorio 1 - Educacao', merged)

def relatorio2(dengue: pd.DataFrame, onibus: pd.DataFrame) -> pd.DataFrame:
    merged = diff(dengue, onibus, ("nome", "data de Nascimento", "data da dengue"))
    merged = fix_date(merged, "Data da Dengue")
    merged = fix_date(merged, "Data de Nascimento")
    return result('Relatorio 2 - Saúde', merged)

def relatorio3(onibus: pd.DataFrame, dengue: pd.DataFrame) -> pd.DataFrame:
    merged = diff(onibus, dengue, ("nome", "data de nascimento", "ônibus"))
    return result('Relatorio 3 - Mobilidade', merged)

if __name__ == "__main__":
    import sys
    import get_dataframes

    alunos = get_dataframes.alunos(1)
    dengue = get_dataframes.dengue(1)
    onibus = get_dataframes.onibus(1)

    # relatorios = {
    #     1: (relatorio1, alunos, dengue),
    # }

    # equipe = 1
    # if len(sys.argv) > 1:
    #     equipe = int(sys.argv[1])

    relatorio = int(sys.argv[1])

    if relatorio == 1:
        relatorio1(alunos, dengue)
    elif relatorio == 2:
        relatorio2(dengue, onibus)
