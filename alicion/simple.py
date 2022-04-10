import time


def in_range(pairs: list):
    def f(values):
        if len(pairs) != len(values):
            raise TypeError('length of values and pairs mismatched')
        return tuple(pairs[i][0] < value < pairs[i][1] for i, value in enumerate(values))
    return f


class Timeout:
    def __init__(self, time_threshold):
        self.time_threshold = time_threshold
        self.__reset()

    def __reset(self):
        self.pressed = set()
        self.res = []
        self.elapsed = 0

    def __call__(self, dt, values):
        if not any(values) and self.elapsed > self.time_threshold:
            ret = tuple(self.res)
            self.__reset()
            return len(ret) != 0, self.elapsed, ret

        for i, value in enumerate(values):
            if value and i not in self.pressed:
                self.pressed.add(i)
                self.res.append(i)
        if not any(values):
            self.elapsed += dt # incr time if not touching
        else:
            self.elapsed = 0

        return False, self.elapsed, tuple(self.res)
