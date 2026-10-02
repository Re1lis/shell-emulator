"""Тесты команд эмулятора."""

from commands import run_command


def test_ls_prints_name_and_args():
    assert run_command("ls -l /home") == "ls ['-l', '/home']"


def test_cd_prints_name_and_args():
    assert run_command("cd /tmp") == "cd ['/tmp']"


def test_double_quotes():
    assert run_command('ls "my dir"') == "ls ['my dir']"


def test_single_quotes():
    assert run_command("ls 'my dir'") == "ls ['my dir']"


def test_unknown_command():
    assert run_command("foo") == "foo: команда не найдена"


def test_empty_line():
    assert run_command("") == ""


def test_unclosed_quote():
    assert run_command('ls "abc') == "Ошибка: незакрытая кавычка"


def test_exit():
    assert run_command("exit") is None