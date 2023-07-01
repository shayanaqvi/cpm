import os
import time
import subprocess
from rich.prompt import IntPrompt
from rich.panel import Panel
from rich.console import Console
from rich.tree import Tree
from rich.layout import Layout
from rich.align import Align
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich import box
from browse import browse_library
from shuffle import shuffle_library
from search import search
from queue import queue


console = Console()




def main():
    try:
        os.system('clear')
        while True:
            menu = "1. Browse Library\n2. Shuffle Library\n3. Search\n4. Queue\n5. Currently Playing\n6. Exit"
            console.print(Panel(menu, title="Main Menu"), style="b yellow")

            opt = IntPrompt.ask("[b yellow]Do", default=1, choices=["1", "2", "3", "4", "5", "6"])

            match opt:
                case 1:
                    browse_library()
                case 2:
                    shuffle_library()
                case 3:
                    search()
                case 4:
                    queue()
                case 5:
                    current_song()
                case 6:
                    os.system('clear')
                    exit()
                case _:
                    os.system('clear')
                    console.print("Inavlid option")
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        exit()


def generate_panel():
    """Make a new panel."""
    csong = subprocess.run(
        ["mpc current -f %title%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    cartist = subprocess.run(
        ["mpc current -f %artist%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    calbum = subprocess.run(
        ["mpc current -f %album%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    queue_title = subprocess.run(
        ["mpc playlist -f %title%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    queue_album = subprocess.run(
        ["mpc playlist -f %album%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    queue_artist = subprocess.run(
        ["mpc playlist -f %artist%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    queue_length = subprocess.run(
        ["mpc playlist | wc -l"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    playback_status_mpc = subprocess.run(
        ["mpc status %state%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    current_time = subprocess.run(
        ["mpc status %currenttime%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout
    total_time = subprocess.run(
        ["mpc status %totaltime%"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    ).stdout


    queue_title_array = []
    for item in queue_title.split("\n"):
        queue_title_array.append(item)
    queue_album_array = []
    for item in queue_album.split("\n"):
        queue_album_array.append(item)
    queue_artist_array = []
    for item in queue_artist.split("\n"):
        queue_artist_array.append(item)

    del(queue_title_array[-1])
    del(queue_album_array[-1])
    del(queue_artist_array[-1])

    current_song = Text(justify="center", overflow="fold")
    current_album = Text(calbum.strip())
    current_artist = Text(cartist.strip())

    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].size = 9

    queue_table = Table(
        expand=True,
        box=box.SIMPLE_HEAD,
        row_styles=["green dim", "Bright_green"],
        border_style="green dim",
        header_style="green dim"
    )
    queue_table.add_column("#")
    queue_table.add_column("Title")
    queue_table.add_column("Album")
    queue_table.add_column("Artist")
    i = 0
    j = 0

    if csong == "":
        current_song.append("MPD not playing")
        panel = Panel("", title="MPD not playing", padding=3)
        layout["upper"].split(
            Layout(panel)
        )
        layout["lower"].split(
            Layout(Panel("", title="Queue is empty", padding=3))
        )
    else:
        for item in queue_title_array:
            if item == csong.strip():
                queue_table.add_row(Text(f"{str(i)}", style="green"), Text(item, style="cyan"), Text(queue_album_array[i], style="blue"), Text(queue_artist_array[j], style="magenta"), style="dim green")
                i += 1
                j += 1
                if i >= len(queue_album_array):
                    i = 0
                if j >= len(queue_artist_array):
                    j = 0
            else:
                queue_table.add_row(f"{str(i)}", item, queue_album_array[i], queue_artist_array[j])
                i += 1
                j += 1
                if i >= len(queue_album_array):
                    i = 0
                if j >= len(queue_artist_array):
                    j = 0

        if playback_status_mpc.strip() == "playing":
            playback_status = "Currently Playing"
        elif playback_status_mpc.strip() == "paused":
            playback_status = "Paused"
        
        current_song.append(csong.strip() + " - ", style="cyan")
        current_song.append(calbum.strip() + " - ", style="blue")
        current_song.append(cartist.strip(), style="magenta")
        current_song_panel = Panel(current_song, title=playback_status, subtitle=f"{str(current_time).strip()}/{str(total_time).strip()}",padding=3, border_style="green dim")
        layout["upper"].split(
            Layout(current_song_panel)
        )
        layout["lower"].split(
            Layout(Panel(queue_table, title=f"Queue ({str(queue_length).strip()})", style="green dim"))
        )

    return layout


def current_song():
    try:
        os.system('clear')
        with Live(generate_panel(), refresh_per_second=4) as live:
            while True:
                time.sleep(0.4)
                live.update(generate_panel())
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        return ""


main()
