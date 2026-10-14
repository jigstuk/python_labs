# Лаб 3

## Функция normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text=text.replace('Ё','Е').replace('ё','е')

    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    return ' '.join(text.split())
```
![фото](/image/lab03/img01.png)
## Функция tokenize
```python
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*",text)
```
![фото](/image/lab03/img02.png)
## Функция count_freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for token in tokens:
        freq[token]=freq.get(token,0)+1
    return freq
```
![фото](/image/lab03/img03.png)
## Функция top_n
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError
    return sorted(freq.items(), key=lambda x:(-x[1],x[0]))[:n]
```
![фото](/image/lab03/img04.png)
## Задание б

```python
import sys

from pathlib import Path
m = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(m))

from lib.lib import normalize,tokenize,count_freq,top_n

txt=sys.stdin.read()

text=normalize(txt)
count=tokenize(text)
uslov=count_freq(count)
top=top_n(uslov,n=5)

print(f'Всего слов:{len(count)}')
print(f'Уникальных слов:{len(uslov)}')
print(f'Топ-5:')

for word, chislo in top:
    print(f'{word}:{chislo}')
```
![фото](/image/lab03/img05.png)