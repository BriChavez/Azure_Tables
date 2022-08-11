import typer

from azure import azure_app

app = typer.Typer()
app.add_typer(azure_app, name='azure')


if __name__ == '__main__':
    app()
