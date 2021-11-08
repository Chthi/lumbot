# strike bot
# use pixel color matching to detect a branches on the left
# there is an animation time for branches to fall
# if we cut branches on at the time we have to wait for the 
# animation to play before looking at the pixels
# instead we save the order of all visible branches on screen
# and cut them in the same order without waiting

import pyautogui as gui
from time import sleep
import keyboard

gui.PAUSE = 0

# we can see 4 branches at the same time on screen
branches_number = 4
# ordre de coupe des branches
cut_order = ['no order'] * branches_number
# colors of the inside of the branches
brown = (161,116,56)
# background color
white = (255,255,255)
# animation time of the branch falling
animation_time = 0.18

# restartX, restartY = 400, 732
restartX, restartY = 800, 734
# increasing
# branches_posX = [367, 431]
branches_posX = [735, -1]
# decreasing
# branches_posY = [441, 342, 243, 141]
branches_posY = [446, 346, 246, 146]

print("Press 's' to start playing.")
keyboard.wait("s")

while not keyboard.is_pressed('q'):
	# starting to play
	gui.moveTo(restartX, restartY)
	gui.click()
	sleep(0.30)
	print(gui.pixelMatchesColor(restartX, restartY, white, tolerance=10))
	# when we lose the button to restart appears and the pixel is not white anymore
	while gui.pixelMatchesColor(restartX, restartY, white, tolerance=10):
		for branch in range(0, branches_number):
			# saving all visible branches on the left
			if gui.pixelMatchesColor(branches_posX[0], branches_posY[branch], brown, tolerance=10):
				cut_order[branch] = 'right'
			else:
				cut_order[branch] = 'left'
			# no need to look for branches on the right

		print("future orders", cut_order)
		# we cut everything we have in memory witout looking twice !
		for order in range(0, branches_number):
			# because he cuts 2 by 2
			gui.press(cut_order[order])
			sleep(0.02)
			gui.press(cut_order[order])
		sleep(animation_time)
