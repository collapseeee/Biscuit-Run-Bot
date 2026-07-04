from capture import capture_screen, clear_img_folder

PORTLIST = [16416]

# Clear the img folder before starting capture
clear_img_folder()

for port in PORTLIST:
    capture_screen("127.0.0.1:" + str(port), f"img/cache/check{port}.png")
