class Address:
    house_no = 0
    add_1 = ""
    add_2 = None
    add_3 = None
    city = ""
    state = ""
    postcode = ""
    country = ""

    def __init__(self, house_no, add_1, city, state, postcode, country, add_2=None, add_3=None):
        self.house_no = house_no
        self.add_1 = add_1
        self.add_2 = add_2
        self.add_3 = add_3
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def display(self):
        print(f"House No.: {self.house_no}")
        print(f"Address Line 1: {self.add_1}")
        if self.add_2 is not None:
            print(f"Address Line 2: {self.add_2}")
        if self.add_3 is not None:
            print(f"Address Line 3: {self.add_3}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Postcode: {self.postcode}")
        print(f"Country: {self.country}")


if __name__ == "__main__":
    