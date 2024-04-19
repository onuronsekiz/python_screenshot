#!/usr/bin/env python

from PIL import Image, ImageGrab
from datetime import datetime
import tkinter as tk
import os

root = tk.Tk()

# Set Variables
rect_id = None
topx, topy, botx, boty = 0, 0, 0, 0

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Get mouse position function
def get_mouse_posn(event):
	global topy, topx

	topx, topy = event.x, event.y

#Update selection rectangle function
def update_sel_rect(event):
	global topy, topx, botx, boty, rect_id

	botx, boty = event.x, event.y
	canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.

#Get screenshot function
def get_screenshot(event):
	global root
	global topx, topy, botx, boty

	if topx > botx: # If mouse drag was right to left
		topx, botx = botx, topx # Correction for coordinates

	if topy > boty: # If mouse drag was bottom to top
		topy, boty = boty, topy # Correction for coordinates
	
	if topx == botx and topy == boty: # If no selection was made
		topx, topy = 0, 0
		botx, boty = screen_width, screen_height # Coordinates for fullscreen

	root.destroy() # Destroy tkinter, otherwise a transparent window will be on top of desktop
	root.after(10) ##### Wait for tkinter destruction, increase if you see a tint in your screenshots
	filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.png') #filename determine
	path = os.path.join(os.path.expanduser('~'),"Pictures",filename) #save file to /home/<user>/Pictures
	img = ImageGrab.grab(bbox=(topx, topy, botx, boty)) # Actual screenshot
	img.save(path) #Screenshot save to file

#Create root window
root_geometry = str(screen_width) + 'x' + str(screen_height) #Creates a geometric string argument
root.geometry(root_geometry) #Sets the geometry string value

root.overrideredirect(True)
root.wait_visibility(root)
root.attributes("-alpha", 0.25) #Set windows transparent

#Create canvas on root windows
canvas = tk.Canvas(root, width=screen_width, height=screen_height) #Create canvas
canvas.config(cursor="cross") #Change mouse pointer to cross
canvas.pack()

# Create selection rectangle (invisible since corner points are equal).
rect_id = canvas.create_rectangle(topx, topy, topx, topy, dash=(8,8), fill='gray', outline='')

canvas.bind('<Button-1>', get_mouse_posn) #Left click gets mouse position
canvas.bind('<B1-Motion>', update_sel_rect) #Mouse drag updates selection area
canvas.bind('<Button-3>', get_screenshot) #Right click gets screenshıt, no selection will result full
canvas.bind('<Button-2>', lambda x: root.destroy()) #Quit without screenshot with middle click

root.mainloop()
