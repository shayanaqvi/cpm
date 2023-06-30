import os
from rich.prompt import IntPrompt
from rich.panel import Panel
from rich.console import Console
from browse import browse_library
from shuffle import shuffle_library
from search import search
from queue import queue


def main():
    console = Console()

    try:
        os.system('clear')
        while True:
            menu = "1. Browse Library\n2. Shuffle Library\n3. Search\n4. Queue"
            console.print(Panel(menu, title="Main Menu", subtitle="Press Ctrl+C to exit"), style="b yellow")

            opt = IntPrompt.ask("[b yellow]Do", default=1, choices=["1", "2", "3", "4"])

            match opt:
                case 1:
                    browse_library()
                case 2:
                    shuffle_library()
                case 3:
                    search()
                case 4:
                    queue()
                case _:
                    os.system('clear')
                    console.print("Inavlid option")
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        exit()


main()
