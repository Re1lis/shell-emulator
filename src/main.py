"""Эмулятор оболочки. Точка входа."""

import argparse

from gui import start_gui


def parse_args():
    """Разбирает параметры командной строки."""
    parser = argparse.ArgumentParser(description="Эмулятор оболочки")
    parser.add_argument(
        "--vfs", help="путь к физическому расположению VFS"
    )
    parser.add_argument(
        "--script", help="путь к стартовому скрипту"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    start_gui(args.vfs, args.script)
