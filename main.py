from operator import itemgetter


class Computer:
    """Компьютер"""

    def __init__(self, id, name, cpu_cores, display_class_room_id):
        self.id = id
        self.computer_name = name
        self.cpu_cores = cpu_cores
        self.display_class_room_id = display_class_room_id


class Display_class_room:
    """Дисплейный класс"""

    def __init__(self, class_room_id, class_room_number):
        self.class_room_id = class_room_id
        self.class_room_number = class_room_number


# Дисплейные классы
display_class_rooms = [
    Display_class_room(1, 'Компьютерный класс 1'),
    Display_class_room(2, 'Компьютерный класс 2'),
    Display_class_room(3, 'Компьютерный класс 3'),
]

# Компьютеры
computers = [
    Computer(1, 'Acer', 4, 1),
    Computer(2, 'Asus', 6, 2),
    Computer(3, 'Lenovo', 8, 3),
    Computer(4, 'HP', 4, 3),
    Computer(5, 'Dell', 4, 3),
]


def main():
    """Основная функция"""

    one_to_many = [(c.computer_name, c.cpu_cores, d.class_room_number)
                   for d in display_class_rooms
                   for c in computers
                   if c.display_class_room_id == d.class_room_id]

    print('Задание 1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание 2')
    res_12_unsorted = []
    for d in display_class_rooms:
        d_computers = list(filter(lambda i: i[2] == d.class_room_number, one_to_many))
        if len(d_computers) > 0:
            d_cpu_cores = [cpu_cores for _, cpu_cores, _ in d_computers]
            d_cpu_cores_sum = sum(d_cpu_cores)
            res_12_unsorted.append((d.class_room_number
                                    , d_cpu_cores_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


if __name__ == '__main__':
    main()
