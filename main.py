class Ammunition:
    def __init__(self, name: str, weight: float, price: float):
        if weight <= 0 or price <= 0:
            raise ValueError("вага/ціна мають бути > 0")
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, вага:{self.weight}, ціна:{self.price})"


class Armor(Ammunition):
    def __init__(self, name: str, weight: float, price: float, defense: int):
        super().__init__(name, weight, price)
        self.defense = defense


class Weapon(Ammunition):
    def __init__(self, name: str, weight: float, price: float, damage: int):
        super().__init__(name, weight, price)
        self.damage = damage


class Node:
    def __init__(self, data: Ammunition):
        self.data = data
        self.next = None
        self.prev = None


class AmmunitionAestheticList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self._size = 0

        # пер типу_констр
        if data is not None:
            if isinstance(data, Ammunition):
                self.append(data)
            elif hasattr(data, '__iter__') and not isinstance(data, (str, bytes)):
                for item in data:
                    self.append(item)
            else:
                raise TypeError("невірний тип констр")

    def append(self, item: Ammunition):
        if not isinstance(item, Ammunition):
            raise TypeError("треба об амун")

        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def remove(self, item: Ammunition) -> bool:
        # лог вид вузла
        curr = self.head
        while curr:
            if curr.data == item:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                self._size -= 1
                return True
            curr = curr.next
        raise ValueError("елемент відсутній")

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Ammunition:
        if index < 0 or index >= self._size:
            raise IndexError("індекс за меж")

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


if __name__ == "__main__":
    try:
        # Тут виправлено: додали шкоду 45 для меча та 30 для лука
        sword = Weapon("Меч", 3.5, 400, 45)
        armor = Armor("Щит", 7.0, 250, 30)

        # констр 1 порож
        list_empty = AmmunitionAestheticList()
        print(f"довжина: {len(list_empty)}")

        # ... констр 2 один
        list_single = AmmunitionAestheticList(sword)
        for x in list_single:
            print(x)

        # констр 3 кол
        standart_list = [sword, armor, Weapon("Лук", 1.8, 150, 30)]
        list_coll = AmmunitionAestheticList(standart_list)

        # елем кол
        for item in list_coll:
            print(item)

        print(f"\nелемент за індексом 1: {list_coll[1]}")

        list_coll.remove(armor)
        # після вид елем
        for item in list_coll:
            print(item)

        print(f"нова довжина: {len(list_coll)}")

    except (ValueError, TypeError, IndexError) as e:
        print(f"помилка виконання: {e}")