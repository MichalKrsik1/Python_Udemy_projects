class FloristShop:
    def __init__(self):
        self.inventory = []
        self.orders = []
        self.budget = 100

    def add_flower(self, name, cost):
        self.inventory.append(Flower(name, cost))

    def sell_bouquet(self, size):
        flowers = []
        while size > 0:
            single_flower = self.inventory.pop()
            self.budget += single_flower.cost
            flowers.append(single_flower)
            size -= 1

        self.orders.append(Bouquet(self.get_next_uid(), flowers))

    def display_inventory(self):
        for item in self.inventory:
            print(item.name)

    def display_orders(self):
        if len(self.orders) == 0:
            print("No orders exist")
        else:
            for order in self.orders:
                print(order)

    def display_budget(self):
        print(f"Budget: {self.budget}")

    def get_next_uid(self):
        if len(self.orders) > 0:
            return self.orders[-1].uid + 1
        else:
            return 0


class Bouquet:
    def __init__(self, uid, flowers=[]):
        self.uid = uid
        self.flowers = flowers

    def __str__(self):
        formatted_order = ", ".join([flower.name for flower in self.flowers])
        return f"Order {self.uid}: {formatted_order}"


class Flower:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
