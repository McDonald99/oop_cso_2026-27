class Rectangle:
    length = 8
    width = 4
    colour = "Blue"

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Colour: {self.colour}")

    def calc_area(self):
        area = self.length * self.width
        return area

if __name__ == "__main__":
    rect_one = Rectangle()
    print(f"Length: {rect_one.length}")
    print(f"Width: {rect_one.width}")
    print(f"Colour: {rect_one.colour}")

    rect_one.display()
    print(f"Rectangle area = {rect_one.calc_area()}")