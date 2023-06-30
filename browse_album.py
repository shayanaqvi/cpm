import os
import subprocess
from rich import box
from rich.table import Table
from rich.console import Console
from rich.prompt import IntPrompt


console = Console()


def browse_album():
    try:
        os.system('clear')

        artist_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["yellow", "b yellow dim"],
            title="Artists",
        )
        artist_table.add_column("Index", no_wrap=True)
        artist_table.add_column("Title")

        artist_list = subprocess.run(
            ["mpc ls"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        ).stdout

        artist_list_array = []
        i = 1
        for line in artist_list.split("\n"):
            artist_list_array.append(line)

        del(artist_list_array[-1])

        for element in artist_list_array:
            artist_table.add_row(str(i), element)
            i += 1

        with console.pager(styles=True):
            console.print(artist_table)

        opt_artist = IntPrompt.ask("Select artist by index: ") - 1
        artist_selection = artist_list_array[opt_artist]

        os.system('clear')

        album_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["yellow", "b yellow dim"],
            title=f"Artists/{artist_selection}"
        )
        album_table.add_column("Index")
        album_table.add_column("Title")

        artist_album_list = subprocess.run(
            [f"mpc ls \"{artist_selection}\""],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        ).stdout

        artist_album_list_array = []
        j = 1
        for line in artist_album_list.split("\n"):
            artist_album_list_array.append(line)

        del(artist_album_list_array[-1])

        for element in artist_album_list_array:
            album_table.add_row(str(j), element)
            j += 1

        with console.pager(styles=True):
            console.print(album_table)

        opt_album = IntPrompt.ask("Select album by index: ") - 1
        album_selection = artist_album_list_array[opt_album]

        subprocess.run(
            [f"mpc add '{album_selection}'"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        os.system('clear')
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""