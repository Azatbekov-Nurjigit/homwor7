
from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    SAVE_DAMAGE_AND_REVERT = 2
class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.super_ability

    def __str__(self):
        return f'BOSS {self.name} health: {self.health} damage: {self.damage} ' \
               f'defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        GameEntity.__init__(self, name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            self.__super_ability = None
            raise AttributeError("Wrong data type for super_ability")
        else:
            self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def apply_super_ability(self, boss, heroes):
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_ability(self, boss, heroes):
        Berserk.damage += boss.damage

class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        coeffient = randint(1, 2)
        if coeffient == 1 :
            boss.damage = 0

class Golem(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            hero.health += boss.damage/5
            Golem.health -= boss.damage/5

class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                Witcher.health = hero.health
                Witcher.health = 0


class Avrora(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        f = round_counter
        if f == 2:
            Avrora.damage += boss.damage
            boss.damage = 0
        if f == 4:
            Avrora.damage += boss.damage
            boss.damage = 0


class Druid(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        if 2 < randint(1, 2):
            for hero in heroes:
                hero.health += 50
        if 2 > randint(1, 2):
            if boss.health < 500:
                Druid.damage *= 2.2

class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_ability(self, boss, heroes):
        if round_counter == 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20:
            boss.health -= 85
            for hero in heroes:
                hero.health += 85

class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        from random import randint
        if 4 < randint(1,5):
            boss.damage = 0
            TrickyBastard.damage = 0


class AntMan(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        if round_counter == 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20:
            if 3 < randint(1, 5):
                AntMan.damage *= 2
                AntMan.health *= 2
            if 3 > randint(1, 5):
                AntMan.damage /= 2
                AntMan.health /= 2

class Deku(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        if 2 < randint(1, 2):
            if 2 < randint(1, 2):
                Deku.damage *= 1.2
            if 2 < randint(1, 2):
                Deku.damage *= 1.5
            if 2 < randint(1, 2):
                Deku.damage *= 2

round_counter = 0

def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0:
            hero.hit(boss)
            hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("GULDAN", 1255, 54)
    berserk = Berserk("VLAD", 280, 20)
    thor = Thor("ТОР", 250, 25)
    golem = Golem("ALISA", 660, 20)
    witcher = Witcher("DIO_KAPRIO", 270, 0)
    avrora = Avrora("ANNA", 290, 32)
    druid = Druid("GENDALF", 250, 15)
    hacker = Hacker("ILON_MASK", 260, 20)
    trickyBastard = TrickyBastard("APOSUM", 250, 15)
    deku = Deku("LION", 290, 34)
    heroes_list = [berserk,thor,golem,witcher,avrora,druid,hacker,trickyBastard,deku]

    print_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def print_statistics(boss, heroes):
    print(f'ROUND {round_counter} -----------')
    print(boss)
    for hero in heroes:
        print(hero)
def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead

start()


# ДЗ: Добавить в проект уникальную реализацию суперспособности героев
# 1. Berserk должен получать от босса урон, затем при ударе наносить ему свой урон, плюс
# часть накопленного урона полученного от босса
# 2. Thor, удар по боссу имеет шанс оглушить босса на 1 раунд, вследствие чего босс
# пропускает 1 раунд и не наносит урон героям
# 3. Golem, который имеет увеличенную жизнь но слабый удар. Может принимать на себя
# 1/5 часть урона исходящего от босса по другим игрокам
# 4. Witcher, не наносит урон боссу, но получает урон от босса. Имеет 1 шанс оживить
# первого погибшего героя, отдав ему свою жизнь, при этом погибает сам.
# 5. Avrora, которая может входить в режим невидимости на 2 раунда (т.е не получает урон
# от босса), в тоже время полученный урон в режиме невидимости возвращает боссу в
# последующих раундах. Она может исчезать только один раз за игру
# 6. Druid, который имеет способность рандомно призывать помощника ангела героям или
# же ворона боссу на 1 раунд за всю игру. "Ангел" увеличивает способность медика лечить
# героев на n кол-во. А ворон прибавляет агрессию (увеличивается урон на 50%), боссу
# если его жизнь менее 50%.
# 7. Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и
# переводить его одному из героев
# 8. TrickyBastard, способность которого будет состоять в том, чтобы притвориться мертвым
# в определенном раунде(из случайного выбора), но в следующем раунде он снова вступает
# в бой. При этом он не получает урон и не бьет босса когда притворился мертвым
# 9. AntMan, в каждом раунде он может увеличиться или же уменьшится на N-ный размер,
# также увеличиваются/уменьшаются жизнь и урон, после раунда он возвращается в
# исходный размер
# 10. Deku (сила удара может меняться каждый раунд с шансом 50 на 50, может усилится на 20%,
# 50%, 100%, но при усилении теряется здоровье (чем сильнее усиление, тем больше здоровья
# потеряет герой)






















