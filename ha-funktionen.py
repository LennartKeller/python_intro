from typing import List
 
def check_anagramm(w1: str, w2: str, check_cases=False) -> bool:
    if not check_cases:
        w1, w2 = w1.lower(), w2.lower()
    for char in w1:
        if w1.count(char) != w2.count(char):
            return False
        w1, w2, = w1.replace(char, ''), w2.replace(char, '')
    if w2:
        return False
    return True

def my_reverse(l:List) -> List:
    reversed_list = []
    for i in range(len(l)):
        negative_index = (len(l) - 1) - i
        reversed_list.append(l[negative_index])
    return reversed_list

def naive_stemmer(token: str):
    if token.endswith("en"):
        token = token[:-2]
    elif token.endswith("s"):
        token = token[:-1]
    if len(token) > 5:
        return token[:(len(token)//5) * 4]
    return token


if __name__ == '__main__':
        
    import re
    from collections import Counter
    from pathlib import Path

    w1 = "Geburt"
    w2 = "Betrug"
    print(check_anagramm(w1, w2))

    l1 = [1,2,3,4]
    l2 = "Also, es begann damit, dass ich in List auf Sylt stehe und ...".split()
    print(my_reverse(l1))
    print(my_reverse(l2))
    
    tokens = re.findall(r"\w+", Path("Fontane-Theodor_Effi Briest.txt").read_text().lower()) 
    stemmed_tokens = list(map(naive_stemmer, tokens))
    stemmed_tokens_freq = Counter(stemmed_tokens)
    print(*stemmed_tokens_freq.most_common(50), sep='\n')

