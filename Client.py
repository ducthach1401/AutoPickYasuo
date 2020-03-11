import pyautogui
import os
import time
def autopick():
	toado_timkiem=None
	toado_yasuo=None
	toado_khoa=None

	locate=os.getcwd()+"\\Data\\Client\\"
	locate_TimKiem=locate+"TimKiem.png"
	locate_yasuo=locate+"Yasuo.png"
	locate_khoa=locate+"Khoa.png"
	time_delay=0.01

	while toado_timkiem==None:
		toado_timkiem=pyautogui.locateCenterOnScreen(locate_TimKiem,confidence=0.75)
	pyautogui.click(toado_timkiem)
	pyautogui.write("ys")
	while toado_yasuo==None:
		toado_yasuo=pyautogui.locateCenterOnScreen(locate_yasuo,grayscale=True,confidence=0.75)
	pyautogui.click(toado_yasuo)


	while toado_khoa==None:
		toado_khoa=pyautogui.locateCenterOnScreen(locate_khoa,confidence=0.5)
	pyautogui.click(toado_khoa)

autopick()