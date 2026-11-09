
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from src.lab04.io_txt_csv import ensure_parent_dir


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''Преобразует CSV-файл в Excel-файл'''

    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.suffix.lower() != ".csv" or xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError("Неверный тип файлов")

    if not csv_path.is_file():
        raise FileNotFoundError("Файл не найден")

    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data or not data[0]:
        raise ValueError("CSV пустой или отсутствует заголовок")

    if not any(row for row in data[1:]):
        raise ValueError("CSV не содержит данных")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in data:
        ws.append(row)

    for column in ws.columns:
        max_length = 0

        for cell in column:
            if cell.value is not None:
                max_length = max(max_length, len(str(cell.value)))

        letter = get_column_letter(column[0].column)
        ws.column_dimensions[letter].width = max(8, max_length + 2)

    ensure_parent_dir(xlsx_path)
    wb.save(xlsx_path)


if __name__ == "__main__":
    sample_csv = "data/lab05/samples/people.csv"
    out_xlsx = "data/lab05/out/people.xlsx"

    csv_to_xlsx(sample_csv, out_xlsx)
