def append(text: str):
    with open('my_notes.txt', 'a', encoding='utf-8') as f:
        f.write(text, '\n')

def read():
    with open('my_notes.txt', 'r', encoding='utf-8') as f:
        print(f.read())

while True:
    ch = input('enter read/append: ' ).strip()
    if ch == 'read':
        read()
    elif ch == 'append':
        text = input('__:').strip()
        append(text)