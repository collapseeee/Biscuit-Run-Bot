import subprocess
import cv2

def capture_screen(device):
    result = subprocess.run(
        ["adb", "-s", device, "shell", "screencap", "-p", "/sdcard/screen.png"],
    )
    subprocess.run(["adb", "-s", device, "pull", "/sdcard/screen.png", "temp_screen.png"])
    return cv2.imread("temp_screen.png")

img = capture_screen()
print("Draw a box around the element, press ENTER/SPACE to confirm, ESC to cancel")
x, y, w, h = cv2.selectROI("Select template", img, showCrosshair=True)
cv2.destroyAllWindows()

if w > 0 and h > 0:
    crop = img[y:y+h, x:x+w]
    name = input("Save as (e.g. mailbox_icon.png): ")
    cv2.imwrite(f"templates/{name}", crop)
    print(f"Saved templates/{name} — location was x={x}, y={y}, w={w}, h={h}")

