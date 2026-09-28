class Enemy:
    type = "electric"
    health = 5
    x_pos = 10
    y_pos = 10

    def display(self):
        print(f"type: {self.type}")
        print(f"health: {self.health}")
        print(f"x_pos: {self.x_pos}")
        print(f"y_pos: {self.y_pos}")


if __name__ == "__main__":
    first_enemy = Enemy()

    print(f"enemy type: {first_enemy.type}")
    first_enemy.type = "fire"
    print(f"enemy type: {first_enemy.type}")

    first_enemy.display()

    second_enemy = Enemy()
    second_enemy.display()