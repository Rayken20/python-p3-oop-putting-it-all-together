class Shoe:
    """Represents a shoe with a brand and size."""

    def __init__(self, brand: str, size: int):
        if not isinstance(size, int):
            print("size must be an integer")
    
        else:
            self.brand = brand
            self.size = size

    def cobble(self):
        print("Your shoe is as good as new!\n")
        self.condition = "New"
