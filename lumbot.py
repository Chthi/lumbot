"""
lumbot
use pixel color matching to detect a branches on the left and right
there is an animation time for branches to fall
if we cut branches on at the time we have to wait for the 
animation to play before looking at the pixels
instead we save the order of all visible branches on screen
and cut them in the same order without waiting for animation
if no branches are detected on left or right we wait a bit and retry
it means that the animation haven't finish to play
it is the case if the animation_time variable is to small

highest score : 938
"""

import pyautogui as gui
from time import sleep
import keyboard
import datetime

gui.PAUSE = 0

# colors of the inside of the branches
brown = (161,116,56)
# background color
white = (255,255,255)
# animation time of the branch falling
animation_time = 0.18

# restartX, restartY = 400, 732
# restartX, restartY = 800, 734
restartX, restartY = 960, 924
# increasing
# branches_posX = [367, 431]
# branches_posX = [735, -1]
branches_posX = [907, 1011]
# decreasing
# branches_posY = [441, 342, 243, 141]
branches_posY = [630, 530, 430, 330, 230, 130]

score_region = (889, 408, 1029-889, 470-408)

print("Press 's' to start playing.")
keyboard.wait("s")


def get_cut_order(img, branches_posX, branches_posY):
	cut_order = ['none'] * len(branches_posY)
	for branch in range(0, len(branches_posY)):
		# memorizing where all the visible branches on the left are
		if img.getpixel((branches_posX[0], branches_posY[branch])) == brown:
			cut_order[branch] = 'right'
		# we for branches on the right
		elif img.getpixel((branches_posX[1], branches_posY[branch])) == brown:
			cut_order[branch] = 'left'
		# if there is no branches anywhere this is because the animation hasn't finished to play
		else:
			# so we wait a little bit
			sleep(0.04)
			print("no branches !")
			return None
	return cut_order


def cut(cut_order):
	print("future orders", cut_order)
	# we cut everything we have in memory witout looking twice !
	for order in range(0, len(cut_order)):
		# because he cuts 2 by 2
		gui.press(cut_order[order])
		sleep(0.02)
		gui.press(cut_order[order])
		# sleep(0.01)


while not keyboard.is_pressed('q'):
	# starting to play
	gui.moveTo(restartX, restartY)
	gui.click()
	sleep(0.30)
	cut(['left'])
	sleep(animation_time)
	img = gui.screenshot()
	# img.show()
	print(img.getpixel((restartX, restartY)) == white)

	# when we lose the button to restart appears and the pixel is not white anymore
	while img.getpixel((restartX, restartY)) == white:
		cut_order = get_cut_order(img, branches_posX, branches_posY)
		if cut_order:
			cut(cut_order)
			sleep(animation_time)
		# we take only one screenshot at the end
		# after waiting for the scrolling down animation
		# so all branches will be placed right
		img = gui.screenshot()

	# at the end take and save a screenshot with the score
	img = gui.screenshot("highscores/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png", region=score_region)
	
