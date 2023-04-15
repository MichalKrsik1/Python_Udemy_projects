class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def create_room(self, room):
        self.rooms.append(room)

    def print_open_rooms(self):
        for room in self.rooms:
            if any(day.status == "Open" for day in room.time):
                print(f"Room {room.number} is open.")
            for day in room.time:
                if day.status == "Open":
                    print(day.start)
        print("________________________________")


class Room:
    def __init__(self, number):
        self.number = number
        self.price = 100
        self.time = []

    def add_block(self, block):
        self.time.append(block)

    def reserve_room(self, num):
        self.time[num - 1].status = "Closed"

    def cancel_reservation(self, num):
        self.time[num - 1].status = "Open"


class Penthouse(Room):
    def __init__(self, number):
        super().__init__(number)
        self.price = 1000


class Day:
    def __init__(self, num_start, start, status):
        self.start = start
        self.status = status
        self.num_start = num_start

