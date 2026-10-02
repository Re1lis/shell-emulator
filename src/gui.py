"""Графический интерфейс эмулятора."""

import tkinter as tk

from commands import run_command
from sysinfo import get_prompt, get_title


def add_text(output, text):
    """Добавляет строку в область вывода."""
    output.config(state="normal")
    output.insert("end", text + "\n")
    output.config(state="disabled")
    output.see("end")


def run_script(root, output, script_path):
    """Выполняет команды из стартового скрипта."""
    try:
        with open(script_path, encoding="utf-8-sig") as file:
            lines = file.read().splitlines()
    except OSError:
        add_text(output, f"Ошибка: не удалось открыть {script_path}")
        return
    for line in lines:
        add_text(output, get_prompt() + line)
        result = run_command(line)
        if result is None:
            root.destroy()
            return
        if result:
            add_text(output, result)


def start_gui(vfs_path=None, script_path=None):
    """Создаёт окно и запускает эмулятор."""
    root = tk.Tk()
    root.title(get_title())
    output = tk.Text(root, bg="black", fg="white", state="disabled")
    output.pack(fill="both", expand=True)
    entry = tk.Entry(root, bg="black", fg="white")
    entry.config(insertbackground="white")
    entry.pack(fill="x")
    entry.focus_set()
    add_text(output, "[отладка] параметры запуска:")
    add_text(output, f"[отладка] vfs = {vfs_path or 'не задан'}")
    add_text(output, f"[отладка] script = {script_path or 'не задан'}")

    if script_path:
        root.after(100, run_script, root, output, script_path)

    def on_enter(event):
        """Обрабатывает нажатие Enter."""
        line = entry.get()
        entry.delete(0, "end")
        add_text(output, get_prompt() + line)
        result = run_command(line)
        if result is None:
            root.destroy()
        elif result:
            add_text(output, result)

    entry.bind("<Return>", on_enter)
    root.mainloop()
