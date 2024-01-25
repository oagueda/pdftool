import typer
from typing import List
from typing_extensions import Annotated
from pypdf import PdfWriter
from rich import print as rprint
app = typer.Typer()

def main():
    app()

@app.command()
def join(
    pdfs:Annotated[List[str], typer.Argument(help="PDFs to join in wanted order. Last is new pdf name")],
    v: Annotated[bool, typer.Option(help="Verbose.")] = False,
    ):
    if v:
        print(f"Joining pdfs {pdfs}")
    merger = PdfWriter()
    errors = 0
    for i in range(len(pdfs)-1):
        pdf = pdfs[i]
        try:
            merger.append(pdf)
        except FileNotFoundError as e:
            if v:
                rprint(f"[red bold]{e.strerror} {e.filename}[/red bold]")
            errors = errors + 1
            if errors == len(pdfs)-1:
                if v:
                    rprint("[red bold]Unable to join any pdf[/red bold]")
                merger.close()
                return
    if(errors>0 and v):
        rprint("[yellow]Unable to join some of the pdf[/yellow]")
    merger.write(pdfs[len(pdfs)-1])
    merger.close()

if __name__ == "__main__":
    main()
