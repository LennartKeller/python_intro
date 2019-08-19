---
classoption: DIV=16
---

### Einfache reguläre Ausdrücke

* »normale« Zeichen (= keine Metazeichen) matchen sich selbst. `a` matcht `a`.
    * _Metazeichen_ sind `. ^ $ * + ? { } [ ] \ | ( )`, sie können gematcht werden, indem man einen `\` voranstellt 
* Ein Punkt `.` matcht ein beliebiges Zeichen (außer Newline). `.` matcht `a` oder `b` oder …    
* Zusammensetzen = Hintereinanderschreiben.
    * `abc` matcht "abc"
    * `H. h. h.` matcht z.B. "Ha ha ha" oder "Ho ho ho" oder "He ha hi"

### Zeichenklassen

* `[abc]` matcht ein Zeichen, das `a` oder `b` oder `c` ist.
* `[A-Fa-f]` matcht einen der Groß- oder Kleinbuchstaben von A bis F
* `^` am Beginn einer Zeichenklasse invertiert die Klasse:
   * `[^0-9]` matcht jedes Zeichen, das _keine_ Ziffer von 0-9 ist
* In Zeichenklassen gelten Metazeichen nicht: `[.]` matcht ebenso wie `\.` einen Punkt

#### häufige Zeichenklassen

-   `.` jedes Zeichen außer neue Zeile (`\n`)
-   `\d` jede Ziffer, z.B. 1, 4, 0 <br/>
    `\D` jedes Zeichen, das **keine** Ziffer ist.
-   `\s` jedes whitespace-Zeichen, z.B. Leerzeichen, `\n`, `\t`
    `\S` jedes Zeichen, das **kein** whitespace ist.<br/>
-   `\w` »Identifier-Zeichen«, also Buchstaben, z.B. A g ö ß 4 é € α И, Ziffern, Unterstrich `_` <br/>
    `\W` jedes Zeichen, das **kein** Identifier-Zeichen ist.

Die Definitionen beziehen sich auf die Unicode-Zeicheneigenschaften. Wer Zugriff auf die kompletten Unicode-Properties will, muss das externe Modul _regex_ installieren.


### Wiederholungen

* `*` matcht auf **0 oder mehr** Wiederholungen des vorherigen Zeichens/Teilausdrucks
* `+` matcht auf **1 oder mehr** Wiederholungen des vorherigen Zeichens/Teilausdrucks
* `?` matcht auf **0 oder 1** Wiederholungen des vorherigen Zeichens/Teilausdrucks
* `{n,m}` matcht auf **n bis m** Wiederholungen des vorherigen Zeichens/Teilausdrucks 


### Positionen / Anker
… matchen nicht _auf_, sondern _vor/nach/zwischen_ Zeichen

* `^` matches the start of the string
* `$` matches the end of the string
* `\b` matches the empty string but only at the beginning or ending of a word 
* `\B` matches the empty string but only if it is not at the beginning or ending of a word




### Gruppierungen

* Runde Klammern um einen Teilausdruck bilden eine **Gruppe**.
* Quantoren gelten für die ganze Gruppe -> `(bla)+` matcht `blablabla`
* Gruppen können separat referenziert werden


```python
s = "Sehr geehrte Frau Mustermann,"
m = re.match("Sehr geehrter? (.*),", s)
m.groups()
```

Gruppen können mit `\1`, `\2`, ... auch innerhalb des Ausdrucks oder in einem Ersetzungsstring bei `re.sub` referenziert werden:

```python
expr = "n = n + 1; test = test + n; n = test + 1"
simplified = re.sub(r"(\w+) = \1 \+ (\w+)",   # diese RE bildet zwei Gruppen, die in der RE (\1) …
                    r"\1 += \2",              # und im 'ersetzen'-String (\1, \2) referenziert werden
                    expr)
print(simplified)
```

    n += 1; test += n; n = test + 1



### Greedy vs. Non-Greedy
* Voreinstellung: greedy, d.h. das die größtmögliche Zeichenkette gesucht wird, die zum regulären Ausdruck passt.
* Durch `?` nach dem Quantifier Umstellung auf non-greedy

### Oder

Mit `|` können Sie nach Alternativen suchen
