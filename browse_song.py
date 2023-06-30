import subprocess
import os
from rich import box
from rich.table import Table
from rich.console import Console
from rich.prompt import IntPrompt


console = Console()


def browse_song():
    try:
        os.system('clear')

        artist_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["blue dim", "bright_blue"],
            border_style="blue dim",
            title="Artists",
            title_style="blue on default",
            header_style="blue dim"
        )
        artist_table.add_column("Index")
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

        opt_artist = IntPrompt.ask("[b blue]Select artist by index: ") - 1
        artist_selection = artist_list_array[opt_artist]

        os.system('clear')

        album_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["cyan dim", "bright_cyan"],
            border_style="cyan dim",
            title_style="cyan on default",
            header_style="cyan dim",
            title=f"Artists/{artist_selection}",
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

        opt_album = IntPrompt.ask("[b cyan]Select album by index: ") - 1
        album_selection = artist_album_list_array[opt_album]

        os.system('clear')

        song_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["green dim", "bright_green"],
            border_style="green dim",
            title_style="green on default",
            header_style="green dim",
            title=f"Artists/{album_selection}",
        )
        song_table.add_column("Index")
        song_table.add_column("Title")

        artist_album_song_list = subprocess.run(
            [f"mpc ls \"{album_selection}\""],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        ).stdout

        artist_album_song_list_array = []
        k = 1
        for line in str(artist_album_song_list).split("\n"):
            artist_album_song_list_array.append(line)

        del(artist_album_song_list_array[-1])

        for element in artist_album_song_list_array:
            song_table.add_row(str(k), element)
            k += 1

        with console.pager(styles=True):
            console.print(song_table)

        opt_song = IntPrompt.ask("[b green]Select track by index: ") - 1
        song_selection = artist_album_song_list_array[opt_song]
        subprocess.run(
          [f"mpc add \"{song_selection}\""],
          shell=True,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          universal_newlines=True
        ).stdout

        os.system('clear')
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""
