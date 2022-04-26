from Components.case import Case
from Components.cpu import CPU
from Components.graphic_card import GraphicCard
from Components.hard_drive import HDD, SSD
from Components.motherboard import Motherboard
from Components.power_unit import PowerUnit
from Components.ram import RAM


def build_computer():
    power_unit = PowerUnit(brand=input('Введите марку блока питания '),
                           capacity=input('Введите мощность блока питания '))

    drive_type = input('Какой ставим диск? ')
    if drive_type == 'HDD':
        drive = HDD(brand=input('Введите марку диска '),
                    capacity=input('Введите объём '),
                    rotational_speed=input('Введите скорость вращения диска '))
    elif drive_type == 'SSD':
        drive = SSD(brand=input('Введите марку диска '),
                    capacity=input('Введите объём '),
                    read_speed=input('Введите скорость чтения '),
                    write_speed=input('Введите скорость записи '))
    else:
        print('Нет такого диска')

    graphic_card = GraphicCard(brand=input('Введите марку видеокарты '),
                               graphic_type=input('Введите тип графики '),
                               memory=input('Введите объём памяти '))

    motherboard = Motherboard(brand=input('Введите марку материнской платы '),
                              cpu=CPU(brand=input('Введите марку процессора '),
                                      socket=input('Введите сокет '),
                                      model=input('Введите модель процессора '),
                                      frequency=input('Введите частоту процессора ')),
                              form_factor=input('Введите форм-фактор материнской платы '),
                              ram=RAM(brand=input('Введите марку оперативной памяти '),
                                      memory_type=input('Введите тип оперативной памяти '),
                                      capacity=input('Введите объём оперативной памяти ')),
                              quantity_ram=input('Введите количество плашек памяти '))

    case_brand = input('Введите марку системного блока ')

    my_computer = Case(brand=f'Системный блок {case_brand}',
                       motherboard=f'Материнская память {motherboard}',
                       graphic_card=f'Видюха {graphic_card}',
                       drive=f'Диск {drive}',
                       power_unit=f'Блок питания {power_unit}')

    return my_computer


if __name__ == '__main__':
    print(build_computer())
