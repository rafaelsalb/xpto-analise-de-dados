import os
from pathlib import Path
import pandas as pd
import sys

base_path = str(Path(os.path.abspath(__file__)).resolve().parents[0])

output_path = os.path.join(
    base_path,
    'output/excel' if sys.platform.startswith("linux") else 'output\\excel'
)

if not os.path.exists(output_path):
    os.mkdir(
        os.path.join(base_path, 'output')
    )
    os.mkdir(output_path)


def write(input: pd.DataFrame, file_name: str, sheet_name: str):
    if os.path.exists(os.path.join(output_path, file_name)):
        with pd.ExcelWriter(os.path.join(output_path, file_name), mode="a", date_format='DD-MM-YYYY', if_sheet_exists="replace") as writer:
            input.to_excel(writer, sheet_name=sheet_name, index=False)
    else:
        with pd.ExcelWriter(os.path.join(output_path, file_name), mode="w", date_format='DD-MM-YYYY') as writer:
            input.to_excel(writer, sheet_name=sheet_name, index=False)
