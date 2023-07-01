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

        menu = "1. Search for artist\n2. Search for album\n3. Search for song\n4. Return"
        console.print(Panel(menu, title="Search"), style="b magenta")
        opt = IntPrompt.ask("[b magenta]Do", choices=["1", "2", "3", "4"])

        # search for artists with special characters in their names (i.e. bjork)
        match opt:
            case 1:
                search_artist()
            case 2:
                search_album()
            case 3:
                search_song()
            case 4:
                os.system('clear')
                return ""

    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""


def search_artist():
    try:
        os.system('clear')
        artist_name = Prompt.ask("[b magenta]Artist name")
        subprocess.run(
            [f"mpc findadd artist '{artist_name}'"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""


def search_album():
    try:
        os.system('clear')
        album_name = Prompt.ask("[b magenta]Album name")
        subprocess.run(
            [f"mpc findadd album '{album_name}'"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""


def search_song():
    try:
        os.system('clear')
        song_name = Prompt.ask("[b magenta]Song name")
        subprocess.run(
            [f"mpc searchadd title '{song_name}'"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""

# go back to search menu if ctrl+c is pressed
