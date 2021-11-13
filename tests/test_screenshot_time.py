


import pyautogui as gui
from gtimeit import Benchmark


def screenshot():
	img = gui.screenshot()

def screenshot_region():
	img = gui.screenshot(region=(897, 120, 73, 814))

# def color_match():
# 	for y in range(0, 60, 10):
# 		gui.pixelMatchesColor(897+10, 120+y, (255, 255, 255))

def get_pixel():
	img = gui.screenshot(region=(897, 120, 73, 814))
	for y in range(0, 60, 10):
		img.getpixel((10, y)) == (255, 255, 255)




# bm = Benchmark()
# bm.add(screenshot)
# bm.add(screenshot_region)
# bm.add(get_pixel)
# bm.run(100)

# conclusion :
# 1) region argument do not speedup screenshot process
# it is juste a croping of a screenshot so it is actually a little bit slower
# 2) screenshot then multiples getpixel is good as it only takes one screenshot
# 3) screenshots takes around 30ms for me (100 ms in documentation)


from time import sleep

def sleep1():
	sleep(0.02)

def sleep2():
	sleep(0.01)
	sleep(0.01)

def sleep4():
	sleep(0.005)
	sleep(0.005)
	sleep(0.005)
	sleep(0.005)

bm = Benchmark()
bm.add(sleep1)
bm.add(sleep2)
bm.add(sleep4)
bm.run(100)

# sleep times smaller than 0.01 seems to actually be 0.01 anyway
# so minimum sleep time seems to be 0.01