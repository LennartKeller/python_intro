Funktionen haben Sie alle schon benutzt – z.B. `len()` oder `sum()`. Funktionen können Sie aber auch selbst definieren, etwa, um gleichartige Funktionalität, die nur von einer Handvoll *Parameter* abhängt,
zusammenzufassen und per Namen aufrufbar zu machen.

Um eine Funktion zu definieren, verwenden Sie die folgende Syntax:

| `def` funktionsname `(` parameter `,` parameter ...`):`
|    Funktionskörper (Programmcode)
|    `return` ergebniswert

Hier, zum Beispiel, eine (funktionsäquivalente) Definition der
eingebauten Summenfunktion, die Sie in der letzten Aufgabe verwendet
haben:

```python
def sum(iterable, start=0):
    result = start
    for value in iterable:
        result = result + value
    return result
```

Wenn Sie das nun mit `x = sum([1,2,3,4])` aufrufen, bekommt `iterable` den
Wert `[1,2,3,4]`, `start` den (voreingestellten) Wert `0`, der Code
unterhalb der `def`-Zeile wird ausgeführt, und schließlich der
abschließende Wert von `result` (10) zurückgegeben (und dann `x`
zugewiesen).

### Übungsaufgabe:

Schauen Sie sich das angehängte Programm an. 

1. Welche Programmabschnitte sind ähnlich und unterscheiden sich nur in Details? Diese Programmabschnitte eigenen sich zur Extraktion in Funktionen. 
2. Versuchen Sie, die in Teil 1 identifizierten Programmabschnitte zu Funktionen zu extrahieren. Dabei werden Sie ggf. eine Funktion einmal schreiben, aber mehrfach aufrufen.

Beachten Sie: Eine Funktion sollte in der Regel nur _entweder_ irgendetwas berechnen und das dann in einer geeigneten Form mit `return` zurückgeben (z.B. im Falle der Summenfunktion eine Zahl) _oder_ irgendetwas auf den Bildschirm schreiben (wie die `print`-Funktion selbst, die ja auch kein Ergebnis zurückgibt). Funktionen, die etwas berechnen und mit return zurückgeben, kann man dann auch in einem anderen Kontext aufrufen und z.B. mit dem Ergebnis weiterrechnen, es auf einer Webseite ausgeben etc.

__Softwaretipp:__ Solche Umstrukturierungen, die zwar die Struktur des Programmes verändern, aber die Funktionalität unangetastet lassen, nennt man auch _Refactoring_. PyCharm bietet im Menü _Refactor_ und z.B. dem Untermenü _Extract_ bzw. mit der Funktion _irgendwas markieren_ / _Refactor this_ (Strg+Alt+⇧+T) eine Reihe von Hilfestellungen dazu, etwa _Extract method_ um Funktionen/Methoden zu extrahieren oder _Rename_ um z.B. eine Variable umzubenennen.
