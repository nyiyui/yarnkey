class Directional:
    def __init__(self, time_threshold):
        self.time_threshold = time_threshold
        self.__reset()

    def __reset(self):
        self.pressed = set()
        self.res = []
        self.elapsed = 0

    def __call__(self, t, values):
        if not any(values) and self.elapsed > self.time_threshold:
            ret = tuple(self.res)
            self.__reset()
            return ret

        for i, value in enumerate(values):
            if value and i not in self.pressed:
                self.pressed.add(i)
                self.res.append(i)
        self.elapsed += t
        #print(self.pressed, self.res, self.elapsed, self.elapsed > self.time_threshold)
        return []
