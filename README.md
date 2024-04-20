# Screenshot with mouse select for python
I couldn't find any native python code which takes partial screenshot via mouse selection. 

All examples I could find either using scrot, gnome-screenshot, pyautogui, qt, gtk, etc.

This project uses only pillow and tkinter and just for learning purposes, feel free to use it.

## Installation
1. Download the file *screenshot.py*, and unpack it somewhere.
2. Install ```python3-tkinter``` and ```python3-pillow``` if they are not. Use repository of your distro for tkinter.
3. Make sure it is executable, either by right click-properties or typing ```chmod 755 screenshot.py``` in your terminal.
4. Script saves pictures to ```/home/<user>/Pictures```, change it if you want.
5. Double click to ```screenshot.py``` to run the program or use terminal.
6. Left click and drag mouse to select area. Right click to save partial screenshot. Middle click exits program.
7. If no area is selected, full screenshot will be saved within right click.
8. In case you see a transparency tint on your screenshots, increase ```root.after(value)``` at line #47.

## Notes
Although I have wrote most of codes myself there are some copy+paste too.
There are some codes from which I had forgot where I gathered.
Please don't get mad if I didn't mentioned about your name.

Regards
