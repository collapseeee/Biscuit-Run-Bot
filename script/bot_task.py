# run_bot.py
from bot_core import capture_screen, find_template, tap, wait

TEMPLATES = "templates/"

def do_mailbox(device):
    screen = capture_screen(device)
    match = find_template(screen, TEMPLATES + "mailbox_icon.png")
    if match:
        tap(match[0], match[1], device)
        wait()
        screen = capture_screen(device)
        claim = find_template(screen, TEMPLATES + "claim_all_btn.png")
        if claim:
            tap(claim[0], claim[1], device)
            wait()
            print("Mailbox claimed.")
            return True
    print("Mailbox step skipped (icon/button not found).")
    return False

def go_to_gacha(device):
    screen = capture_screen(device)
    match = find_template(screen, TEMPLATES + "gacha_icon.png")
    if match:
        tap(match[0], match[1], device)
        wait(1.2, 2.0)  # gacha screens often have transition animations
        return True
    print("Could not find gacha icon.")
    return False

def pull_gacha(device):
    screen = capture_screen(device)
    match = find_template(screen, TEMPLATES + "pull_btn.png")
    if match:
        tap(match[0], match[1], device)
        wait(1.5, 2.5)  # allow pull animation to play out
        return True
    return False

def check_target_item(device):
    screen = capture_screen(device)
    match = find_template(screen, TEMPLATES + "target_item.png", threshold=0.85)
    return match is not None

def run(device):
    do_mailbox(device)

    if not go_to_gacha(device):
        print("Aborting — couldn't reach gacha screen.")
        return

    max_pulls = 200  # safety cap so it doesn't run forever
    for i in range(max_pulls):
        print(f"Pull attempt {i+1}...")
        pulled = pull_gacha(device)
        if not pulled:
            print("Pull button not found — may need to dismiss a popup. Stopping.")
            break

        wait(1.0, 1.5)  # let result screen settle
        if check_target_item(device):
            print(f"Target item found on attempt {i+1}. Stopping.")
            break
    else:
        print("Reached max pull cap without finding item.")
