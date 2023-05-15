from enum import Enum
from datetime import datetime

class ItemType(Enum):
    CONSTRUCTION = 1
    PAINTING = 2
    ELECTRICIAN_PLUMBING = 3
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
                       description='Kambi', amount=2822, page_num=5)

    item_list.add_item(dt=datetime(2021, 8, 5), item_type=ItemType.CONSTRUCTION,
                       description='ConcreteBelt', amount=23300, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 5), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=6000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 6), item_type=ItemType.CONSTRUCTION,
                       description='Aadhi?', amount=13500, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 16), item_type=ItemType.CONSTRUCTION,
                       description='Gravel', amount=57100, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 19), item_type=ItemType.CONSTRUCTION,
                       description='Gravel', amount=85000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 22), item_type=ItemType.CONSTRUCTION,
                       description='Gravel', amount=40000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 23), item_type=ItemType.CONSTRUCTION,
                       description='JCB rent, Gravel filling', amount=27000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 27), item_type=ItemType.CONSTRUCTION,
                       description='Lawyer registration fee', amount=3000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 30), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=8000, page_num=7)

    item_list.add_item(dt=datetime(2021, 8, 31), item_type=ItemType.CONSTRUCTION,
                       description='2 loads of gravel', amount=28000, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 2), item_type=ItemType.CONSTRUCTION,
                       description='EC registration', amount=1000, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 6), item_type=ItemType.CONSTRUCTION,
                       description='Brick', amount=82800, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 12), item_type=ItemType.CONSTRUCTION,
                       description='5 cement bag', amount=2500, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 13), item_type=ItemType.CONSTRUCTION,
                       description='Manal', amount=13000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 13), item_type=ItemType.MESTHRI,
                       description='Kothanar', amount=27000, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.CONSTRUCTION,
                       description='Kambi', amount=42160, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=8000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.CONSTRUCTION,
                       description='Septic tank', amount=2000, page_num=8)

    item_list.add_item(dt=datetime(2021, 9, 21), item_type=ItemType.CONSTRUCTION,
                       description='Jelli potathu', amount=6000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 21), item_type=ItemType.CONSTRUCTION,
                       description='Septic tank', amount=6000, page_num=8)

    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION,
                       description='Sengal: 10000*9.6', amount=96000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION,
                       description='M-sand', amount=12000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION,
                       description='P-sand', amount=6500, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.MESTHRI,
                       description='Kothanar, kambi construct', amount=23000, page_num=8)

    item_list.add_item(dt=datetime(2021, 9, 29), item_type=ItemType.CONSTRUCTION,
                       description='Water supply', amount=1000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 29), item_type=ItemType.CONSTRUCTION,
                       description='Gunny sack-6 pieces', amount=320, page_num=8)

    item_list.add_item(dt=datetime(2021, 9, 30), item_type=ItemType.CONSTRUCTION,
                       description='Water pipe', amount=1800, page_num=9)

    item_list.add_item(dt=datetime(2021, 10, 4), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=26000, page_num=9)

    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION,
                       description='M-sand', amount=13000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION,
                       description='Cement: 15-bag', amount=7300, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.MESTHRI,
                       description='Mesthri', amount=40000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION,
                       description='centring', amount=3000, page_num=9)

    item_list.add_item(dt=datetime(2021, 10, 18), item_type=ItemType.CONSTRUCTION,
                       description='20 cement', amount=9700, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 12), item_type=ItemType.CONSTRUCTION,
                       description='30 cement', amount=13950, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 12), item_type=ItemType.CONSTRUCTION,
                       description='Kambi', amount=82529, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 18), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=20000, page_num=9)

    item_list.add_item(dt=datetime(2021, 10, 25), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=4000, page_num=10)
    item_list.add_item(dt=datetime(2021, 10, 27), item_type=ItemType.CONSTRUCTION,
                       description='Steps sheet', amount=11000, page_num=10)
    item_list.add_item(dt=datetime(2021, 10, 27), item_type=ItemType.CONSTRUCTION,
                       description='Kambi', amount=166710, page_num=10)

    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=80000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.ELECTRICIAN_PLUMBING,
                       description='Electrician', amount=1000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='Jally & Manal', amount=41000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='Poojai & Seval', amount=1500, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='Concrete Mixer', amount=6000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='Mamiyar power of attorney', amount=3000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='MOD registration', amount=57500, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION,
                       description='Cement bag', amount=46500, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.ELECTRICIAN_PLUMBING,
                       description='Balance for shop', amount=19719, page_num=11)

    item_list.add_item(dt=datetime(2021, 11, 18), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=9000, page_num=11)

    item_list.add_item(dt=datetime(2021, 11, 24), item_type=ItemType.CONSTRUCTION,
                       description='Saravanan LIC', amount=10000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 20), item_type=ItemType.CONSTRUCTION,
                       description='Manal', amount=12000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 20), item_type=ItemType.MESTHRI,
                       description='Mesthri', amount=26000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 23), item_type=ItemType.MESTHRI,
                       description='Brick(5000)', amount=55000, page_num=11)

    item_list.add_item(dt=datetime(2021, 12, 1), item_type=ItemType.CONSTRUCTION,
                       description='Kadai balance', amount=20000, page_num=11)

    item_list.add_item(dt=datetime(2021, 12, 8), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=3500, page_num=11)
    item_list.add_item(dt=datetime(2021, 12, 10), item_type=ItemType.MESTHRI,
                       description='MESTHRI', amount=2000, page_num=11)






if __name__ == '__main__':
    print("House expenses copied from Aruna's note")