from digitalio import DigitalInOut, Direction
import time
import board


class Cap:
    def __init__(self, pin_settings: tuple, timeout: int = 1e12, low_pass: bool = False):
        self.pin_settings = pin_settings
        self.timeout = timeout
        self.low_pass = low_pass

    def __init_pins(self, pin_settings: tuple) -> tuple:
        pins = []
        for pin_pair_number in pin_settings:
            w, r = map(DigitalInOut, pin_pair_number)
            w.direction = Direction.OUTPUT
            pins.append((w, r))
        return tuple(pins)

    def __deinit_pins(self) -> None:
        for pin_pair in self.pin_pairs:
            pin_pair[0].deinit()
            pin_pair[1].deinit()

    def __enter__(self):
        self.pin_pairs = self.__init_pins(self.pin_settings)
        return self

    def __exit__(self, exc_type, exc_value, tb) -> None:
        self.__deinit_pins()

    def __call__(self) -> tuple:
        values = []
        for i, pin_pair in enumerate(self.pin_pairs):
            w, r = pin_pair
            start = time.monotonic_ns()
            w.value = True
            while not r.value and time.monotonic_ns()-start < self.timeout:
                pass
            w.value = False
            cd = time.monotonic_ns()-start
            values.append(cd)
        return tuple(values)
