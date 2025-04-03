class Point:
    """
    Defines a point on the canvas.
    x=0 is the left of the screen
    y=0 is the top of the screen
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
