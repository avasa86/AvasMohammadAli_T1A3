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
    insert_subject(subject)
    show_subject()

@app.command(short_help='adds a subject')
def add(first_name: str,last_name: str,email:str,age:int,phone_number:str,parents_phone_number:str,mark:int,subject_id:int):
    typer.echo(f"adding student details}")
    student = Student(first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id)
    insert_student(student)
    show_student()

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

@app.command()
def show_subject():
    student_list = get_all_students()
    console.print("[bold magenta]Subject[/bold magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("First Name", min_width=20)
    table.add_column("Last Name", min_width=20)
    table.add_column("Email",min_width=20)
    table.add_column("Age",min_width=5)
    table.add_column("Phone Number", min_width=20)
    table.add_column("Parent Phone Number",min_width=20)
    table.add_columng("Mark",min_width=10)
    table.add_column("Subject", min_width=20)
    for idx, student in enumerate(student_list, start=1):
        the_stud = str(subject)[1:-1]
        table.add_row(str(idx),the_stud)
    console.print(table)
if __name__ == "__main__":
    app()