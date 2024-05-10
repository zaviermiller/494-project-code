import subprocess
import time
import pyautogui
import json

def parse_stdout(text):
  fpses = []
  max_fps = 0
  min_fps = 1000
  lines = text.split("\n")
  for line in lines[10:]:
    try:
      fps = int(line)
      fpses.append(fps)
      max_fps = max(max_fps, fps)
      min_fps = min(min_fps, fps)
    except:
      pass
  
  print(f"Max FPS: {max_fps}")
  print(f"Min FPS: {min_fps}")
  print(f"Average FPS: {sum(fpses) / len(fpses)}")


def hold_key(key, duration):
  pyautogui.keyDown(key)
  time.sleep(duration)
  pyautogui.keyUp(key)

# run the mc clone
p = subprocess.Popen(["scalene", "pycraft/__main__.py", "--memory", "--cli", "--json", "--outfile", "profile.json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# wait for the game to load
time.sleep(5)

# move forward for 10 seconds
hold_key("w", 5)
pyautogui.rightClick()
pyautogui.rightClick()

pyautogui.press('tab')
hold_key("space", 1)
hold_key("w", 31)
pyautogui.press('tab')
time.sleep(3)

pyautogui.move(0, 500)

for i in range(10):
  pyautogui.click()

time.sleep(1)


pyautogui.press('esc')
pyautogui.moveTo(1345, 255)
pyautogui.click()


# get stdout and print
text = p.stdout.read()

parse_stdout(text.decode("utf-8"))

## get the memory information
d = None
with open("profile.json", "r") as f:
  d = json.load(f)

py_mem = 0
native_mem = 0

for file in d['files']:
  for line in d['files'][file]['lines']:
    py_mem += line['n_peak_mb']

print(py_mem)