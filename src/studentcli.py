import typer

app = typer.Typer()


@app.command(short_help='adds an item')
def add(first_name: str, last_name: str, email: str,phno:str):
    typer.echo(f"Adding details: {first_name}, {last_name}, {email},{phno}")


@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")


@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")


@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")


@app.command()
def show():
    typer.echo(f"Todos")


if __name__ == "__main__":
    app()