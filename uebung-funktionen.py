# Funktionen: Übung

# Zerlegen Sie den folgenden Code (auch in WueCampus als Python-Datei) sinnvoll in Funktionen.
# Die Funktionen sollten einen Wert berechnen, schreiben Sie davon getrennt eine Funktion `main()`, die die Textausgaben enthält und die Funktionen aufruft.

# Tip: PyCharm-Refactoring-Funktionen _rename_ und _extract method_

s = "Herr Mustermann kommt ins Haus und trifft dort Frau Musterfrau"
sum_wordlength = 0
for w in s.split():
    sum_wordlength += len(w)
avg_wordlength = sum_wordlength / len(s.split())
print("Durchschnittliche Wortlänge: ", avg_wordlength )
list_vowels = []
for w in s.lower().split():
    word_vowels = 0
    for c in w:
        if c in "aeiou":
            word_vowels += 1
    list_vowels.append(word_vowels)
print("Durchschnittliche Vokalanzahl: ", sum(list_vowels) / len(list_vowels))
list_consonants = []
for w in s.lower().split():
    word_cons = 0
    for c in w:
        if c in "bcdfghjklmnpqrstvwxyz":
            word_cons += 1
    list_consonants.append(word_cons)
print("Durchschnittliche Konsonantenanzahl: ", sum(list_consonants) / len(list_consonants))