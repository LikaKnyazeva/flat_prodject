class Restroom(object):


    def __init__(self, footage_room: float):
        self.count_room = 0
        self.adjacency = False
        self.footage = footage_room

    def view_count(self):
        if self.footage > 0.0:
            self.count_room = 1

    def view_adjacency(self):
        if self.footage >= 6.0:
            self.adjacency = True
        print(self.adjacency)

