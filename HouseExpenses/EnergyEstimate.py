# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import pandas as pd
import calendar


class Charges:
    def __init__(self):
        self.gas_unit = {}
        self.electricity_unit = {}
        self.gas_rate = {}
        self.electricity_rate = {}

    def add(self, date_value, gas_unit, elec_unit, gas_rate, elec_unit_rate):
        self.gas_unit.update({date_value: gas_unit})
        self.electricity_unit.update({date_value: elec_unit})
        self.gas_rate.update({date_value: gas_rate})
        self.electricity_rate.update({date_value: elec_unit_rate})

    def as_csv(self):
        df = pd.DataFrame()
        df['dts'] = self.gas_unit.keys()
        df['gas_unit'] = self.gas_unit.values()
        df['electricity_unit'] = self.electricity_unit.values()
        df['gas_rate'] = self.gas_rate.values()
        df['electricity_rate'] = self.electricity_rate.values()

        num_days = []
        for val in df['dts']:
            num_days.append(calendar.monthrange(val.year, val.month)[1])

        df['num_days'] = num_days
        return df

def calculate_values(header, df, gas_si, elec_si, gas_per_unit, elec_per_unit):
    calculated_gas_rate = []
    calculated_electricity_rate = []
    calculated_total_rate = []
    for index, row in df.iterrows():
        gas_value = (row['num_days'] * gas_si) + (row['gas_unit'] * gas_per_unit)
        elec_value = (row['num_days'] * elec_si) + (row['electricity_unit'] * elec_per_unit)
        calculated_gas_rate.append(gas_value/100)
        calculated_electricity_rate.append(elec_value/100)
        calculated_total_rate.append((gas_value/100) + (elec_value/100))
    df[f'{header}_gas_rate'] = calculated_gas_rate
    df[f'{header}_electricity_rate'] = calculated_electricity_rate
    df[f'{header}_total_rate'] = calculated_total_rate


def usage_data(charges):
    charges.add(date_value=datetime(2023, 1, 1), gas_unit=671.72, elec_unit=104, gas_rate=22.13, elec_unit_rate=27.65)
    charges.add(date_value=datetime(2023, 2, 1), gas_unit=488.12, elec_unit=67, gas_rate=16.08, elec_unit_rate=19.88)
    charges.add(date_value=datetime(2023, 3, 1), gas_unit=509.08, elec_unit=102, gas_rate=16.77, elec_unit_rate=27.27)
    charges.add(date_value=datetime(2023, 4, 1), gas_unit=435.69, elec_unit=110, gas_rate=14.35, elec_unit_rate=28.52)

    charges.add(date_value=datetime(2022, 1, 1), gas_unit=629.59, elec_unit=177, gas_rate=20.72, elec_unit_rate=41.45)
    charges.add(date_value=datetime(2022, 2, 1), gas_unit=379.29, elec_unit=121, gas_rate=12.27, elec_unit_rate=30.09)
    charges.add(date_value=datetime(2022, 3, 1), gas_unit=341.23, elec_unit=114, gas_rate=11.24, elec_unit_rate=29.54)
    charges.add(date_value=datetime(2022, 4, 1), gas_unit=301.8, elec_unit=121, gas_rate=9.94, elec_unit_rate=30.60)

    charges.add(date_value=datetime(2022, 5, 1), gas_unit=226.3, elec_unit=102, gas_rate=7.46, elec_unit_rate=27.27)
    charges.add(date_value=datetime(2022, 6, 1), gas_unit=165.07, elec_unit=99, gas_rate=5.44, elec_unit_rate=26.45)
    charges.add(date_value=datetime(2022, 7, 1), gas_unit=166.41, elec_unit=106, gas_rate=5.49, elec_unit_rate=28.03)
    charges.add(date_value=datetime(2022, 8, 1), gas_unit=200.46, elec_unit=110, gas_rate=6.60, elec_unit_rate=28.78)

    charges.add(date_value=datetime(2022, 9, 1), gas_unit=231.1, elec_unit=101, gas_rate=7.61, elec_unit_rate=26.82)
    charges.add(date_value=datetime(2022, 10, 1), gas_unit=331.79, elec_unit=104, gas_rate=10.93, elec_unit_rate=27.65)
    charges.add(date_value=datetime(2022, 11, 1), gas_unit=421.17, elec_unit=127, gas_rate=14.06, elec_unit_rate=31.74)
    charges.add(date_value=datetime(2022, 12, 1), gas_unit=669.46, elec_unit=127, gas_rate=22.06, elec_unit_rate=32.00)

    charges.add(date_value=datetime(2021, 5, 1), gas_unit=330.21, elec_unit=105, gas_rate=10.88, elec_unit_rate=27.84)
    charges.add(date_value=datetime(2021, 6, 1), gas_unit=148.61, elec_unit=105, gas_rate=4.89, elec_unit_rate=27.58)
    charges.add(date_value=datetime(2021, 7, 1), gas_unit=120.38, elec_unit=103, gas_rate=3.97, elec_unit_rate=27.46)
    charges.add(date_value=datetime(2021, 8, 1), gas_unit=102.18, elec_unit=105, gas_rate=3.36, elec_unit_rate=27.84)

    charges.add(date_value=datetime(2021, 9, 1), gas_unit=125.76, elec_unit=106, gas_rate=4.14, elec_unit_rate=27.77)
    charges.add(date_value=datetime(2021, 10, 1), gas_unit=350.61, elec_unit=133, gas_rate=11.55, elec_unit_rate=33.13)
    charges.add(date_value=datetime(2021, 11, 1), gas_unit=455.02, elec_unit=128, gas_rate=14.99, elec_unit_rate=31.93)
    charges.add(date_value=datetime(2021, 12, 1), gas_unit=694.3, elec_unit=157, gas_rate=22.88, elec_unit_rate=37.67)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    charges = Charges()
    usage_data(charges)
    result_df = charges.as_csv()
    calculate_values(header="used_rate", df=result_df, gas_si=27.66,
                     gas_per_unit=3.294, elec_si=24.54, elec_per_unit=18.003)
    calculate_values(header="new_rate", df=result_df, gas_si=29.11,
                     gas_per_unit=10.316, elec_si=38.18, elec_per_unit=34.684)
    print(result_df.to_string())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
