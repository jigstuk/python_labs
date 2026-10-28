# python_labs
# Лабораторная работа 4

# Задание A 

## Функция read_text
Читает файл целиком и возвращает содержимое в виде одной строки. 
По умолчанию используется кодировка UTF-8. Внутри функции создается объект 
Path из переданного пути. Если файл не найден, возникает FileNotFoundError. 
При несовпадении кодировки возникает UnicodeDecodeError.
``` python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    '''Читает файл и возвращает его содержимое одной строкой.

    Args: 
        path: путь к файлу
        encoding: кодировка файла(пример: encoding="cp1251"), по умолчанию UTF-8
    Returns:
        Прочитанный файл в виде строки
    '''

    return Path(path).read_text(encoding=encoding)
 ```
## Функция ensure_parent_dir
Создает все родительские папки для указанного файла, если их еще нет. 
Полезна перед записью: если папки не существует, обычная запись упадет 
с ошибкой FileNotFoundError, а эта функция создаст всю цепочку директорий. 
Если папка уже существует, ошибка не возникает.

``` python
def ensure_parent_dir(path: str | Path) -> None:
    '''Создаем родительские папки, если их еще нет.
    Args: 
        path: путь к файлу
    Returns:
        None
    '''
    
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```

## Функция write_csv
Записывает строки в CSV-файл с разделителем «запятая». Существующий файл 
перезаписывается. Заголовок (если передан) пишется первой строкой. 
Перед записью проверяется, что все строки таблицы — это списки или кортежи 
(иначе TypeError), и что они имеют одинаковую длину (иначе ValueError). 
Запись идет через csv.writer с кодировкой UTF-8 и параметром newline="" 
(чтобы избежать лишних пустых строк на Windows).

```python
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None=None) -> None:
    '''Записывает список строк, кортежей или списков в csv-файл с разделителем-запятой.
    Args:
        rows: строки таблицы; все должны быть одной длины
        path: путь к файлу 
        header: заголовок таблицы. если передан, пишется первой строкой.

    Returns:
        None
    
    Raises:
        ValueError: Строки разной длины
    '''
    if rows:
        width = len(rows[0])
        for number, row in enumerate(rows, start=1):
            if len(row) != width:
                raise ValueError("У строк разная длина")
            
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
```
тест-кейс
![фото](/image/lab04/2.png)

# Задание B

```python
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from lib.lib import normalize, tokenize, top_n, count_freq
import argparse
from pathlib import Path

def generate_report(input_path: str | Path, output_path: str | Path, encoding: str = "utf-8"):
    text = read_text(input_path, encoding=encoding) #читаем текст, передаем кодировку
    normal_text = normalize(text) 
    tokens = tokenize(normal_text) 
    freq = count_freq(tokens)      
    top_words = top_n(freq, 5)     

    write_csv(top_words, output_path, header=("word", "count"))

    total_words = len(tokens) 
    unique_words = len(freq)  

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

def run_test_a():
    '''Тест А: обычный файл с текстом'''
    print("\n" + "="*40)
    print("ТЕСТ А: Один файл")
    print("="*40)

    input_file = "data/lab04/input.txt"
    output_file = "data/lab04/report.csv"

    ensure_parent_dir(input_file)
    Path(input_file).write_text("Привет, мир, привет!!!", encoding = "utf-8")

    #Запускаем генерацию
    generate_report(input_file, output_file)

    #Проверяем CSV
    print("\n---Проверка report.csv---")
    actual_csv = read_text(output_file)
    expected_csv = "word,count\nпривет,2\nмир,1\n"
    if actual_csv==expected_csv:
        print("CSV совпадает с ожидаемым!")
    else:
        print("Ошибка! CSV не совпадает с ожидаемым")

def run_test_b_empty():
    '''Тест B: пустой файл'''
    print("\n" + "="*40)
    print("ТЕСТ B: Пустой файл")
    print("="*40)

    input_file = "data/lab04/empty.txt"
    output_file = "data/lab04/report_empty.csv"

    #Создаем пустой входной файл
    write_csv([],input_file)
    #Запускаем генерацию
    generate_report(input_file,output_file)

    #Проверяем CSV
    print("\n---Проверка report_empty.csv---")
    actual_csv = read_text(output_file)
    expected_csv = "word,count\n"
    if actual_csv==expected_csv:
        print("CSV корректен")
    else:
        print("CSV не совпадает")

def run_test_c():
    '''Тест С: кодировка cp1251'''
    print("\n" + "="*40)
    print("ТЕСТ С: кодировка cp1251")
    print("="*40)
    
    input_file = "data/lab04/input_cp1251.txt"
    output_file = "data/lab04/report_cp1251.csv"

    ensure_parent_dir(input_file)
    Path(input_file).write_text("Привет", encoding = "cp1251")

    print("---Запуск для cp1251---")
    generate_report(input_file,output_file,encoding="cp1251")
    print("--Результат в report_cp1251---")
    print(read_text(output_file))
                                

if __name__ == "__main__":
    run_test_a()
    run_test_b_empty()
    run_test_c()

# python -m src.lab04.text_report
# python -m src.lab04.text_report --in data/in.txt --out data/out.csv
```
тест а 
![фото](/image/lab04/а.png)
тест б
![фото](/image/lab04/б.png)
тест с
![фото](/image/lab04/с.png)