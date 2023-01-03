from Boot.login import*

running = True
while running:
    check_username()
    if not on_boot():
        running = False