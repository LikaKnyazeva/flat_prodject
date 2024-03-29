from flat import Flat
from restroom import Restroom
from room import Room


# Инфо о квартире (номер квартиры, номер дома, название улицы, город, колличество комнат, метраж, имя владельца,
# этаж, основной материал)
flat = Flat(number_flat=33, number_house=12, street="Street", city="Kyiv", footage=60.4, owner="Vasya", floor=2,
            material="glass", rooms=(
                                    Room("Kitchen", True, 41.0),
                                    Room("Sleeping room", True, 13.3),
                                    Room("Children room", True, 4.1)
                                    )
            )

# Инфо о санузле (метраж, можно проверить смежный или нет по методу view_adjacency() и проверить количество санузлов
# по методу view_count())
restroom = Restroom(1.0)
restroom1 = Restroom(5.0)
restroom2 = Restroom(7.0)


# Сгенерировать номер учетной записи
def number_of_account():
    print(str(flat.number_flat) + str(flat.number_house) + str(flat.owner[0]) + str(flat.city[2]) + str(flat.floor))


# Функция майн
def main():
    number_of_account()
    Restroom.view_adjacency(restroom1)
    print(flat.room_number)
    flat.area_room()


if __name__ == "__main__":
    main()
