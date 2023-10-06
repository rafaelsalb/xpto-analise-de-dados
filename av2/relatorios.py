import pandas as pd


def fix_date(df: pd.DataFrame) -> pd.DataFrame:
    for index, _ in df.iterrows():
        df.at[index, "Data de Nascimento"] = df.at[index, "Data de Nascimento"].split(" ")[0]
    return df

def result(nome: str, DataFrame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {'Nome': nome, 'DataFrame': DataFrame}


def relatorio1(alunos: pd.DataFrame, dengue: pd.DataFrame) -> dict[str, pd.DataFrame]:
    merged = pd.merge(alunos, dengue, how='outer', on=['Nome'], indicator=True, suffixes=['', '_y'])
    merged = merged.loc[lambda x: x['_merge'] == 'left_only']
    merged = merged.drop(
        [i for i in list(merged.columns)
         if i not in ("Nome", "ID", "Data de Nascimento")],
        axis=1
    )
    merged = fix_date(merged)
    return result('Relatorio 1 - Educacao', merged)

def relatorio2(dengue: pd.DataFrame, onibus: pd.DataFrame) -> pd.DataFrame:
    return