from enum import Enum
from datetime import datetime

class ItemType(Enum):
    CONSTRUCTION = 1
    PAINTING = 2
    PLUMBING = 3
    INTERIOR = 4
    MESTHRI = 5


class Item:
    def __init__(self, dt, item_type, description, amount):
        self.dt = dt
        self.item_type = item_type
        self.description = description
        self.amount = amount

class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, dt, item_type, description, amount):
        self.items.append(Item(dt=dt, item_type=item_type, description=description, amount=amount))


def items(item_list):
    item_list.add_item(dt=datetime(2021, 7, 10),item_type=ItemType.CONSTRUCTION,
                       description='Manal', amount=10000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION,
                       description='1-Ft-Pipe,Vadagai,coolie', amount=9000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION,
                       description='coolie', amount=6000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION,
                       description='JCB', amount=9000, page_num=1)

    item_list.add_item(dt=datetime(2021, 7, 14), item_type=ItemType.CONSTRUCTION,
                       description='Jalli-Manal', amount=10000, page_num=2)

    item_list.add_item(dt=datetime(2021, 7, 15), item_type=ItemType.CONSTRUCTION,
                       description='Pipe, Motor-installation', amount=6000, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION,
                       description='Kambi-16M-40-No', amount=57960, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION,
                       description='Kambi-12M-40-No', amount=32560, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION,
                       description='Kambi-10M-10-No', amount=5680, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION,
                       description='B-wice(kattukambi?) 10', amount=900, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION,
                       description='10 Bag cement', amount=4500, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.MESTHRI,
                       description='Kothanar advance', amount=10000, page_num=3)

    item_list.add_item(dt=datetime(2021, 7, 17), item_type=ItemType.CONSTRUCTION,
                       description='50 bags cement', amount=22500, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 17), item_type=ItemType.CONSTRUCTION,
                       description='Manal, Jalli, Total23K, Balance 8K', amount=15000, page_num=3)

    item_list.add_item(dt=datetime(2021, 7, 18), item_type=ItemType.CONSTRUCTION,
                       description='Basement column', amount=15000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 19), item_type=ItemType.MESTHRI,
                       description='Column coolie', amount=25000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 19), item_type=ItemType.CONSTRUCTION,
                       description='Manal Jalli Balance', amount=8000, page_num=3)

    item_list.add_item(dt=datetime(2021, 7, 20), item_type=ItemType.CONSTRUCTION,
                       description='MachineRent', amount=2500, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 21), item_type=ItemType.CONSTRUCTION,
                       description='Cement Balance', amount=3500, page_num=3)

    item_list.add_item(dt=datetime(2021, 7, 22), item_type=ItemType.CONSTRUCTION,
                       description='Brick', amount=80000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 24), item_type=ItemType.CONSTRUCTION,
                       description='Kambi-Timber', amount=30000, page_num=4)

    item_list.add_item(dt=datetime(2021, 7, 26), item_type=ItemType.MESTHRI,
                       description='Mesthri', amount=75000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 26), item_type=ItemType.CONSTRUCTION,
                       description='Shed', amount=12000, page_num=4)

    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION,
                       description='100 Bag cement(100*450=45000 for cement, Kambi:15000', amount=60000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION,
                       description='Manal-Jalli', amount=20000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.MESTHRI,
                       description='Mesthri', amount=20000, page_num=4)

    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION,
                       description='70 feet etension bore, 10 feet pipe 460', amount=7000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 29), item_type=ItemType.CONSTRUCTION,
                       description='Mixing machine rent: 5k, Shed build: 1.5K, ShedDoor: 1.9K', amount=5000, page_num=5)

    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.CONSTRUCTION,
                       description='Brick balance', amount=2000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.CONSTRUCTION,
                       description='Manal-Jalli balance', amount=2500, page_num=5)

    item_list.add_item(dt=datetime(2021, 8, 2), item_type=ItemType.CONSTRUCTION,
                       description='Kambi', amount=27000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.MESTHRI,
                       description='Kothanar', amount=32000, page_num=5)
    item_list.add_item(dt=datetime(2021, 8, 4), item_type=ItemType.CONSTRUCTION,
                       description='Kambi', amount=32000, page_num=2822)




if __name__ == '__main__':
    print("House expenses copied from Aruna's note")