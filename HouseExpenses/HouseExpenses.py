from enum import Enum
from datetime import datetime
from collections import defaultdict
import click

class ItemType(Enum):
    CONSTRUCTION = 1
    PAINTER = 2
    ELECTRICIAN_PLUMBING = 3
    INTERIOR = 4
    MESTHRI = 5
    TILES=6
    CARPENTER=7
    GOVT = 8,
    GLASS_WORK = 9,
    FURNITURES = 10



class Item:
    def __init__(self, dt, item_type, description, amount, page_num, notes):
        self.dt = dt
        self.item_type = item_type
        self.description = description
        self.amount = amount
        self.page_num = page_num
        self.notes = notes

    def __str__(self):
        return f'{self.dt}, {self.description}, {self.amount}, {self.page_num}'

class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, dt, item_type, description, amount, page_num, notes=''):
        self.items.append(Item(dt=dt, item_type=item_type, description=description,
                               amount=amount, page_num=page_num, notes=notes))


    def page_wise_sum(self):
        d = defaultdict(list)
        total_page_wise_sum = 0
        for item in self.items:
            d[item.page_num].append(item)
        for k, v in d.items():
            sum_value = sum(i.amount for i in v)
            total_page_wise_sum += sum_value
            print(f'{k}: {sum_value}')
        print(f'Total page_wise_sum: {total_page_wise_sum}')

    def total(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.amount
        print(f'Total sum: {total_sum}')

    def item_wise_sum(self):
        d = defaultdict(list)
        for item in self.items:
            d[item.item_type].append(item.amount)
        for k, v in d.items():
            print(f'{k}: {sum(v)}')

    def item_wise_detail_impl(self, item_type):
        sum_value = 0
        for item in self.items:
            if item.item_type == item_type:
                sum_value += item.amount
                print(item)
        print(f'Total: {sum_value}')

    def item_wise_detail_painter(self):
        self.item_wise_detail_impl(ItemType.PAINTER)

    def item_wise_detail_electrician(self):
        self.item_wise_detail_impl(ItemType.ELECTRICIAN_PLUMBING)

    def item_wise_detail_interior(self):
        self.item_wise_detail_impl(ItemType.INTERIOR)

    def item_wise_detail_tiles(self):
        self.item_wise_detail_impl(ItemType.TILES)

    def item_wise_detail_carpenter(self):
        self.item_wise_detail_impl(ItemType.CARPENTER)

    def item_wise_detail_glasswork(self):
        self.item_wise_detail_impl(ItemType.GLASS_WORK)

def populate_items(item_list):
    item_list.add_item(dt=datetime(2021, 7, 10),item_type=ItemType.CONSTRUCTION, description='Manal', amount=10000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION, description='1-Ft-Pipe,Vadagai,coolie', amount=9000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION, description='coolie', amount=6000, page_num=1)
    item_list.add_item(dt=datetime(2021, 7, 12), item_type=ItemType.CONSTRUCTION, description='JCB', amount=9000, page_num=1)

    item_list.add_item(dt=datetime(2021, 7, 14), item_type=ItemType.CONSTRUCTION, description='Jalli-Manal', amount=10000, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 15), item_type=ItemType.CONSTRUCTION, description='Pipe, Motor-installation', amount=6000, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION, description='Kambi-16M-40-No', amount=57960, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION, description='Kambi-12M-40-No', amount=32560, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION, description='Kambi-10M-10-No', amount=5680, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION, description='B-wice(kattukambi?) 10', amount=900, page_num=2)
    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.CONSTRUCTION, description='10 Bag cement', amount=4500, page_num=2)

    item_list.add_item(dt=datetime(2021, 7, 16), item_type=ItemType.MESTHRI, description='Kothanar advance', amount=10000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 17), item_type=ItemType.CONSTRUCTION, description='50 bags cement', amount=22500, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 17), item_type=ItemType.CONSTRUCTION, description='Manal, Jalli, Total23K, Balance 8K', amount=15000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 18), item_type=ItemType.CONSTRUCTION, description='Basement column', amount=15000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 19), item_type=ItemType.MESTHRI, description='Column coolie', amount=25000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 19), item_type=ItemType.CONSTRUCTION, description='Manal Jalli Balance', amount=8000, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 20), item_type=ItemType.CONSTRUCTION, description='MachineRent', amount=2500, page_num=3)
    item_list.add_item(dt=datetime(2021, 7, 21), item_type=ItemType.CONSTRUCTION, description='Cement Balance', amount=3500, page_num=3)

    item_list.add_item(dt=datetime(2021, 7, 22), item_type=ItemType.CONSTRUCTION, description='Brick', amount=80000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 24), item_type=ItemType.CONSTRUCTION, description='Kambi-Timber', amount=30000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 26), item_type=ItemType.MESTHRI, description='Mesthri', amount=75000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 26), item_type=ItemType.CONSTRUCTION, description='Shed', amount=12000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION, description='100 Bag cement(100*450=45000 for cement, Kambi:15000', amount=60000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION, description='Manal-Jalli', amount=20000, page_num=4)
    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.MESTHRI, description='Mesthri', amount=20000, page_num=4)

    item_list.add_item(dt=datetime(2021, 7, 27), item_type=ItemType.CONSTRUCTION, description='70 feet etension bore, 10 feet pipe 460', amount=7000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 29), item_type=ItemType.CONSTRUCTION, description='Mixing machine rent: 5k, Shed build: 1.5K, ShedDoor: 1.9K', amount=5000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.CONSTRUCTION, description='Brick balance', amount=2000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.CONSTRUCTION, description='Manal-Jalli balance', amount=2500, page_num=5)
    item_list.add_item(dt=datetime(2021, 8, 2), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=27000, page_num=5)
    item_list.add_item(dt=datetime(2021, 7, 31), item_type=ItemType.MESTHRI, description='Kothanar', amount=32000, page_num=5)
    item_list.add_item(dt=datetime(2021, 8, 4), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=2822, page_num=5)

    item_list.add_item(dt=datetime(2021, 8, 5), item_type=ItemType.CONSTRUCTION, description='ConcreteBelt', amount=23300, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 5), item_type=ItemType.MESTHRI, description='MESTHRI', amount=6000, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 6), item_type=ItemType.CONSTRUCTION, description='Aadhi?', amount=13500, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 16), item_type=ItemType.CONSTRUCTION, description='Gravel', amount=57100, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 19), item_type=ItemType.CONSTRUCTION, description='Gravel', amount=85000, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 22), item_type=ItemType.CONSTRUCTION, description='Gravel', amount=40000, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 23), item_type=ItemType.CONSTRUCTION, description='JCB rent, Gravel filling', amount=27000, page_num=6)
    item_list.add_item(dt=datetime(2021, 8, 27), item_type=ItemType.CONSTRUCTION, description='Lawyer registration fee', amount=3000, page_num=6)

    item_list.add_item(dt=datetime(2021, 8, 30), item_type=ItemType.MESTHRI, description='MESTHRI', amount=8000, page_num=7)
    item_list.add_item(dt=datetime(2021, 8, 31), item_type=ItemType.CONSTRUCTION, description='2 loads of gravel', amount=28000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 2), item_type=ItemType.CONSTRUCTION, description='EC registration', amount=1000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 6), item_type=ItemType.CONSTRUCTION, description='Brick', amount=82800, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 12), item_type=ItemType.CONSTRUCTION, description='5 cement bag', amount=2500, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 13), item_type=ItemType.CONSTRUCTION, description='Manal', amount=13000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 13), item_type=ItemType.MESTHRI, description='Kothanar', amount=27000, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=42160, page_num=7)
    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.MESTHRI, description='MESTHRI', amount=8000, page_num=7)

    item_list.add_item(dt=datetime(2021, 9, 20), item_type=ItemType.CONSTRUCTION, description='Septic tank', amount=2000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 21), item_type=ItemType.CONSTRUCTION, description='Jelli potathu', amount=6000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 21), item_type=ItemType.CONSTRUCTION, description='Septic tank', amount=6500, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION, description='Sengal: 10000*9.6', amount=96000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION, description='M-sand', amount=12000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.CONSTRUCTION, description='P-sand', amount=6500, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 27), item_type=ItemType.MESTHRI, description='Kothanar, kambi construct', amount=23000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 29), item_type=ItemType.CONSTRUCTION, description='Water supply', amount=1000, page_num=8)
    item_list.add_item(dt=datetime(2021, 9, 29), item_type=ItemType.CONSTRUCTION, description='Gunny sack-6 pieces', amount=320, page_num=8)

    item_list.add_item(dt=datetime(2021, 9, 30), item_type=ItemType.CONSTRUCTION, description='Water pipe', amount=1800, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 4), item_type=ItemType.MESTHRI, description='MESTHRI', amount=26000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION, description='M-sand', amount=13000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION, description='Cement: 15-bag', amount=7300, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.MESTHRI, description='Mesthri', amount=40000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 10), item_type=ItemType.CONSTRUCTION, description='centring', amount=3000, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 18), item_type=ItemType.CONSTRUCTION, description='20 cement', amount=9700, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 12), item_type=ItemType.CONSTRUCTION, description='30 cement', amount=13950, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 12), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=82529, page_num=9)
    item_list.add_item(dt=datetime(2021, 10, 18), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=9)

    item_list.add_item(dt=datetime(2021, 10, 25), item_type=ItemType.MESTHRI, description='MESTHRI', amount=4000, page_num=10)
    item_list.add_item(dt=datetime(2021, 10, 27), item_type=ItemType.CONSTRUCTION, description='Steps sheet', amount=11000, page_num=10)
    item_list.add_item(dt=datetime(2021, 10, 27), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=166710, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.MESTHRI, description='MESTHRI', amount=80000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=1000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='Jally & Manal', amount=41000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='Poojai & Seval', amount=1500, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='Concrete Mixer', amount=6000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='Mamiyar power of attorney', amount=3000, page_num=10)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='MOD registration', amount=57500, page_num=10)

    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.CONSTRUCTION, description='Cement bag', amount=46500, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 1), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Balance for shop', amount=19719, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 18), item_type=ItemType.MESTHRI, description='MESTHRI', amount=9000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 24), item_type=ItemType.CONSTRUCTION, description='Saravanan LIC', amount=10000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 20), item_type=ItemType.CONSTRUCTION, description='Manal', amount=12000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 20), item_type=ItemType.MESTHRI, description='Mesthri', amount=26000, page_num=11)
    item_list.add_item(dt=datetime(2021, 11, 23), item_type=ItemType.CONSTRUCTION, description='Brick(5000)', amount=55000, page_num=11)
    item_list.add_item(dt=datetime(2021, 12, 1), item_type=ItemType.CONSTRUCTION, description='Kadai balance', amount=20000, page_num=11)
    item_list.add_item(dt=datetime(2021, 12, 8), item_type=ItemType.MESTHRI, description='MESTHRI', amount=3500, page_num=11)
    item_list.add_item(dt=datetime(2021, 12, 10), item_type=ItemType.MESTHRI, description='MESTHRI', amount=2000, page_num=11)

    item_list.add_item(dt=datetime(2021, 12, 13), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 14), item_type=ItemType.CONSTRUCTION, description='Brick(5000)', amount=55000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 15), item_type=ItemType.MESTHRI, description='MESTHRI', amount=5000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 16), item_type=ItemType.CONSTRUCTION, description='SHOP', amount=44000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 16), item_type=ItemType.CONSTRUCTION, description='20 Cement Bag', amount=9700, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 20), item_type=ItemType.MESTHRI, description='MESTHRI', amount=25000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 25), item_type=ItemType.CONSTRUCTION, description='ElectricityTools', amount=17000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 27), item_type=ItemType.MESTHRI, description='MESTHRI', amount=52000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 22), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electricity man', amount=10000, page_num=12)
    item_list.add_item(dt=datetime(2021, 12, 30), item_type=ItemType.MESTHRI, description='TimberShop', amount=50000, page_num=12)

    item_list.add_item(dt=datetime(2021, 12, 31), item_type=ItemType.CONSTRUCTION, description='Brick(8000)', amount=84000, page_num=13)
    item_list.add_item(dt=datetime(2021, 12, 31), item_type=ItemType.CONSTRUCTION, description='Jelly', amount=3000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 3), item_type=ItemType.MESTHRI, description='MESTHRI', amount=21000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 3), item_type=ItemType.CONSTRUCTION, description='Sengal,Manaal,Jelly 5000Balance', amount=34000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 3), item_type=ItemType.CONSTRUCTION, description='20 Cement Bag shop', amount=24000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 5), item_type=ItemType.MESTHRI, description='MESTHRI', amount=6000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 10), item_type=ItemType.MESTHRI, description='MESTHRI', amount=22000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 10), item_type=ItemType.CONSTRUCTION, description='1 1/2 Jelly', amount=2800, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 12), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=13)
    item_list.add_item(dt=datetime(2022, 1, 13), item_type=ItemType.CONSTRUCTION, description='Cement Shop', amount=20000, page_num=13)

    item_list.add_item(dt=datetime(2022, 1, 13), item_type=ItemType.CONSTRUCTION, description='3/4 Jelly', amount=8000, page_num=14)
    item_list.add_item(dt=datetime(2022, 1, 21), item_type=ItemType.CONSTRUCTION, description='Kambi Kadaikku', amount=50000, page_num=14)
    item_list.add_item(dt=datetime(2022, 1, 24), item_type=ItemType.MESTHRI, description='MESTHRI', amount=25000, page_num=14)
    item_list.add_item(dt=datetime(2022, 1, 31), item_type=ItemType.MESTHRI, description='MESTHRI', amount=19000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 2), item_type=ItemType.CONSTRUCTION, description='Manal, MSand', amount=12000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 3), item_type=ItemType.CONSTRUCTION, description='Kadaikku', amount=25000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 5), item_type=ItemType.TILES, description='Tiles for sump water', amount=18000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 5), item_type=ItemType.CARPENTER, description='Wood shop for door', amount=27000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 7), item_type=ItemType.MESTHRI, description='MESTHRI', amount=36000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 11), item_type=ItemType.CONSTRUCTION, description='Sump lid 4 nos', amount=7300, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 12), item_type=ItemType.CARPENTER, description='Carpenter work for door', amount=10000, page_num=14)
    item_list.add_item(dt=datetime(2022, 2, 14), item_type=ItemType.MESTHRI, description='MESTHRI', amount=15000, page_num=14)

    item_list.add_item(dt=datetime(2022, 2, 16), item_type=ItemType.CONSTRUCTION, description='Kadaikku kambi', amount=40000, page_num=15)
    item_list.add_item(dt=datetime(2022, 2, 25), item_type=ItemType.CONSTRUCTION, description='Protico centering', amount=10000, page_num=15)
    item_list.add_item(dt=datetime(2022, 2, 18), item_type=ItemType.MESTHRI, description='MESTHRI', amount=3000, page_num=15)
    item_list.add_item(dt=datetime(2022, 2, 25), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=15)
    item_list.add_item(dt=datetime(2022, 2, 25), item_type=ItemType.CONSTRUCTION, description='Electrician for portico centering', amount=2000, page_num=15)
    item_list.add_item(dt=datetime(2022, 2, 26), item_type=ItemType.CONSTRUCTION, description='Manal', amount=12000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 7), item_type=ItemType.CONSTRUCTION, description='Cement', amount=60000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 7), item_type=ItemType.MESTHRI, description='MESTHRI', amount=8000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 11), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 8), item_type=ItemType.CONSTRUCTION, description='Aathu manal', amount=39000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 11), item_type=ItemType.CONSTRUCTION, description='Pipe boles 3rd', amount=1500, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 15), item_type=ItemType.CONSTRUCTION, description='Electrician tools', amount=10000, page_num=15)
    item_list.add_item(dt=datetime(2022, 3, 15), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=10000, page_num=15)

    item_list.add_item(dt=datetime(2022, 3, 12), item_type=ItemType.CARPENTER, description='Carptenter for door', amount=40000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 16), item_type=ItemType.CARPENTER, description='Carptenter', amount=10000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 19), item_type=ItemType.MESTHRI, description='MESTHRI', amount=16000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 21), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 23), item_type=ItemType.CONSTRUCTION, description='Kambi cement', amount=60000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 25), item_type=ItemType.CONSTRUCTION, description='Manal 5.5 unit', amount=58000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 25), item_type=ItemType.CONSTRUCTION, description='Electrician tools camp', amount=2000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 25), item_type=ItemType.MESTHRI, description='MESTHRI', amount=8500, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 28), item_type=ItemType.MESTHRI, description='MESTHRI', amount=40000, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 28), item_type=ItemType.CONSTRUCTION, description='Kambi', amount=202929, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 29), item_type=ItemType.CONSTRUCTION, description='Electrician tools', amount=17510, page_num=16)
    item_list.add_item(dt=datetime(2022, 3, 29), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician cooley', amount=10000, page_num=16)

    item_list.add_item(dt=datetime(2022, 3, 30), item_type=ItemType.CONSTRUCTION, description='Oil for not leaking roof', amount=3800, page_num=17)
    item_list.add_item(dt=datetime(2022, 3, 30), item_type=ItemType.CONSTRUCTION, description='Kambi extra', amount=1260, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 3), item_type=ItemType.CONSTRUCTION, description='Electrical', amount=3600, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 3), item_type=ItemType.CONSTRUCTION, description='Food for roof day', amount=3000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 4), item_type=ItemType.CONSTRUCTION, description='Manal', amount=60000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 3), item_type=ItemType.CONSTRUCTION, description='Cement', amount=63000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 4), item_type=ItemType.MESTHRI, description='MESTHRI', amount=50000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 3), item_type=ItemType.MESTHRI, description='MESTHRI on roof day', amount=50000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 5), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 8), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=750, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 10), item_type=ItemType.MESTHRI, description='MESTHRI', amount=26000, page_num=17)
    item_list.add_item(dt=datetime(2022, 4, 11), item_type=ItemType.CONSTRUCTION, description='Bricks', amount=81600, page_num=17)

    item_list.add_item(dt=datetime(2022, 4, 11), item_type=ItemType.CONSTRUCTION, description='Parryware', amount=50000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 13), item_type=ItemType.CONSTRUCTION, description='Parryware saradha & sons', amount=60000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 16), item_type=ItemType.CONSTRUCTION, description='Electrician', amount=4000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 18), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 19), item_type=ItemType.MESTHRI, description='MESTHRI', amount=8500, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 19), item_type=ItemType.CONSTRUCTION, description='Machine rent', amount=2000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 21), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 22), item_type=ItemType.CONSTRUCTION, description='Cement shopbill(67014) given: 65000', amount=65000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 22), item_type=ItemType.CONSTRUCTION, description='Windows steal', amount=110000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 25), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 25), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrical tools', amount=20032, page_num=18)
    item_list.add_item(dt=datetime(2022, 4, 25), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=7000, page_num=18)

    item_list.add_item(dt=datetime(2022, 4, 28), item_type=ItemType.CONSTRUCTION, description='Elevation', amount=3000, page_num=19)
    item_list.add_item(dt=datetime(2022, 4, 28), item_type=ItemType.CONSTRUCTION, description='Manal Aathu',amount=58000, page_num=19)
    item_list.add_item(dt=datetime(2022, 4, 30), item_type=ItemType.MESTHRI, description='MESTHRI', amount=7000, page_num=19)
    item_list.add_item(dt=datetime(2022, 4, 30), item_type=ItemType.CONSTRUCTION, description='Courtyard grill, backdroor grill advance', amount=20000, page_num=19)
    item_list.add_item(dt=datetime(2022, 4, 30), item_type=ItemType.CONSTRUCTION, description='Electrical tools clamp', amount=2000, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 1), item_type=ItemType.MESTHRI, description='MESTHRI', amount=32000, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 3), item_type=ItemType.MESTHRI, description='MESTHRI', amount=3000, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 3), item_type=ItemType.CONSTRUCTION, description='Window vehicle rent', amount=4500, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 9), item_type=ItemType.MESTHRI, description='MESTHRI', amount=38000, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 6), item_type=ItemType.CONSTRUCTION, description='Courtyard grill', amount=20000, page_num=19)
    item_list.add_item(dt=datetime(2022, 5, 9), item_type=ItemType.CONSTRUCTION, description='Window gate', amount=110000, page_num=19)

    item_list.add_item(dt=datetime(2022, 5, 11), item_type=ItemType.CONSTRUCTION, description='Door windows given 270000', amount=50000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 16), item_type=ItemType.MESTHRI, description='Mesthri Appa sent15K, SS Anna 20K', amount=35000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 17), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician Appa', amount=21000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 23), item_type=ItemType.MESTHRI, description='Anna sent 49K', amount=19000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 16), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=10000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 25), item_type=ItemType.MESTHRI, description='MESTHRI sent Appa', amount=5000, page_num=20)
    item_list.add_item(dt=datetime(2022, 6, 3), item_type=ItemType.CONSTRUCTION, description='Cement 95 bags', amount=45189, page_num=20)
    item_list.add_item(dt=datetime(2022, 6, 3), item_type=ItemType.CONSTRUCTION, description='Bricks', amount=28000, page_num=20)
    item_list.add_item(dt=datetime(2022, 5, 30), item_type=ItemType.MESTHRI, description='MESTHRI on roof day', amount=22000, page_num=20)
    item_list.add_item(dt=datetime(2022, 6, 6), item_type=ItemType.MESTHRI, description='MESTHRI', amount=33000, page_num=20)
    item_list.add_item(dt=datetime(2022, 6, 13), item_type=ItemType.MESTHRI, description='MESTHRI', amount=40000, page_num=20)

    item_list.add_item(dt=datetime(2022, 6, 11), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrical plumbing tools', amount=100000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 21), item_type=ItemType.MESTHRI, description='MESTHRI', amount=22000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 21), item_type=ItemType.CONSTRUCTION, description='Adjustment', amount=500, page_num=21, notes='Adjustment')
    item_list.add_item(dt=datetime(2022, 6, 21), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Plumbing', amount=22500, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 21), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Plumbing', amount=7500, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 21), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=20000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 30), item_type=ItemType.MESTHRI, description='MESTHRI', amount=25000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 30), item_type=ItemType.MESTHRI, description='Appa->Mesthri for monday', amount=15000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 30), item_type=ItemType.PAINTER, description='PAINTER tools Janathachem limestone', amount=13000, page_num=21)
    item_list.add_item(dt=datetime(2022, 6, 30), item_type=ItemType.PAINTER, description='PAINTER advance', amount=10000, page_num=21)
    item_list.add_item(dt=datetime(2022, 7, 4), item_type=ItemType.MESTHRI, description='Sent by sathish', amount=30000, page_num=21, notes='Sent by Sathish')
    item_list.add_item(dt=datetime(2022, 7, 4), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=10000, page_num=21, notes='Sent by Sathish')
    item_list.add_item(dt=datetime(2022, 7, 4), item_type=ItemType.PAINTER, description='PAINTER advance', amount=20000, page_num=21, notes='Sent by Sathish')
    item_list.add_item(dt=datetime(2022, 7, 8), item_type=ItemType.CONSTRUCTION, description='Appa', amount=40000, page_num=21)
    item_list.add_item(dt=datetime(2022, 7, 8), item_type=ItemType.PAINTER, description='Painter 25000, 2 boyes whitecement 2000', amount=27000, page_num=21)

    item_list.add_item(dt=datetime(2022, 7, 9), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 11), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 15), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician Appa', amount=80000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 16), item_type=ItemType.CONSTRUCTION, description='Sump lid', amount=6200, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 18), item_type=ItemType.CONSTRUCTION, description='Bricks', amount=11000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 18), item_type=ItemType.INTERIOR, description='Interior Chandran', amount=50000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 18), item_type=ItemType.MESTHRI, description='MESTHRI', amount=35000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 18), item_type=ItemType.CONSTRUCTION, description='Bricks', amount=11500, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 18), item_type=ItemType.CONSTRUCTION, description='LID', amount=6200, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 20), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician pipe', amount=4000, page_num=22)
    item_list.add_item(dt=datetime(2022, 7, 20), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrical tools', amount=7400, page_num=22)

    item_list.add_item(dt=datetime(2022, 7, 22), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Anna Electrician', amount=11000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 22), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Anna Electrical items', amount=5500, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 22), item_type=ItemType.CONSTRUCTION, description='Anna pilar smoothing paste', amount=5500, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 22), item_type=ItemType.PAINTER, description='PAINTER', amount=30000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 22), item_type=ItemType.INTERIOR, description='Interior Chandran', amount=25000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 24), item_type=ItemType.CONSTRUCTION, description='Compound wall', amount=4900, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 24), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrical tools', amount=6300, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 25), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrical and plumbing sivasakthi hardware', amount=84000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 26), item_type=ItemType.MESTHRI, description='Anna MESTHRI', amount=31000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 26), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Anna Electrician', amount=15000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 26), item_type=ItemType.TILES, description='Anuj tiles', amount=280000, page_num=23)
    item_list.add_item(dt=datetime(2022, 7, 28), item_type=ItemType.CONSTRUCTION, description='Appa Tally 30k, Extra 20K', amount=50000, page_num=23, notes='As per note: 527000')

    item_list.add_item(dt=datetime(2022, 7, 29), item_type=ItemType.PAINTER, description='Painting', amount=40000, page_num=24)
    item_list.add_item(dt=datetime(2022, 7, 29), item_type=ItemType.INTERIOR, description='Interior Chandran', amount=27000, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 1), item_type=ItemType.MESTHRI, description='MESTHRI Appa', amount=20000, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 5), item_type=ItemType.PAINTER, description='Painting', amount=25000, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 6), item_type=ItemType.MESTHRI, description='MESTHRI Appa', amount=10000, page_num=24)
    item_list.add_item(dt=datetime(2022, 7, 30), item_type=ItemType.CONSTRUCTION, description='SentAppa(Sivasakthi clamp and tools)', amount=33000, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 4), item_type=ItemType.CONSTRUCTION, description='B-Sand(Appa)', amount=3500, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='Without details(munnadi bakki)', amount=44039, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='11/7/22(Kambi)', amount=6850, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='15/7/22(cement 10)', amount=4250, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='18/7/22(Kambi)', amount=10600, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='23/7/22(cement 10)', amount=4250, page_num=24)
    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.CONSTRUCTION, description='8/8/22(cement 5)', amount=2200, page_num=24)
    #item_list.add_item(dt=datetime(2022, 8, 13), item_type=ItemType.CONSTRUCTION, description='Lawrence', amount=70000, page_num=24)

    item_list.add_item(dt=datetime(2022, 8, 8), item_type=ItemType.MESTHRI, description='MESTHRI', amount=5000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 12), item_type=ItemType.PAINTER, description='PAINTER', amount=20000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 16), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=30000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 16), item_type=ItemType.MESTHRI, description='MESTHRI', amount=15000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 16), item_type=ItemType.PAINTER, description='Paint shop bill', amount=8500, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 16), item_type=ItemType.CONSTRUCTION, description='3 stool rent', amount=4000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 22), item_type=ItemType.CONSTRUCTION, description='Appa', amount=20000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 23), item_type=ItemType.TILES, description='Granite Anna 10,000 Advance', amount=91000, page_num=25)
    item_list.add_item(dt=datetime(2022, 8, 23), item_type=ItemType.MESTHRI, description='MESTHRI Anna', amount=15000, page_num=25)

    item_list.add_item(dt=datetime(2022, 8, 24), item_type=ItemType.TILES, description='Tiles vehicle charge from Madurai', amount=9500, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 25), item_type=ItemType.TILES, description='Granite vehicle charge from Madurai', amount=9500, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 27), item_type=ItemType.CONSTRUCTION, description='Rough piece',  amount=11000, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 27), item_type=ItemType.CONSTRUCTION, description='Sunnambu', amount=5500, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 29), item_type=ItemType.MESTHRI, description='MESTHRI', amount=9000, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 30), item_type=ItemType.TILES, description='Floor tiles Anuj tiles', amount=93000, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 30), item_type=ItemType.TILES, description='vehicle charge for tiles', amount=7000, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 30), item_type=ItemType.CONSTRUCTION, description='Msand', amount=12000, page_num=26)
    item_list.add_item(dt=datetime(2022, 8, 31), item_type=ItemType.TILES, description='Food charges', amount=3000, page_num=26)

    item_list.add_item(dt=datetime(2022, 9, 1), item_type=ItemType.CONSTRUCTION, description='Washbasin', amount=3000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 3), item_type=ItemType.CONSTRUCTION, description='Msand', amount=12000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 6), item_type=ItemType.MESTHRI, description='MESTHRI', amount=5000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 6), item_type=ItemType.TILES, description='Food charges', amount=3000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 6), item_type=ItemType.CONSTRUCTION, description='Eeshwar electricals', amount=88000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 8), item_type=ItemType.TILES, description='Tiles cooley', amount=8000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 9), item_type=ItemType.TILES, description='TILES', amount=22000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 8), item_type=ItemType.TILES, description='Paste granite', amount=900, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 10), item_type=ItemType.TILES, description='Tiles cooley', amount=30000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 10), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Anna(Electrician)', amount=15000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 13), item_type=ItemType.CONSTRUCTION, description='Electricals Eeshwar tubelights', amount=11000, page_num=27)
    item_list.add_item(dt=datetime(2022, 9, 12), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=27)

    item_list.add_item(dt=datetime(2022, 9, 12), item_type=ItemType.TILES, description='Paste granite', amount=950, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 15), item_type=ItemType.TILES, description='Food charges', amount=4500, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 17), item_type=ItemType.CONSTRUCTION, description='Msand 1-unit', amount=12000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 17), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=2000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 17), item_type=ItemType.TILES, description='Tiles cooley', amount=20000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 21), item_type=ItemType.CONSTRUCTION, description='Electrical tools Sivasakthi electricals', amount=14000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 22), item_type=ItemType.TILES, description='Tiles cooley', amount=20000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 22), item_type=ItemType.TILES, description='Food charges', amount=4600, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 26), item_type=ItemType.TILES, description='Tiles cooley', amount=20000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Anna - Electrician', amount=20000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.TILES, description='Anna - Tiles cooley', amount=5000, page_num=28)
    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.CONSTRUCTION, description='Anna - Pipe connector', amount=7000, page_num=28)

    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.TILES, description='Food charges', amount=4800, page_num=29)
    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.TILES, description='Granite paste', amount=950, page_num=29)
    item_list.add_item(dt=datetime(2022, 9, 27), item_type=ItemType.TILES, description='Food charges inhand', amount=3000, page_num=29)
    item_list.add_item(dt=datetime(2022, 9, 29), item_type=ItemType.MESTHRI, description='MESTHRI', amount=10000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 4), item_type=ItemType.TILES, description='Granite adding coutryard', amount=9000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 4), item_type=ItemType.TILES, description='TILES', amount=10000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 2), item_type=ItemType.TILES, description='TILES', amount=20000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 8), item_type=ItemType.TILES, description='Food charges', amount=4000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 8), item_type=ItemType.TILES, description='TILES', amount=20000, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 10), item_type=ItemType.CONSTRUCTION, description='Manal', amount=12500, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 10), item_type=ItemType.TILES, description='Tiles outdoor', amount=4800, page_num=29)
    item_list.add_item(dt=datetime(2022, 10, 10), item_type=ItemType.TILES, description='Cement paste', amount=700, page_num=29)

    item_list.add_item(dt=datetime(2022, 10, 10), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Sivasakthi electricals Bill 21985 Rs', amount=20000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 10), item_type=ItemType.CONSTRUCTION, description='Ceemnt Lawrence', amount=50000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 17), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=10000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.CONSTRUCTION, description='Appa - Saradha', amount=1200, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.CONSTRUCTION, description='Appa - Cement sheet', amount=1900, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.CONSTRUCTION, description='Appa - Brick 500', amount=5500, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.CONSTRUCTION, description='Appa - Gravel Jelly', amount=7000, page_num=30)
    item_list.add_item(dt=datetime(2022, 10, 20), item_type=ItemType.CONSTRUCTION, description='Appa - MSK Cement works', amount=3500, page_num=30)

    item_list.add_item(dt=datetime(2022, 10, 21), item_type=ItemType.PAINTER, description='PAINTER', amount=20000, page_num=31)
    item_list.add_item(dt=datetime(2022, 10, 21), item_type=ItemType.PAINTER, description='Hari paint box', amount=200000, page_num=31)
    item_list.add_item(dt=datetime(2022, 10, 31), item_type=ItemType.MESTHRI, description='MESTHRI', amount=15000, page_num=31)
    item_list.add_item(dt=datetime(2022, 10, 31), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Tank(Eeshwar electricals)', amount=26000, page_num=31)
    item_list.add_item(dt=datetime(2022, 11, 4), item_type=ItemType.GOVT, description='tax(corporation office)', amount=4800, page_num=31)
    item_list.add_item(dt=datetime(2022, 11, 12), item_type=ItemType.CONSTRUCTION, description='Gate vehicle charges', amount=3500, page_num=31)
    item_list.add_item(dt=datetime(2022, 11, 12), item_type=ItemType.MESTHRI, description='MESTHRI', amount=3000, page_num=31)
    item_list.add_item(dt=datetime(2022, 11, 12), item_type=ItemType.CONSTRUCTION, description='Gate Chnadran anna', amount=35000, page_num=31)
    item_list.add_item(dt=datetime(2022, 11, 13), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=15000, page_num=31)

    item_list.add_item(dt=datetime(2022, 11, 21), item_type=ItemType.MESTHRI, description='MESTHRI', amount=20000, page_num=32)
    item_list.add_item(dt=datetime(2022, 11, 22), item_type=ItemType.PAINTER, description='Chandran', amount=30000, page_num=32)
    item_list.add_item(dt=datetime(2022, 11, 30), item_type=ItemType.CONSTRUCTION, description='Chandran steps poke', amount=50000, page_num=32)
    item_list.add_item(dt=datetime(2022, 12, 5), item_type=ItemType.GLASS_WORK, description='Glass for courtyard & balcony', amount=200000, page_num=32)
    item_list.add_item(dt=datetime(2022, 12, 12), item_type=ItemType.CONSTRUCTION, description='Bathroom doors', amount=54300, page_num=32)
    item_list.add_item(dt=datetime(2022, 12, 17), item_type=ItemType.CONSTRUCTION, description='Saradha settlement Appa', amount=14500, page_num=32)
    item_list.add_item(dt=datetime(2022, 12, 19), item_type=ItemType.INTERIOR, description='Interiors chandran', amount=150000, page_num=32)
    item_list.add_item(dt=datetime(2022, 12, 19), item_type=ItemType.INTERIOR, description='Mosquito net', amount=60000, page_num=32)

    item_list.add_item(dt=datetime(2023, 1, 2), item_type=ItemType.PAINTER, description='PAINTER', amount=8000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 2), item_type=ItemType.CONSTRUCTION, description='Window glass fitting: chandran bill', amount=17500, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 2), item_type=ItemType.CONSTRUCTION, description='App for front door', amount=25000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 4), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Electrician', amount=25000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 4), item_type=ItemType.ELECTRICIAN_PLUMBING, description='Easwar elctricals', amount=50500, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 4), item_type=ItemType.GLASS_WORK, description='Raja glass works', amount=50000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 10), item_type=ItemType.TILES, description='Tiles completion work', amount=10000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 10), item_type=ItemType.TILES, description='Tiles velan tiles', amount=11000, page_num=34)
    item_list.add_item(dt=datetime(2023, 1, 10), item_type=ItemType.PAINTER, description='Appa painter settle, electical tools', amount=30000, page_num=34)

    item_list.add_item(dt=datetime(2023, 1, 10), item_type=ItemType.CONSTRUCTION, description='Pooja handle expenses', amount=16400, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 10), item_type=ItemType.TILES, description='Anuj front tile 15 boxes', amount=6000, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 12), item_type=ItemType.TILES, description='Anna compound tiles and other stuff', amount=6000, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 11), item_type=ItemType.FURNITURES, description='Furnitures', amount=78000, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 11), item_type=ItemType.CONSTRUCTION, description='Amazon sink top', amount=3591, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 13), item_type=ItemType.CONSTRUCTION, description='Anna Maindoor settlement', amount=25000, page_num=35)
    item_list.add_item(dt=datetime(2023, 1, 13), item_type=ItemType.CONSTRUCTION, description='Anna mainddoor fitting', amount=11000, page_num=35)

@click.command()
@click.option('--page_wise_sum', '-ps', is_flag=True, default=False, help='Page wise individual')
@click.option('--item_wise_sum', '-is', is_flag=True, default=False, help='Item wise total')
@click.option('--total_value', '-t', is_flag=True, default=False, help='Page wise Total')
@click.option('--item_wise_detail_painter', '-idp', is_flag=True, default=False, help='Item wise entries for painter')
@click.option('--item_wise_detail_electrician', '-ide', is_flag=True, default=False, help='Item wise entries for electrician')
@click.option('--item_wise_detail_interior', '-idi', is_flag=True, default=False, help='Item wise entries for interior')
@click.option('--item_wise_detail_tiles', '-idt', is_flag=True, default=False, help='Item wise entries for tiles')
@click.option('--item_wise_detail_carpenter', '-idc', is_flag=True, default=False, help='Item wise entries for carpenter')
@click.option('--item_wise_detail_glasswork', '-idg', is_flag=True, default=False, help='Item wise entries for glasswork')
def summary(page_wise_sum, item_wise_sum, total_value, item_wise_detail_painter,
            item_wise_detail_electrician, item_wise_detail_interior, item_wise_detail_tiles,
            item_wise_detail_carpenter, item_wise_detail_glasswork):
    item_list = ItemList()
    populate_items(item_list)
    fns = {'page_wise_sum': (page_wise_sum, item_list.page_wise_sum),
           'item_wise_sum': (item_wise_sum, item_list.item_wise_sum),
           'total_value': (total_value, item_list.total),
           'item_wise_detail_painter': (item_wise_detail_painter, item_list.item_wise_detail_painter),
           'item_wise_detail_electrician': (item_wise_detail_electrician, item_list.item_wise_detail_electrician),
           'item_wise_detail_interior': (item_wise_detail_interior, item_list.item_wise_detail_interior),
           'item_wise_detail_tiles': (item_wise_detail_tiles, item_list.item_wise_detail_tiles),
           'item_wise_detail_carpenter': (item_wise_detail_carpenter, item_list.item_wise_detail_carpenter),
           'item_wise_detail_glasswork': (item_wise_detail_glasswork, item_list.item_wise_detail_glasswork),}
    for k, v in fns.items():
        option_value, fn = v
        print(f'{k}, {option_value}')

    for k, v in fns.items():
        option_value, fn = v
        if option_value:
            fn()

if __name__ == '__main__':
    summary()
    print("House expenses copied from Aruna's note")
