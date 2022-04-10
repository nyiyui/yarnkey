import usb_hid
from adafruit_hid.keyboard import Keyboard as Kb
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


class Keyboard:
    def __init__(self, dry_run: bool = False, keys: dict = {}):
        self.dry_run = dry_run
        self.keys = keys
        self.kbd = None
        self.lay = None

    def __enter__(self):
        self.kbd = Kb(usb_hid.devices)
        self.lay = KeyboardLayoutUS(self.kbd)
        return self

    def __exit__(self, exc_type, exc_value, tb) -> None:
        pass

    def __call__(self, values):
        kcs = self.keys.get(tuple(values), [])
        if self.dry_run:
            if len(kcs) != 0:
                print(kcs)
        else:
            self.kbd.send(*kcs)
        return values
