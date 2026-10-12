def basket_total(basket):
    total = 0
    for item in basket:
        sub_total = item["price"] * item["quantity"]
        total += sub_total

    return total

def print_receipt(basket):
    total = 0
    for item in basket:
        sub_total = item["price"] * item["quantity"]
        total += sub_total
        print(f"{item["name"]} {item["quantity"]} x €{item["price"]} €{sub_total}")

    print(f"Total €{total}")

if __name__ == "__main__":
    basket = [
        {"name": "Yogurt", "price": 1.79, "quantity": 4},
        {"name": "Bread", "price": 1.80, "quantity": 1},
        {"name": "Milk", "price": 1.59, "quantity": 2},
    ]

    print(basket_total(basket))

    print(print_receipt(basket))