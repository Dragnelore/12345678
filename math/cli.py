import click
from . import OPERATIONS



@click.group()
def cli():
    pass

@cli.command(name = "fact")
@click.argument('n', type=int)
def fact(n):
    op_class = OPERATIONS['fa']
    obj = op_class(n)
    res = obj.execute()
    click.echo(f"{res}")

@cli.command(name = "avg")
@click.argument("g", type = float,nargs = -1)
def avg(g):
    op_class = OPERATIONS['avg']
    obj = op_class(*g)
    res = obj.execute()
    click.echo(f"{res}")


@cli.command(name = "add")
@click.argument("b", type = int,nargs=2)
def add_command(b):
    op = OPERATIONS["add"]
    obj = op(*b)
    res = obj.execute()
    click.echo(f"{res}")

if __name__ == "__main__":
    cli()