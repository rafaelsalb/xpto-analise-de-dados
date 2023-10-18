import map_dates as md
import pandas as pd


def filter_dates(df: pd.DataFrame, col: str, lower_year: int = 1900, lower_month: int = 1, lower_day: int = 1, upper_year: int = 2024, upper_month: int = 12, upper_day: int = 31) -> pd.DataFrame:
    to_drop = []
    for index, _ in df.iterrows():
        curr_date = df.at[index, col]
        year = int(md.get_year(curr_date))
        month = int(md.get_month(curr_date))
        day = int(md.get_day(curr_date))
        if not lower_year <= year <= upper_year:
            to_drop.append(index)
        elif not lower_month <= month <= upper_month:
            to_drop.append(index)
        elif not lower_day <= day <= upper_day:
            to_drop.append(index)
    return df.drop(index=to_drop)

def format_date(df: pd.DataFrame, column_label: str) -> pd.DataFrame:
    for index, _ in df.iterrows():
        df.at[index, column_label] = df.at[index, column_label].split(" ")[0].strip()
    return df

def diff(A: pd.DataFrame, B: pd.DataFrame, output_columns: tuple[str] = ()) -> pd.DataFrame:
    # merged = pd.merge(A, B, how='outer', on=['Nome', 'Data de Nascimento'], indicator=True, suffixes=['', '_y'])
    merged = pd.merge(A, B, how='outer', on=['Nome'], indicator=True, suffixes=['', '_y'])
    merged = merged.loc[lambda x: x['_merge'] == 'left_only']
    merged = merged.drop(
        [i for i in list(merged.columns)
         if i.lower() not in (j.lower() for j in output_columns)],
        axis=1
    )
    return merged

def intersection(A: pd.DataFrame, B: pd.DataFrame, output_columns: tuple[str] = ()) -> pd.DataFrame:
    # merged = pd.merge(A, B, how='outer', on=['Nome', 'Data de Nascimento'], indicator=True, suffixes=['', '_y'])
    merged = pd.merge(A, B, how='outer', on=['Nome'], indicator=True, suffixes=['', '_y'])
    merged = merged.loc[lambda x: x['_merge'] == 'both']
    merged = merged.drop(
        [i for i in list(merged.columns)
         if i.lower() not in (j.lower() for j in output_columns)],
        axis=1
    )
    return merged

def result(nome: str, DataFrame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {'Nome': nome, 'DataFrame': DataFrame}

def relatorio1(alunos: pd.DataFrame, dengue: pd.DataFrame, filtrar: bool = False) -> dict[str, pd.DataFrame]:
    '''
    Diferença entre os DataFrames "alunos" e "dengue"
    O DataFrame resultante preserva apenas as colunas ID, Nome e Data de Nascimento.
    '''
    merged = diff(alunos, dengue, ("nome", "id", "data de nascimento"))
    merged = format_date(merged, "Data de Nascimento")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
    merged = merged.drop_duplicates()
    return result('Relatório 1 - Educação', merged)

def relatorio2(dengue: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Intersecção entre os DataFrames "dengue" e "onibus"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento e Data da Dengue.
    '''
    merged = intersection(dengue, onibus, ("nome", "data de Nascimento", "data da dengue"))
    merged = format_date(merged, "Data de Nascimento")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 2 - Saúde', merged)

def relatorio3(onibus: pd.DataFrame, dengue: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Diferença entre os DataFrames "onibus" e "dengue"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento e Ônibus.
    '''
    merged = diff(onibus, dengue, ("nome", "data de nascimento", "ônibus"))
    merged = md.add_sep(merged)
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
    merged = merged.drop_duplicates()
    return result('Relatório 3 - Mobilidade', merged)

def relatorio4(alunos: pd.DataFrame, dengue: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Intersecção entre os DataFrames "alunos" e "dengue"
    O DataFrame resultante preserva apenas as colunas ID, Nome, Data de Nascimento e Data da Dengue.
    '''
    merged = intersection(alunos, dengue, ("id", "nome", "data de nascimento", "data da dengue"))
    # Remover horários
    merged = format_date(merged, "Data de Nascimento")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 4 - Educação e Saúde', merged)

def relatorio5(alunos: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Intersecção entre os DataFrames "alunos" e "onibus"
    O DataFrame resultante preserva apenas as colunas ID, Nome, Data de Nascimento e Ônibus.
    '''
    merged = intersection(alunos, onibus, ("id", "nome", "data de nascimento", "ônibus"))
    # Remover horários
    merged = format_date(merged, "Data de Nascimento")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
    merged = merged.drop_duplicates()
    return result('Relatório 5 - Educação e Mobilidade', merged)

def relatorio6(dengue: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Intersecção entre os DataFrames "dengue" e "onibus"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento, Data da Dengue e Ônibus.
    '''
    merged = intersection(dengue, onibus, ("nome", "data de nascimento", "data da dengue", "ônibus"))
    merged = format_date(merged, "Data da Dengue")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 6 - Saúde e Mobilidade', merged)

def relatorio7(alunos: pd.DataFrame, dengue: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Intersecção entre os DataFrames "alunos", "dengue" e "onibus"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento, Data da Dengue e Ônibus.
    '''
    merged = intersection(alunos, dengue, ("nome", "data de nascimento", "data da dengue"))
    merged = format_date(merged, "Data de Nascimento")
    merged = format_date(merged, "Data da Dengue")
    merged = intersection(merged, onibus, ("nome", "data de nascimento", "data da dengue", "ônibus"))
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 7 - Saúde, Mobilidade e Educação', merged)

def relatorio8(dengue: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Diferença entre os DataFrames "dengue" e "onibus"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento e Data da Dengue.
    '''
    merged = diff(dengue, onibus, ("nome", "data de Nascimento", "data da dengue"))
    merged = format_date(merged, "Data de Nascimento")
    merged = format_date(merged, "Data da Dengue")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 8 - Dengue sem Transporte Público', merged)

def relatorio9(dengue: pd.DataFrame, alunos: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Diferença entre os DataFrames "dengue" e "alunos"
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento e Data da Dengue.
    '''
    merged = diff(dengue, alunos, ("nome", "data de Nascimento", "data da dengue"))
    merged = format_date(merged, "Data de Nascimento")
    merged = format_date(merged, "Data da Dengue")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 9 - Dengue sem Educação', merged)

def relatorio10(alunos: pd.DataFrame, dengue: pd.DataFrame, onibus: pd.DataFrame, filtrar: bool = False) -> pd.DataFrame:
    '''
    Diferença entre os DataFrames "dengue", "alunos", e depois "onibus
    O DataFrame resultante preserva apenas as colunas Nome, Data de Nascimento e Data da Dengue.
    '''
    merged = diff(dengue, alunos, ("nome", "data de Nascimento", "data da dengue"))
    merged = diff(merged, onibus, ("nome", "data de Nascimento", "data da dengue"))
    merged = format_date(merged, "Data de Nascimento")
    merged = format_date(merged, "Data da Dengue")
    if filtrar:
        merged = filter_dates(merged, "Data de Nascimento")
        merged = filter_dates(merged, "Data da Dengue")
    merged = merged.drop_duplicates()
    return result('Relatório 10 - Dengue sem Educação e Transporte Público', merged)

if __name__ == "__main__":
    import sys
    import get_dataframes

    alunos = get_dataframes.alunos(1)
    dengue = get_dataframes.dengue(1)
    onibus = get_dataframes.onibus(1)
    relatorio = int(sys.argv[1])

    if relatorio == 1:
        relatorio1(alunos, dengue)
    elif relatorio == 2:
        relatorio2(dengue, onibus)
    elif relatorio == 3:
        relatorio3(onibus, dengue)
    elif relatorio == 4:
        relatorio4(alunos, dengue)
    elif relatorio == 5:
        relatorio5(alunos, onibus)
    elif relatorio == 6:
        relatorio6(dengue, onibus)
    elif relatorio == 7:
        relatorio7(alunos, dengue, onibus)
