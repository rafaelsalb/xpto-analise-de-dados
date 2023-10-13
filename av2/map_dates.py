import pandas as pd


def is_leap_year(year: int):
    return year % 4 == 0 and year % 100 == 0 and year % 400 == 0

def get_year(strdate: str) -> str:
    return strdate[-4:]

def get_month(strdate: str) -> str:
    return strdate[3:5]

def get_day(strdate: str) -> str:
    return strdate[0:2]

def add_sep(src: pd.DataFrame) -> pd.DataFrame:
    for i, _ in src.iterrows():
        if len(src.at[i, 'Data de Nascimento']) == 6:
            day = src.at[i, 'Data de Nascimento'][:1]
            month = src.at[i, 'Data de Nascimento'][1:2]
        elif len(src.at[i, 'Data de Nascimento']) == 7:
            day = src.at[i, 'Data de Nascimento'][:1]
            month = src.at[i, 'Data de Nascimento'][1:3]
        elif len(src.at[i, 'Data de Nascimento']) == 8:
            day = src.at[i, 'Data de Nascimento'][:2]
            month = src.at[i, 'Data de Nascimento'][2:4]
        else:
            day = src.at[i, 'Data de Nascimento'].split('-')[0]
            month = src.at[i, 'Data de Nascimento'].split('-')[1]
        src.at[i, 'Data de Nascimento'] = str(day).zfill(2) + "-" + str(month).zfill(2) + "-" + src.at[i, 'Data de Nascimento'][-4:]
    return src

def day_month(date: str) -> str:
    year = 0
    day_weight, month_weight = 0, 0
    if len(date) == 6:
        day_weight = int(date[:1])
        month_weight = int(date[1:2])
    elif len(date) == 7:
        day_weight = int(date[:1])
        month_weight = int(date[1:3])
    elif len(date) == 8:
        day_weight = int(date[:2])
        month_weight = int(date[2:4])
    else:
        day_weight = int(date[:2])
        month_weight = int(date[3:5])
    year = int(date[-4:])
    month = int(0.01 * month_weight * 12 + 1)
    month_lengths = {
        1: 31,
        2: 28 if not is_leap_year(year) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    day = int(0.01 * day_weight * month_lengths[month] + 1)
    return f"{str(day).zfill(2)}-{str(month).zfill(2)}-{str(year).zfill(4)}"

def correct_column(date: pd.Series) -> pd.Series:
    new_col = date.map(day_month)
    return new_col
