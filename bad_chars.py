import time

for t in reversed(range(1,11)):
	print(f"Nur noch {t} Sekund{'en' if t > 1 else 'e'}. Dann ist alles startbereit!")
	time.sleep(1)

def get_chars(instring):
    chars = []
    for i in instring:
        chars.append(i)
    return chars

if __name__ == '__main__':
    print(get_chars("Hello World!"))