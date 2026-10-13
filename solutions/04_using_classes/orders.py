class Pizza:
    _sizes = ["small", "medium", "large", "extra-large"]

    def __init__(self, toppings, size="medium"):
        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size = "medium"


        self.toppings = toppings

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

    def get_size(self):
        return self._size

    def get_num_toppings(self):
        count = len(self.toppings)
        return count

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return True

    def remove_topping(self, topping):
        if topping.lower() in self.toppings:
            self.toppings.remove(topping)
            return True
        else:
            return False


if __name__ == "__main__":
    pizza1 = Pizza(["cheese", "pineapple"], "small")
    pizza1.display()

    pizza2 = Pizza(["ham, cheese", "pineapple"], "large")
    pizza2.display()

    pizza3 = Pizza(["cheese"])
    pizza3.display()

    pizza4 = Pizza([], "medium")
    pizza4.display()