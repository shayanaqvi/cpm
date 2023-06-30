import subprocess
import os
from rich import box
from rich.table import Table
from rich.console import Console
from rich.prompt import IntPrompt
from rich.panel import Panel


console = Console()


def queue():
    try:
        os.system('clear')
        queue_table = Table(
            expand=True,
            box=box.ROUNDED,
            row_styles=["red", "b yellow"],
            title="Queue",
        )
        queue_table.add_column("Index")
        queue_table.add_column("Title")

        queue_list = subprocess.run(
            ["mpc playlist"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        ).stdout

        queue_list_array = []
        i = 1
        for line in queue_list.split("\n"):
            queue_list_array.append(line)

        del(queue_list_array[-1])

        for element in queue_list_array:
            queue_table.add_row(str(i), element)
            i += 1
        with console.pager(styles=True):
            console.print(queue_table)

        menu = "1. View queue\n2. Reorder queue\n3. Remove songs from queue\n4. Shuffle queue\n5. Clear queue"
        console.print(Panel(menu, title="Queue", subtitle="Press Ctrl+c to go back", style="b blue"))
        opt = IntPrompt.ask("t")

        match opt:
            case 1:
                view_queue(queue_table)
            case 2:
                pass
            case 3:
                pass
            case 4:
                shuffle_queue()
            case 5:
                clear_queue()

        os.system('clear')
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""


def shuffle_queue():
    subprocess.run(
        ["mpc shuffle"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    os.system('clear')


def clear_queue():
    subprocess.run(
        ["mpc clear"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    os.system('clear')


def view_queue(table):
    pass
#     with console.pager(styles=True):
#         console.print(table)

