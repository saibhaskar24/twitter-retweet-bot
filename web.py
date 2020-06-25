
import pyautogui
import time
while True:
		if pyautogui.locateCenterOnScreen('rt.PNG', confidence=0.3): 
			pyautogui.click(pyautogui.locateCenterOnScreen('rt.PNG', confidence=0.7),duration=1)
			pyautogui.scroll(-25)
		else:
			pyautogui.scroll(-300)#scroll down
			time.sleep(1)



