import os
import sys

def make_noise():
    if sys.platform == 'win32':
        import winsound
        freq = 1000
        dur = 500
        winsound.Beep(freq, dur)
    else:
        os.system('echo -e "\a"')

make_noise()
