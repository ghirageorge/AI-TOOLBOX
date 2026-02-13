import click

@click.group()
def cli():
    """AI Toolbox Command Line Interface"""
    pass

@click.command()
def hello():
    """Prints a greeting message."""
    click.echo("hello from AI toolbox!")

# Attach the hello command to the cli group
cli.add_command(hello)

if __name__ == "__main__":
    cli()