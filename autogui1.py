import time
import pyautogui
message = 3
while message > 0 :
    time.sleep(1)
 # pyautogui.typewrite('Realme 10 seems the best one among those . The price ,the configuration seems amazing . All the phones are really unmatchable but Realme 10 is the unique one')
    time.sleep(2)
  #pyautogui.press("left")
    pyautogui.typewrite("Realme 10 seems the best one among those . The price ,the configuration seems amazing . All the phones are really unmatchable but Realme 10 is the unique one")
    current_x, current_y = pyautogui.position()

# Click at the current mouse pointer position
    pyautogui.click(x=current_x, y=current_y)
message = message - 1