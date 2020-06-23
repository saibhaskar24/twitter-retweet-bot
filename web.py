# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
import pyautogui
import time

# options = webdriver.ChromeOptions() 
# options.add_argument("user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data") 
# browser = webdriver.Chrome(executable_path='chromedriver',chrome_options=options) 
# url = "https://twitter.com/"
# hashtag = '#dscomg'
# browser.get(url)
# print("Done")
while True:
		if pyautogui.locateCenterOnScreen('rt.PNG', confidence=0.7): 
			pyautogui.click(pyautogui.locateCenterOnScreen('rt.PNG', confidence=0.7),duration=1)
			pyautogui.scroll(-25)
		else:
			# pyautogui.moveTo(650,150)
			pyautogui.scroll(-300)#scroll down
			time.sleep(1)


# like_it = '''section.css-1dbjc4n > div:nth-child(2) > div:nth-child(1) > 
# div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
# > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) >
# div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'''

# print("Opened")

# # like 1st tweet timeline user.
# browser.find_element_by_css_selector('button[class="ProfileTweet-actionButton js-actionButton js-actionFavorite"]').click()
# browser.find_element_by_xpath(xpath)
# browser.find_element_by_xpath(f"/{xpat}[@d={svgpath}]")
# browser.click






