import typer
from typing import Optional
from pathlib import Path

def  main(extension: str,
          directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel cherche."),
          delete: bool = typer.Option(False, help="Supprime les fichiers trouver.")):
    """"
    Afficher les fichiers trouver avec l'extension donnee.
    """
    if not directory:
        directory = Path.cwd()
        print(directory)


if __name__== "__main__" :
    typer.run(main)
