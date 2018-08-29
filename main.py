import pyautogui as pgui 
import sys,time,json
import urllib.request
import win32clipboard as cb
from bs4 import BeautifulSoup
import requests
import processing

#res = int(input("Select Quality (1-3):"))+2

pgui.hotkey('alt', 'tab')
time.sleep(1)
pgui.hotkey('ctrl', 'shift','c')
time.sleep(1)
pgui.typewrite('end')
time.sleep(1)
pgui.hotkey('ctrl','c')
time.sleep(1)
pgui.hotkey('ctrl', 'shift','i')

cb.OpenClipboard()
source = cb.GetClipboardData()
cb.CloseClipboard()

soup = BeautifulSoup(source,'html.parser')

image_url = soup.find("div",{"class","current-word__bottom"}).find_all("img")[0]['src']
urllib.request.urlretrieve(image_url,"image.jpg")

with open('palette.json','r') as data:
	clr_palette = json.load(data)

matrix = processing.get_image(5)
dictionary = processing.get_dot_instructions(matrix)

pgui.PAUSE = 0.03	

for key in dictionary:
	pgui.click(clr_palette[str(key)])
	start_pos = (0,0)
	last_pos = (0,0)
	cnt = 0
	for pixel in dictionary[key]:
		pgui.click(pixel)
