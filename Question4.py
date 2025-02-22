class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the Rectangle instance with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Return an iterator that first yields length and then width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Input: Take length and width as input from the user
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Create a Rectangle instance
rect = Rectangle(length, width)

# Output: Iterate over the Rectangle instance and print the result
for item in rect:
    print(item)
