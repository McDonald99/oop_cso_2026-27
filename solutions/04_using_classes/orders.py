
class Pizza:
    _sizes = ["small", "medium", "large", "extra-large"]

    def __init__(self, toppings, size="medium"):
        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size = "medium"

        self.toppings = toppings

    @classmethod
    def validate_size(cls, size):
        if size.lower() in cls._sizes:
            return True

        return False

    @classmethod
    def add_valid_size(cls, new_size):
        if new_size.lower() not in cls._sizes:
            cls._sizes.append(new_size.lower())
            return True

        return False

    def set_size(self, new_size):
        if new_size.lower() in Pizza._sizes:
            self._size = new_size
            return True
        else:
            return False

    def display(self):
        if len(self.toppings) == 1:
            toppings = self.toppings[0]
        elif len(self.toppings) > 1:
            toppings = ", ".join(self.toppings[0:-1])
            toppings += f" and {self.toppings[-1]}"
        else:
            toppings = "no toppings."

        print(f"{self._size} pizza with {toppings}")


if __name__ == "__main__":
    pizza1 = Pizza(["cheese", "pineapple"], "medium")
    pizza1.display()

    pizza2 = Pizza(["hame, cheese", "pineapple"], "medium")
    pizza2.display()

    pizza3 = Pizza(["cheese"], "medium")
    pizza3.display()

    pizza4 = Pizza([], "medium")
    pizza4.display()

    new_size = "personal"
    if pizza1.validate_size(new_size):
        print(f"{new_size} is a valid size")
    else:
        print(f"{new_size} is invalid")

    if Pizza.validate_size(new_size):
        print(f"{new_size} is a valid size")
    else:
        print(f"{new_size} is invalid")