import pyautogui as pgui
import json,time,pyHook,pythoncom,sys

palette = {}
cnt = 1

print ("Click on each of the colours on the right side, starting from the top left. Go down each column from top to bottom.")

def onclick(event):
	global cnt,palette
	palette[cnt] = event.Position
	print("clicked")
	cnt+=1
	if cnt > 21:
		with open('palette.json', 'w') as outfile:
			json.dump(palette, outfile)
		sys.exit()
	return True

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()



