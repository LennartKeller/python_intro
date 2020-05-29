from pathlib import Path
import re
from typing import List, Dict, Iterable

def count_types(tokens: List[str]) -> Dict[str, int]:
    types_freqs = {}
    for token in tokens:
        if types_freqs.get(token):
            types_freqs[token] += 1
        else:
            types_freqs[token] = 1
    return types_freqs

def count_vowels(string: str) -> int:
    return sum([string.lower().count(vowel) for vowel in "aieuüäöo"])

def my_filter(function: callable, iterable: Iterable) -> List:
    return [value for value in iterable if function(value)]

if __name__ == '__main__':

    text = Path('Fontane-Theodor_Effi Briest.txt').read_text()

    tokens = re.findall(r'\w+', text)

    # 1. Aufgabe
    types_freqs = count_types(tokens)
    types_sorted = list(sorted(types_freqs.items(), key=lambda x: x[1]))
    print(types_sorted[-50:])

    # 2. Aufgabe
    first_hundred = tokens[:100]
    print(list(sorted(first_hundred, key=count_vowels, reverse=True)))

    # 3. Aufgabe
    print(my_filter(lambda x: x[0].isupper(), tokens[:20]))



