# breaking bot
# this bot cut the branches so fast that the game actually breaks... 

# highest score : 40

import pyautogui as gui
from time import sleep
import keyboard
import datetime

gui.PAUSE = 0

# we can see 4 branches at the same time on screen
branches_number = 6
# ordre de coupe des branches
cut_order = ['no order'] * branches_number
# colors of the inside of the branches
brown = (161,116,56)
# background color
white = (255,255,255)
# animation time of the branch falling
animation_time = 0.8

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

print("Press 's' to start playing.")
keyboard.wait("s")

while not keyboard.is_pressed('q'):
	# starting to play
	gui.moveTo(restartX, restartY)
	gui.click()
	sleep(0.30)
	img = gui.screenshot()
	# img.show()
	print(img.getpixel((restartX, restartY)) == white)

	# when we lose the button to restart appears and the pixel is not white anymore
	while img.getpixel((restartX, restartY)) == white:
		for branch in range(0, branches_number):
			# memorizing where all the visible branches on the left are
			if img.getpixel((branches_posX[0], branches_posY[branch])) == brown:
				cut_order[branch] = 'right'
			else:
				cut_order[branch] = 'left'
			# no need to look for branches on the right

		print("future orders", cut_order)
		# we cut everything we have in memory witout looking twice !
		for order in range(0, branches_number):
			# because he cuts 2 by 2
			gui.press(cut_order[order])
			gui.press(cut_order[order])
		# we take only one screenshot at the end
		# after waiting for the scrolling down animation
		# so all branches will be placed right
		sleep(animation_time)
		img = gui.screenshot()
	# at the end take and save a screenshot with the score
	img = gui.screenshot("highscores/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png")
	
