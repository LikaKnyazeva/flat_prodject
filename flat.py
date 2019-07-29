import uuid


class Flat(object):
    def __init__(self, number_flat: int, number_house: int, street: str, city: str, rooms: tuple, footage: float,
                 owner: str, floor: int, material: str):
        self.number_flat = number_flat
        self.number_house = number_house
        self.street = street
        self.city = city
        self.rooms = rooms
        self.footage = footage
        self.owner = owner
        self.floor = floor
        self.material = material
        self.id = uuid.uuid4()
        for room in self.rooms:
            room.set_flat_id(self.id)

    def plan_flat(self):
        pass

    @property
    def room_number(self) -> int:
        return len(self.rooms)

    def area_room(self):
        """ Метод площади комнаты """
        return sum([room.footage for room in self.rooms])

