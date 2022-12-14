from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    rrrr = 0




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
        Hero.__init__(self, name, health, damage, SuperAbility.rrrr)




    def apply_super_ability(self, boss, heroes):
        self.__saved_damage = SuperAbility.rrrr
        SuperAbility.rrrr += Berserk.damage

class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):
        coeffient = randint(1, 2)
        if coeffient == 1 :
            boss.damage = 0

class Golem(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if Golem.damage

        boss.health -







class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                Witcher.health = hero
                Witcher.health = 0





class Avrora(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):
        boss.damage = 0


class Druid(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):

class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):

class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):

class AntMan(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):

class Deku(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if
        Deku.damage
        boss.health -

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
    boss = Boss("GULDAN", 1000, 50)
    berserk = Berserk("VLAD", 280, 10)
    thor = Thor("??????", 250, 5)
    golem = Golem("ALISA", 260, 20)
    witcher = Witcher("DIO_KAPRIO", 270, 0)
    avrora = Avrora("ANNA", 290, 10)
    druid = Druid("GENDALF", 250, 5)
    hacker = Hacker("ILON_MASK", 260, 20)
    trickyBastard = TrickyBastard("APOSUM", 270, 15)
    deku = Deku("LION", 290, 10)
    heroes_list = [berserk,thor,golem,witcher,avrora,druid,hacker,trickyBastard,deku]

    print_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def print_statistics(boss, heroes):
    print(f'ROUND {round_counter} ------------------')
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

# ????: ???????????????? ?? ???????????? ???????????????????? ???????????????????? ???????????????????????????????? ????????????
# 1. Berserk ???????????? ???????????????? ???? ?????????? ????????, ?????????? ?????? ?????????? ???????????????? ?????? ???????? ????????, ????????
# ?????????? ???????????????????????? ?????????? ?????????????????????? ???? ??????????
# 2. Thor, ???????? ???? ?????????? ?????????? ???????? ???????????????? ?????????? ???? 1 ??????????, ???????????????????? ???????? ????????
# ???????????????????? 1 ?????????? ?? ???? ?????????????? ???????? ????????????
# 3. Golem, ?????????????? ?????????? ?????????????????????? ?????????? ???? ???????????? ????????. ?????????? ?????????????????? ???? ????????
# 1/5 ?????????? ?????????? ???????????????????? ???? ?????????? ???? ???????????? ??????????????
# 4. Witcher, ???? ?????????????? ???????? ??????????, ???? ???????????????? ???????? ???? ??????????. ?????????? 1 ???????? ??????????????
# ?????????????? ?????????????????? ??????????, ?????????? ?????? ???????? ??????????, ?????? ???????? ???????????????? ??????.
# 5. Avrora, ?????????????? ?????????? ?????????????? ?? ?????????? ?????????????????????? ???? 2 ???????????? (??.?? ???? ???????????????? ????????
# ???? ??????????), ?? ???????? ?????????? ???????????????????? ???????? ?? ???????????? ?????????????????????? ???????????????????? ?????????? ??
# ?????????????????????? ??????????????. ?????? ?????????? ???????????????? ???????????? ???????? ?????? ???? ????????
# 6. Druid, ?????????????? ?????????? ?????????????????????? ???????????????? ?????????????????? ?????????????????? ???????????? ???????????? ??????
# ???? ???????????? ?????????? ???? 1 ?????????? ???? ?????? ????????. "??????????" ?????????????????????? ?????????????????????? ???????????? ????????????
# ???????????? ???? n ??????-????. ?? ?????????? ???????????????????? ???????????????? (?????????????????????????? ???????? ???? 50%), ??????????
# ???????? ?????? ?????????? ?????????? 50%.
# 7. Hacker, ?????????????? ?????????? ?????????? ?????????? ???????????????? ?? ?????????? N-???? ???????????????????? ???????????????? ??
# ???????????????????? ?????? ???????????? ???? ????????????
# 8. TrickyBastard, ?????????????????????? ???????????????? ?????????? ???????????????? ?? ??????, ?????????? ???????????????????????? ??????????????
# ?? ???????????????????????? ????????????(???? ???????????????????? ????????????), ???? ?? ?????????????????? ???????????? ???? ?????????? ????????????????
# ?? ??????. ?????? ???????? ???? ???? ???????????????? ???????? ?? ???? ???????? ?????????? ?????????? ?????????????????????? ??????????????
# 9. AntMan, ?? ???????????? ???????????? ???? ?????????? ?????????????????????? ?????? ???? ???????????????????? ???? N-?????? ????????????,
# ?????????? ??????????????????????????/?????????????????????? ?????????? ?? ????????, ?????????? ???????????? ???? ???????????????????????? ??
# ???????????????? ????????????
# 10. Deku (???????? ?????????? ?????????? ???????????????? ???????????? ?????????? ?? ???????????? 50 ???? 50, ?????????? ???????????????? ???? 20%,
# 50%, 100%, ???? ?????? ???????????????? ???????????????? ???????????????? (?????? ?????????????? ????????????????, ?????? ???????????? ????????????????
# ???????????????? ??????????)





