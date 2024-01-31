import click

@click.command("catzilla")
@click.version_option("0.0.1", prog_name="catzilla-cli")
def cli():
    click.echo("Hello from Catzilla")

if __name__ == "__main__":
    cli()