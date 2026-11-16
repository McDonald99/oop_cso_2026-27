from datetime import date
from types import NotImplementedType


class Animal:
    def __init__(self, dob: date, weight: float | int, name: str = "Fido"):
        if not dob:
            print("Animal cannot have no date of birth")
            print("Defaulting to today")
            dob = date.today()

        if not isinstance(dob, date):
            print("Date of birth must be a datetime.date type")
            print("Defaulting to today")
            dob = date.today()

        if not isinstance(weight, int | float):
            print("Animal weight must be numeric")
            print("Defaulting to 5")
            weight = 5

        if weight <= 0:
            print("Animal cannot have no weight.")
            print("Defaulting to 5")
            weight = 5

        if not name:
            print("Animal cannot have no name")
            print("Defaulting to \"Fido\"")
            name = "Fido"

        self.dob = dob
        self.weight = weight
        self.name = name

    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.name} is {self.calc_age()} years old and weighs {self.weight}kg."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{name={self.name}, weight:{self.weight}, dob={self.dob}}}"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Animal):
            return NotImplemented

        if self.dob != other.dob:
            return False

        if self.weight != other.weight:
            return False

        if self.name.lower() != other.name.lower():
            return False

        return True


    def calc_age(self):
        today = date.today()
        difference = today - self.dob
        return int(difference.days / 365)


class Dog(Animal):
    def __init__(self, dob: date, weight: float | int, breed:str, name: str = "Fido", personality: str = "Happy"  ):
        super().__init__(dob, weight, name)

        if not breed:
            print("Dog cannot have a breed")
            print("Defaulting to \"Labrador\"")
            breed = "Labrador"

        self.breed = breed
        self.personality = personality




if __name__ == "__main__":
    animal = Animal(date(2025, 10, 1), 0)
    print(animal.calc_age())

    dog = Dog(date(2021, 10, 13), 4, "poodle", "Celia", "Bubbly!")
    dog.display()