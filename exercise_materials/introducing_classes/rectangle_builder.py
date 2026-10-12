from shapes import Rectangle

def find_greatest_area(rect_list):
    max_area = -1
    biggest = None

    for rect in rect_list:
        if rect.calc_area() > max_area:
            max_area = rect.calc_area()
            biggest = rect

    return biggest

def find_smallest_width(rect_list):
    smallest_width = 9999
    sw_rect = None

    for rect in rect_list:
        if rect.width < smallest_width:
            smallest_width = rect.width
            sw_rect = rect

    return sw_rect

def find_red_rect(rect_list):
    red_rects = []

    for rect in rect_list:
        if rect.colour.lower() == "red":
            red_rects.append(rect)

    return red_rects

if __name__ == "__main__":
    rectangles = []

    for i in range(5):
        # Create new default Rectangle
        rect = Rectangle()
        # Take in details for new Rectangle
        length = float(input(f"Enter length of rectangle {(i+1)}: "))
        width = float(input(f"Enter width of rectangle {(i + 1)}: "))
        colour = input(f"Enter colour of rectangle {(i + 1)}: ")

        # Update rectangle information to user's data
        rect.length = length
        rect.width = width
        rect.colour = colour

        # Save rectangle in the list
        rectangles.append(rect)

    max_rect = find_greatest_area(rectangles)
    if max_rect is not None:
        max_rect.display()

    min_width = find_smallest_width(rectangles)
    if min_width is not None:
        min_width.display()