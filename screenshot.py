#!/usr/bin/env python

from PIL import Image, ImageGrab
from datetime import datetime
import tkinter as tk
import os

root = tk.Tk()

########################## Set Variables ##########################
rect_id = None
topx, topy, botx, boty = 0, 0, 0, 0

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def get_mouse_posn(event):
	global topy, topx

	topx, topy = event.x, event.y

def update_sel_rect(event):
	global topy, topx, botx, boty, rect_id

	botx, boty = event.x, event.y
	canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.

def get_screen_shot(event):
	global root
	global topx, topy, botx, boty

	if topx > botx:
		topx, botx = botx, topx

	if topy > boty:
		topy, boty = boty, topy
	
	if topx == botx and topy == boty:
		topx, topy = 0, 0
		botx, boty = screen_width, screen_height

	root.destroy()
	root.after(10)
	img = ImageGrab.grab(bbox=(topx, topy, botx, boty))
	filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.png')
	path = os.path.join(os.path.expanduser('~'),"Pictures",filename) #save file to /home/<user>/Pictures
	img.save(path)

root_geometry = str(screen_width) + 'x' + str(screen_height) #Creates a geometric string argument
root.geometry(root_geometry) #Sets the geometry string value

root.overrideredirect(True)
root.wait_visibility(root)
root.attributes("-alpha", 0.25) #Set windows transparent

canvas = tk.Canvas(root, width=screen_width, height=screen_height) #Create canvas
canvas.config(cursor="cross") #Change mouse pointer to cross
canvas.pack()

# Create selection rectangle (invisible since corner points are equal).
rect_id = canvas.create_rectangle(topx, topy, topx, topy, dash=(8,8), fill='gray', outline='')

canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)
canvas.bind('<Button-3>', get_screen_shot) #trigger with right click, not selected will result full screenshot
canvas.bind('<Button-2>', lambda x: root.destroy()) #quit without screenshot with middle click

root.mainloop()
