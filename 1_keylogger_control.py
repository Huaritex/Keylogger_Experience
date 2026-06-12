from pynput.mouse import Controller
import sys


def control_teclado():
    teclado = Controller()
    teclado.type('')


def control_mouse():
    mouse = Controller()
    mouse.position = (1200,800)


def main():
    control_mouse()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
