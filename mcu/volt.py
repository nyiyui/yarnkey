from analogio import AnalogIn
import time
import board


class Volt:
    def __init__(self, pin_settings: tuple):
        self.pin_settings = pin_settings

    def __enter__(self):
        self.pins = tuple(AnalogIn(pin_setting) for pin_setting in self.pin_settings)
        return self

    def __exit__(self, exc_type, exc_value, tb) -> None:
        for pin in self.pins:
            pin.deinit()

    def __call__(self) -> tuple:
        return tuple(pin.value for pin in self.pins)
