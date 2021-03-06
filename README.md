# SketchLeagueBot
Bot that plays Sketch League written in Python using pyautogui

***Update: Unfortunately, as of 2/15/2020, Sketch League went offline :(***<br>
*This project still features some useful image processing tools though!*

<h2>Implementation Details</h2>

Coded entirely in Python using the popular module, pyautogui. The bot scrapes the website for the image and downloads it. It processes the image into a lower resolution using average RGB value, and matches them to the closest palette colour (RGB difference) available in Sketch League. It then draws each pixel rapidly (roughly 100 pixels/second). 

To set up the bot, run the file *inital_setup.py* and click each of the colours on the palette starting with the top left colour and moving down each column (top to bottom first before moving to next column).

Make sure to set the brushsize to 1 tick above the small option before running the bot. The bot will start by alt-tabbing so make sure that the browser with sketch league is the last visited screen (so alt-tab will switch to it).

<h2>License</h2>

Copyright (c) 2018 Derek Zhang, Dereck Tu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
