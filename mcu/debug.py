class Debug:
    """
    Prints the given values to console.
    """
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb) -> None:
        pass

    def __call__(self, values):
        print(values)
        print(''.join(list({True:'o', False:'-'}[value[0]] for value in values)))
