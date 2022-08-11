import typer

from .blobs import blobs_app

azure_app = typer.Typer()
azure_app.add_typer(blobs_app, name='blobs')
