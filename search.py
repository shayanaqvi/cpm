import subprocess
import os
from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from rich.panel import Panel


def search():
    console = Console()
    try: 
        os.system('clear')
        # search for a specific song that may exist on multiple albums (i.e. kid a mnesia)

        menu = "1. Artist\n2. Album\n3. Song"
        console.print(Panel(menu, title="Search for"), style="b yellow")
        opt = IntPrompt.ask("[b cyan]Do:[/]", choices=["1", "2", "3"])

        # search for artists with special characters in their names (i.e. bjork)

        match opt:
            case 1:
                artist_name = Prompt.ask("[b cyan]Artist name[/]")
                subprocess.run(
                    [f"mpc findadd artist '{artist_name}'"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )
            case 2:
                album_name = Prompt.ask("[b cyan]Album name[/]")
                subprocess.run(
                    [f"mpc findadd album '{album_name}'"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )

            case 3:
                song_name = Prompt.ask("[b cyan]Song name[/]")
                subprocess.run(
                    [f"mpc searchadd title '{song_name}'"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )
            case _:
                console.print("Invalid option")

        os.system('clear')
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""
