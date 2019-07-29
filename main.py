from flat import Flat
from restroom import Restroom
from room import Room

# Инфо о каждой комнате(название, наличие балкона, метраж)
rooms = (
    Room("Kitchen", True, 41.0),
    Room("Sleeping room", True, 13.3),
    Room("Children room", True, 4.1)
)

# Инфо о квартире (номер квартиры, номер дома, название улицы, город, колличество комнат, метраж, имя владельца,
# этаж, основной материал)
flat = Flat(number_flat=33, number_house=12, street="Street", city="Kyiv", footage=60.4, owner="Vasya", floor=2, material="glass", rooms=(
    Room("Kitchen", True, 41.0),
    Room("Sleeping room", True, 13.3),
    Room("Children room", True, 4.1)
))

# Инфо о санузле (метраж, можно проверить смежный или нет по методу view_adjacency() и проверить количество санузлов
# по методу view_count())
restroom = Restroom(1.0)
restroom1 = Restroom(5.0)
restroom2 = Restroom(7.0)


# Метод площади комнаты
def area_room():
    area2 = room.footage + room1.footage + room2.footage
    print("Общая площадь комнат: ")
    print(area2)
    return area2


# Общая площадь санузла
def area_restroom() -> float:
    area1 = restroom.footage + restroom1.footage + restroom2.footage
    print("Общая площать санузла в квартире:")
    print(area1)
    return area1


# Колличество комнат
def count_of_restroom():
    restroom.view_count()
    restroom1.view_count()
    restroom2.view_count()
    print(restroom.count_room + restroom1.count_room + restroom2.count_room)


# Общая площадь квартиры
def common_footage():
    area3 = area_room()
    area4 = area_restroom()
    area5 = area3 + area4
    print("Общая площать квартиры:")
    print(area5)
    return area5


# Сгенерировать номер учетной записи
def number_of_account():
    print(str(flat.number_flat) + str(flat.number_house) + str(flat.owner[0]) + str(flat.city[2]) + str(flat.floor))


# Функция майн
def main():
    number_of_account()
    common_footage()
    Restroom.view_adjacency(restroom1)
    count_of_restroom()
    # count_of_room()
    print(flat.room_number)
    flat.area_room()


if __name__ == "__main__":
    main()
