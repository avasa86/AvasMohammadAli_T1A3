import typer
from rich.console import Console
from rich.table import Table
from model import Todo
#from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()


@app.command(short_help='adds an item')
def add(task: str, category: str):
    pass

@app.command()
def delete(position: int): ##removes an item
    pass

@app.command() ##updates an item
def update(position: int, task: str = None, category: str = None):
    pass