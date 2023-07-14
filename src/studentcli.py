import typer
from rich.console import Console
from rich.table import Table
from model import Subject,Student
from database import get_all_subjects,insert_subject

console = Console()

app = typer.Typer()


@app.command(short_help='adds a subject')
def add(subject_name: str):
    typer.echo(f"adding {subject_name}")
    subject = Subject(subject_name)
    typer.echo("arun")
    insert_subject(subject)
    show_subject()

@app.command()
def show_subject():
    subject_list = get_all_subjects()
    console.print("[bold magenta]Subject[/bold magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Subject Name", min_width=20)

    def get_subject_color(category):
        COLORS = {'Maths': 'cyan', 'Physics': 'red', 'Chemistry': 'cyan', 'Economics': 'green','English': 'orange','Philosophy':'violet'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, subject in enumerate(subject_list, start=1):
        the_sub = str(subject)[1:-1]
        c = get_subject_color(the_sub)
        table.add_row(str(idx), f'[{c}]{the_sub}[/{c}]')
    console.print(table)


if __name__ == "__main__":
    app()