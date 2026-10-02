"""Разбор и выполнение команд."""

import shlex


def run_command(line):
    """Выполняет команду и возвращает текст результата.

    Возвращает None, если нужно закрыть эмулятор.
    """
    try:
        parts = shlex.split(line)
    except ValueError:
        return "Ошибка: незакрытая кавычка"
    if not parts:
        return ""
    name = parts[0]
    args = parts[1:]
    if name == "exit":
        return None
    if name in ("ls", "cd"):
        return f"{name} {args}"
    return f"{name}: команда не найдена"
