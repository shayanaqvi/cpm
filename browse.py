import os
from rich.prompt import IntPrompt
from rich.console import Console
from rich.panel import Panel
from browse_artist import browse_artist
from browse_album import browse_album
from browse_song import browse_song


console = Console()


def browse_library():
    try:
        os.system('clear')
        while True:
            menu = "1. Browse by artist\n2. Browse by album\n3. Browse by song\n4. Return"
            console.print(Panel(menu, title="Browse Library", subtitle="Press Ctrl+c to go back", style="b red"))

            opt = IntPrompt.ask("[b red]Do", default=3, choices=["1", "2", "3", "4"])

            match opt:
                case 1:
                    browse_artist()
                case 2:
                    browse_album()
                case 3:
                    browse_song()
                case 4:
                    os.system("clear")
                    return ""
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""

# navigate backwards
