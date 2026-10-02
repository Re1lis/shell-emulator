"""Данные о операционной системе."""

import getpass
import socket


def get_title():
    """Возвращает заголовок окна."""
    return f"Эмулятор - [{getpass.getuser()}@{socket.gethostname()}]"


def get_prompt():
    """Возвращает приглашение ввода."""
    return f"{getpass.getuser()}@{socket.gethostname()}:~$ "