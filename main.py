from script.bot_task import run
from script.capture_template import capture_screen
from script.file_process import clear_img_folder

PORTLIST = [16416]

# Clear the img folder before starting capture
clear_img_folder()

for port in PORTLIST:
    capture_screen("127.0.0.1:" + str(port))
    run("127.0.0.1:" + str(port))
