class Culminate:
    def __init__(self):
        self.values = None

    def __call__(self, values):
        if self.values is None:
            self.values = values
            return values
        if not any(values):
            fake = [False] * len(values)
            values = self.values
            self.values = fake
            return values
        values2 = []
        fake = [False] * len(values)
        for i, value in enumerate(values):
            values2.append(bool(any([value, self.values[i]])))
        self.values = values2
        return fake
