class Pizza:
    _sizes = ["small", "medium", "large", "extra-large"]

    toppings = []

    def __init__(self, size, toppings):
        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size = "medium"

        for topping in self.toppings:
            Pizza.toppings.append(topping)

    def set_size(self, new_size):

        if new_size.lower() in Pizza._sizes:
            self._size = new_size
            return True
        else:
            return False

    def display(self):
        print(f"Pizza size: {self._size}")
        print(f"Pizza toppings: {self.toppings}")

    def get_size(self):
        return self._size

    def get_num_toppings(self):
        count = 0
        for i in self.toppings:
            count += 1
        return count

    def add_topping(self, topping):
        self.toppings.append(topping)
        return True

    def remove_topping(self, topping):
        if topping.lower() in self.toppings:
            self.toppings.remove(topping)
            return True
        else:
            return False