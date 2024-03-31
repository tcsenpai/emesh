import itertools
import threading
import time
import sys

done = True
message = ""
#here is the animation
def animate():
    global done
    global message
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + message + ' ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

def start(msg="loading..."):
    global done
    global message
    done = False
    message = msg
    t = threading.Thread(target=animate)
    t.start()

def stop():
    global done
    done = True
