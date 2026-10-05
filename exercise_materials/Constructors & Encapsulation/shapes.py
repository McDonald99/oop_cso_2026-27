class Rectangle:
    length = 10
    width = 5
    colour = "blue"

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]")

    def calc_area(self):
        return self.length * self.width

    def __init__(self, length, width, colour="blue"):
        self.length = length
        self.width = width
        self.colour = colour

if __name__ == "__main__":
    import random

    rect_list = []

    for i in range(5):
        rand = random.randint(1,10)
        r_length = input("Enter rectangle length: ")
        r_width = input("Enter rectangle width: ")
        if rand % 2 == 0:
            r_colour = input("Enter rectangle colour: ")
            rect = Rectangle(r_length, r_width, r_colour)
        else:
            rect = Rectangle(r_length, r_width)
        rect_list.append(rect)

    print(rect_list)