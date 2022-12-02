
```python
import pyautogui
import time
while True:
    for i in range(0,10):
        x, y = pyautogui.position()
        pyautogui.moveTo(x+1,y)
    time.sleep(15)
print('perro')
```
