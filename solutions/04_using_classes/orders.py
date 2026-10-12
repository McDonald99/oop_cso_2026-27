class Pizza:
    _sizes = ["small", "medium", "large", "extra-large"]

    def __init__(self, size, toppings):
        if size.lower() in Pizza._sizes:
            self._size = size
        else:
            self._size = "medium"


    def set_size(self, new_size):

        if new_size.lower() in Pizza._sizes:
            self._size = new_size
            return True
        else:
            return False