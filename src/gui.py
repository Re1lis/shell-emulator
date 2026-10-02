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


def start_gui():
    """Создаёт окно и запускает эмулятор."""
    root = tk.Tk()
    root.title(get_title())
    output = tk.Text(root, bg="black", fg="white", state="disabled")
    output.pack(fill="both", expand=True)
    entry = tk.Entry(root, bg="black", fg="white")
    entry.config(insertbackground="white")
    entry.pack(fill="x")
    entry.focus_set()

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