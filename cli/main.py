import click


@click.command(help="Print simple hello.")
@click.argument("name", default="world")
def greet(name):
    click.echo(f"Hello, {name}!")


@click.group()
def cli():
    pass


cli.add_command(greet)

if __name__ == "__main__":
    cli()
