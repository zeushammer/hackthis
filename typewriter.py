###
### script for printing text as-if typed
###

import time, sys

def typewrite(pace,text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(pace)
    print "\n"

