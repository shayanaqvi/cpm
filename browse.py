import os
import subprocess
from rich import print, box
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.console import Console


def browse_library():
    console = Console()

    artist_table = Table(
        expand=True,
        box=box.ROUNDED,
        row_styles=["yellow", "b yellow dim"],
        title="Library",
        caption="Press q to exit",
    )
    artist_table.add_column("Index", style="magenta", no_wrap=True)
    artist_table.add_column("Title", style="yellow")

    try:
        os.system('clear')
        album_list_ugly = subprocess.run(
            ["mpc list album group artist"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        artist_list_ugly = subprocess.run(
            ["mpc list artist"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        album_list = album_list_ugly.stdout
        artist_list = artist_list_ugly.stdout

        album_list_array = []
        artist_list_array = []

        for line in album_list.split("\n"):
            album_list_array.append(line)
        for line in artist_list.split("\n"):
            artist_list_array.append(line)
        del(album_list_array[-1])

        i = 1
        for album in album_list_array:
            artist_table.add_row(str(i), album)
            i += 1

        with console.pager(styles=True):
            console.print(artist_table)

        user_selection = IntPrompt.ask("[b cyan]Choose by index[/]") 
        final_selection = album_list_array[user_selection - 1].strip()

        add_or_replace_queue = Prompt.ask("[b cyan](A)ppend to queue or (r)eplace queue?[/]", default="a", choices=["a", "r"])

        match add_or_replace_queue:
            case "a":
                if final_selection in artist_list_array:
                    subprocess.run(
                        [f"mpc findadd artist '{final_selection}'"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True
                    )
                else:
                    subprocess.run(
                        [f"mpc findadd album '{final_selection}'"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True
                    )
            case "r":
                subprocess.run(
                    ["mpc clear"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )
                if final_selection in artist_list_array:
                    subprocess.run(
                        [f"mpc findadd artist '{final_selection}'"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True
                    )
                else:
                    subprocess.run(
                        [f"mpc findadd album '{final_selection}'"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True
                    )

            case _:
                print("Invalid option")
        os.system('clear')
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""
