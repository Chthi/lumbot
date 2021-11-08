import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='\n')
        # print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
