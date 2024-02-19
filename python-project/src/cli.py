
# src/cli.py
import click

@click.group()
def cli():
    pass

@cli.command()
def create_tables():
    from .database import Base, engine
    Base.metadata.create_all(bind=engine)
    click.echo("Tables created")

if __name__ == "__main__":
    cli()