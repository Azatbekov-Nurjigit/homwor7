# print('Выберите +  -  /  *  для вычесления cpu и  memory')  dd = input()
class Computer:

    def __init__(self,cpu ,memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return
    @cpu.setter
    def cpu(self, value):
        pass
    @property
    def memory(self):
        return
    @memory.setter
    def memory(self, value):
        pass

    def make_computations(self,):
        print(f" {self.__cpu + self.memory}\n"
              f"subtraction: {self.__cpu - self.__memory}\n"
              f"multiplication: {self.__cpu * self.__memory}\n"
              f"division: {self.__cpu / self.__memory}\n")






    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __str__(self):
        return self. make_computations


class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def __str__(self):
        return f' {self.sim_cards_list}'


    def call(self,sim_card_number,call_to_number):
        self.__sim_card_number = sim_card_number
        self.__call_to_number = call_to_number
        if sim_card_number == 1:
            print(f'Идет звонок на номер { call_to_number} с сим-карты { sim_card_number} ')
        elif sim_card_number == 2:
              print(f'Идет звонок на номер { call_to_number} с сим-карты { sim_card_number} ')
        else:
            print('Oшибка. Наберите только 1 или 2')


    #     return

class SmartPhone(Computer,Phone):
    def __init__(self,cpu ,memory,sim_cards_list):
        Phone.__init__(self, sim_cards_list)

        Computer.__init__(self,cpu ,memory)

    def __str__(self):
        print(f' {self.cpu},{self.memory},{self.sim_cards_list}')

    @staticmethod
    def use_gps(location):
        print(f' До {location} осталось 400 метров , через 20 метров поверните направо.\n' )

# print(f"{SAMSUNG_GALAXY_FOLD_4 == Xiaome_Redmi_10_A}\n"

   #
   #     return
ASUS_E510 = Computer(10, 10)

# '
NOKIA_3610 = Phone('O ' )
print(NOKIA_3610)
NOKIA_3610.call(1," 0708 23 78 25 \n")

SAMSUNG_GALAXY_FOLD_4 = SmartPhone(' 8 ', 12 ,' Bilain  , Megacom ' )
SAMSUNG_GALAXY_FOLD_4.call(2," 0707 23 54 25" )
SAMSUNG_GALAXY_FOLD_4.use_gps('Филармонии')

Xiaome_Redmi_10_A = SmartPhone(' 6 ', 8 ," O , Bilain " )
Xiaome_Redmi_10_A.call(1," 0708 27 94 25" )
Xiaome_Redmi_10_A.use_gps('Аламедина')

print(f'{SAMSUNG_GALAXY_FOLD_4 == Xiaome_Redmi_10_A}\n'
     f'{SAMSUNG_GALAXY_FOLD_4 < Xiaome_Redmi_10_A}\n'
     f'{SAMSUNG_GALAXY_FOLD_4 > Xiaome_Redmi_10_A}')

# Xiaome_Redmi_10_A = Phone('O , ','FF',"  " )
# ASUS_E510 = Computer.make_computations(45,55)
# print(ASUS_E510)
# NOKIA_3610 = P.,call(45,45)
# print(NOKIA_3610)
# Phone.call('ff','ff')
# zvonok =
# print(zvonok)


#
# ASUS_E510
# NOKIA 3610
# SAMSUNG GALAXY FOLD 4
# Xiaome Redmi 10 A
# ДЗ*:
# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись
# арифметические вычисления с атрибутами объекта cpu и memory.
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# 3. Добавить сеттеры и геттеры к существующему атрибуту.
# 4. Добавить в класс Phone метод call с входящим параметром sim_card_number и
# call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от
# переданного номера сим-карты (например: если при вызове метода передать число 1 и
# номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с
# сим-карты-1 - Beeline).
# 5. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 6. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который
# бы распечатывал симуляцию проложения маршрута до локации.
# 7. В каждом классе переопределить магический метод __str__ которые бы возвращали
# полную информацию об объекте.
# 8. Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно
# было сравнивать между собой объекты, по атрибуту memory.
# 9. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 10. Распечатать информацию о созданных объектах
# 11. Опробовать все возможные методы каждого объекта (например: use_gps, а также
# магические методы и тд.)


