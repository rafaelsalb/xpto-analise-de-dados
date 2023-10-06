import os
from pathlib import Path
import pandas as pd


output_path = os.path.join(
    str(Path(os.path.abspath(__file__)).resolve().parents[0]),
    'output/excel'
)


def write(input: pd.DataFrame, file_name: str, sheet_name: str):
    if os.path.exists(os.path.join(output_path, file_name)):
        with pd.ExcelWriter(os.path.join(output_path, file_name), mode="a", date_format='DD-MM-YYYY', if_sheet_exists="replace") as writer:
            input.to_excel(writer, sheet_name=sheet_name, index=False)
    with pd.ExcelWriter(os.path.join(output_path, file_name), mode="w", date_format='DD-MM-YYYY') as writer:
        input.to_excel(writer, sheet_name=sheet_name, index=False)
