import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program start on " + time.ctime())
while break_count <= total_breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=CU1k1UvM60Y")
    break_count = break_count + 1
