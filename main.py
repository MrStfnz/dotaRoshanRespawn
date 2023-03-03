"""
Simple PoC to check when Roshan is killed, once Aegis has been taken, it starts the 5 minute timer
After 5 minutes, in turbo, Roshan respawns, so this seems to be the ideal value.

Bear in mind that this is not the best method, but since Valve doesn't have anything 
for the dota2gsi that I can listen to for this specific event(roshan killed), this seems to be the only way.
"""

import time
import pytesseract
from PIL import ImageGrab
import winsound

#pytesseract.pytesseract.tesseract_cmd = "your\\pytesseract\\path"

# Set up the coordinates for the specific area. For 2560x1440 this is mine.
capture_area = (7, 1001, 504, 1038)

# Initialize the timer and sound variables
start_time = 0
end_time = 0
sound_played = True

while True:
    # Grab a screenshot of the game screen and use OCR
    screenshot = ImageGrab.grab(bbox=capture_area)
    text = pytesseract.image_to_string(screenshot)

    # Check if the "Aegis of the Immortal" message is present
    if "Aegis of the Immortal" in text and time.time() > end_time:
        # Look for aegis text
        start_time = time.time()
        end_time = start_time + 300
        sound_played = False

    if time.time() > end_time and not sound_played:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        sound_played = True

    if time.time() > end_time:
        # Reset the timer
        start_time = 0
        end_time = 0

    # Making sure I don't get a million temp files or pytesseract responds slow
    time.sleep(3)
