import webbrowser
import time

breakTime = 1
while (breakTime < 4):
    time.sleep(10)
    print breakTime
    webbrowser.open("youtube.com")
    breakTime = breakTime + 1
