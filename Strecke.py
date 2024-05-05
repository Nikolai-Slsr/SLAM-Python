class Strecke:
    A = [0, 0]
    B = [1, 1]

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
