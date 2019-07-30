""" Room class"""


class Room(object):
    def __init__(self, name: str, balcony: bool, footage: float):
        self.name = name
        self.balcony = balcony
        self.footage = footage
        self.count_room = 0
        self.id = None

    def view_count(self):
        if 0.0 < self.footage:
            self.count_room = 1

    def set_flat_id(self, idx):
        self.id = idx

    def plan_room(self):
        pass
