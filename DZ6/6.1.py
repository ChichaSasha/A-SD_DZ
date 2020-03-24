M = 9999991
N = 1


class Node:
    def init(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.valid = True


def hash_func(n):
    return n % M


def init():
    global values
    values = [None for i in range(M)]

    with open("input.txt") as file:
        for line in file:
            pair = line.strip().split('=')
            key, value = int(pair[0]), pair[1]
            set(key, value)


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global values
    hash_key = hash_func(key)
    slot = values[hash_key]
    while slot != None:
        if slot.key == key:
            slot.value = value
            slot.valid = True
            return
        slot = slot.next
    slot = Node(key, value)
    slot.next = values[hash_key]
    values[hash_key] = slot


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    global values
    hash_key = hash_func(key)
    slot = values[hash_key]
    while slot != None:
        if slot.key == key:
            return slot.value
        slot = slot.next
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    global values
    hash_key = hash_func(key)
    slot = values[hash_key]
    if slot == None:
        return
    while slot != None:
        if slot.key == key:
            if slot.next:
                slot.key = slot.next.key
            else:
                slot.key = None
            return
