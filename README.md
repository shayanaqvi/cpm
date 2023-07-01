# CPM
CPM is a terminal frontend for MPC, built in Python using the [Rich](https://github.com/Textualize/rich) library. It is unfinished and will likely remain so.
## Dependencies
The following is needed to run CPM:
- Python
- MPD
  - MPC
- Rich (`pip install rich`)
### Optional
- Bat (for a more prettified library viewing experience)
### MPD
This requires a working MPD setup. [Here](https://forum.endeavouros.com/t/beginner-s-guide-to-setting-up-and-using-mpd/16831) is a decent getting-started guide.
## Running the app
For now, simply run `main.py` and follow the prompts. You can press Ctrl+c in most places to go back, abort an operation or exit the app.
## Issues
- [ ] Search is iffy
  - It can't differentiate between songs of the same name that are on different albums (i.e. a song like "Pyramid Song" exists on the albums "Amnesiac" and "Kid A Mnesiac").
  - Searching for artists with special characters in their names requires typing that special character (i.e. Sigur Rós). I'm not entirely sure if there is a workaround for this.
- [ ] Using Ctrl+c in the pager causes glitching
- [ ] The Queue in the Currently Playing screen needs consume mode to work properly
