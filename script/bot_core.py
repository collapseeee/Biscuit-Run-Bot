# bot_core.py
import subprocess
import numpy as np
import cv2
import time
import random

def capture_screen(device):
    result = subprocess.run(
        ["adb", "-s", device, "exec-out", "screencap", "-p"],
        capture_output=True
    )
    img_array = np.frombuffer(result.stdout, dtype=np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_COLOR)

def find_template(screen, template_path, threshold=0.85):
    template = cv2.imread(template_path)
    if template is None:
        raise FileNotFoundError(template_path)
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        h, w = template.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y, max_val)
    return None

def tap(x, y, device):
    subprocess.run(["adb", "-s", device, "shell", "input", "tap", str(x), str(y)])

def wait(a=0.8, b=1.6):
    time.sleep(random.uniform(a, b))