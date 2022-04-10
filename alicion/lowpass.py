class LowPass:
    def __init__(self):
        self.prev = None


    def __call__(self, values):
        if not self.prev is None:
            values2 = []
            for i, value in enumerate(values):
                values2.append(bool(all([value, self.prev[i]])))
            values = values2
        self.prev = values
        return values
