from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction
import time
import json
import gc
import board
#from cap import Cap
from volt import Volt
#from debug import Debug
from keyboard import Keyboard
from simple import in_range, Timeout
#from lowpass import LowPass
#from directional import Directional
import adafruit_dotstar
from data import keys


led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
d = {'o': True, '.': False}
ds = {True: 'o', False: '.'}


r = in_range([(-1, 40e3)]*6)
to = Timeout(100 * 1e6)

def index(a: list, v) -> int:
    for i in range(len(a)):
        if v == a[i]:
            return str(i)
    return '-'

print('meta {"version":"alicion-v2.8","board":"'+board.board_id+'"}')

with Volt((board.A0, board.A1, board.A2, board.A3, board.A4, board.D2)) as first:
    with Keyboard(dry_run=False, keys=keys) as out:
        gc.collect()
        led[0] = (255, 0, 0)
        oc = []
        t_prev = time.monotonic_ns()
        while 1:
            t_curr = time.monotonic_ns()
            t_diff = t_curr-t_prev
            a = first()
            gc.collect()
            b = r(a)
            ca, ct, c = to(t_diff, b) #c activate
            if c != oc:
                print('frame '+json.dumps({
                    'ca': ca,
                    'ct': ct,
                    'c': c,
                }))
                print('raw start')
                print(f'{index(c, 5)}{index(c, 4)}')
                print(f'{index(c, 3)}{index(c, 2)}')
                print(f'{index(c, 1)}{index(c, 0)}')
                print('raw end')
                oc = c
                led[0] = (0, 0, 255)
                time.sleep(0.1)
            if ca:
                print('commit '+json.dumps(c))
                d = out(c)
                led[0] = (0, 255, 0)
                time.sleep(0.1)
            t_prev = t_curr
