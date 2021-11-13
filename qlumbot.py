"""
simplest bot
use pixel color matching to detect a branch on the direct left

highest score : 402
"""

import pyautogui as gui
from time import sleep

gui.PAUSE = 0

sleep(1)
while True:
	# aim at a brown pixel in the left branch lowest position   
	if gui.screenshot().getpixel((907, 630)) == (161,116,56):
		gui.press('right')
		sleep(0.02)
		gui.press('right')
	else:
		gui.press('left')
		sleep(0.02)
		gui.press('left')
	sleep(0.20)
