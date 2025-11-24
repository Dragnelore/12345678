import click
from . import OPERATIONS


@click.group()
def cli():
    """CLI для mini_mathlib: факториал и среднее арифметическое."""
    pass


@cli.command(name="fa")
@click.argument("n", type=int)
def fa_command(n: int):
    """
    Посчитать факториал числа n.

    Пример:
      python -m mini_mathlib.cli fa 5
    """
    # 1. Берём класс из реестра
    op_class = OPERATIONS["fa"]
    # 2. Создаём объект операции (у тебя __init__(self, a))
    op = op_class(n)
    # 3. Вызываем execute
    result = op.execute()
    # 4. Печатаем результат
    click.echo(result)


@cli.command(name="avg")
@click.argument("numbers", type=float, nargs=-1)
def avg_command(numbers: tuple[float, ...]):
    """
    Посчитать среднее арифметическое произвольного количества чисел.

    Пример:
      python -m mini_mathlib.cli avg 1 2 3 4 5
    """
    if not numbers:
        click.echo("Ошибка: нужно передать хотя бы одно число.", err=True)
        raise SystemExit(1)

    # 1. Берём класс из реестра
    op_class = OPERATIONS["avg"]
    # 2. Создаём объект: у тебя __init__(self, *args)
    op = op_class(*numbers)
    # 3. Вызываем execute
    result = op.execute()
    # 4. Печатаем результат
    click.echo(result)






@cli.command(name = "add")
@click.argument("a", type=int, nargs=2)
def add_command(a: int):
    if len(a) != 2:
        click.echo("Ошибка: нужно передать ровно два числа.", err=True)
        raise SystemExit(1)
    op_class = OPERATIONS["add"]
    op = op_class(*a)
    result = op.execute()
    click.echo(result)


if __name__ == "__main__":
    cli()
