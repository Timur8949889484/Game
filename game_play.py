import random


class GameEntity:
    def __init__(self, health, damage, name):
        self.__health = health
        self.__damage = damage
        self.__name = name

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f'Name - {self.name}, DAMAGE - {self.damage}, Health - {self.health}'


class BossMonster(GameEntity):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)


class Hero(GameEntity):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        pass


class King(Hero):
    def __init__(self, health, name, damage=0):
        super().__init__(health, damage, name)

    def ability(self):
        rand_num = random.randint(1, 100)

        if rand_num <= 10:
            BossMonster.health = 0
            print(f'{self.name} ВСЕ ХАНА, СУДЬЯ СПАСАТ КЕРИ КУДРЕДЖА ОТ НЕМЕНУЕМ.....СМЕРТИ!!!')


class Deku(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        rand_num = random.randint(1, 100)
        twenty = int(((self.damage / 100) * 20) + self.damage)
        fifty = int(((self.damage / 100) * 50) + self.damage)
        hundred = int(self.damage * 2)

        if rand_num <= 50:
            power_up = random.choice([twenty, fifty, hundred])
            self.damage = power_up

            if power_up == twenty:
                self.health -= 1
                print(f'{self.name} усилился на 20%, минус 1хп')
            elif power_up == fifty:
                self.health -= 2
                print(f'{self.name} усилился на 50%, минус 2хп')
            elif power_up == hundred:
                self.health -= 3
                print(f'{self.name} усилился на 100%, минус 3хп')


class Witcher(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.damage = 0

    def ability(self):
        for hero in heroes:
            if hero.health == 0:
                hero.health = 100
                self.health = 0
                print(f'{self.name} пожертвовал свою жизнь {hero.name}')
                break


class Magic(Hero):
    def __init__(self, health, damage, name, damage_boost):
        super().__init__(health, damage, name)
        self.damage_boost = damage_boost

    def ability(self):
        for hero in heroes:
            hero.damage += self.damage_boost
        print(f'{self.name} увеличил атаку всем на {self.damage_boost}')


class Hacker(Hero):
    def __init__(self, health, damage, name, steal_hp):
        super().__init__(health, damage, name)
        self.__steal_hp = steal_hp
        self.round_counter = 0

    def ability(self):
        self.round_counter += 1
        if self.round_counter % 2 == 0:
            b.health -= self.__steal_hp
            heal_hero = random.choice(heroes)
            heal_hero.health += self.__steal_hp
            print(f'{heal_hero.name} получил {self.__steal_hp} от {self.name}')
            print(self.round_counter)


class Golem(Hero):
    def __init__(self, health, damage, name, boss_damage):
        super().__init__(health, damage, name)
        self.__boss_damage = boss_damage

    def ability(self):
        for hero in heroes:
            hero.health += (b.damage // 5) * 4
            self.health -= (b.damage // 5) * len(heroes)

        print(f'{self.name} ПОМОГ')


class Avrora(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.round_counter = 0

    def ability(self):
        self.round_counter += 1

        if b.damage > 0:
            if self.round_counter <= 2:
                self.health += bossDamage
                b.health -= b.damage
                print(f'{self.name} МЫШЬ КРАДЕТСЯ')


class Medic(Hero):
    def __init__(self, health, damage, name, heal_points):
        super().__init__(health, damage, name)
        self.heal_points = heal_points

    def ability(self):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                #ОУЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ
                hero.health += self.heal_points
                print(f'{self.name}: Aw, dont be such a baby, they will grow back!'
                      f'\nno they will not')


class Druid(Hero):
    def __init__(self, health, damage, name, heal_boost):
        super().__init__(health, damage, name)
        self.heal_boost = heal_boost
        self.round_counter = 0

    def ability(self):
        self.round_counter += 1
        random_number = random.choice([0, 1])

        if self.round_counter == 1:

            if random_number == 0:
                b.damage += d.damage // 2
                print( f'{self.name} хотел как лучше, но получилось как всегда. Урон {b.name} авеличился на {d.damage // 2}')

            else:
                if mm in heroes:
                    mm.heal_points += self.heal_boost
                    print(f'благодоря {self.name} медик полезнее на {self.heal_boost}')
                else:
                    print(f'завидуйте мертвым')


class Thor(Hero):
    def __init__(self, health, damage, name, stan_percent):
        super().__init__(health, damage, name)
        self.__stan_percent = stan_percent

    def ability(self):
        stan_chance = random.randint(1, 100)
        if stan_chance <= self.__stan_percent:
            b.damage = 0
            print(f'{self.name} оглушил {b.name}')
        else:
            b.damage = bossDamage


class TrickyBastard(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        hide_chance = random.randint(1, 100)

        if hide_chance <= 50 and b.damage != 0:
            self.damage = 0
            self.health += 20
            print(f'{self.name} упрятался')
        else:
            self.damage = hopDamage


class Antman(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.boost_health = 20
        self.boost_damage = 20

    def ability(self):
        ant_chance = random.randint(1, 100)

        if ant_chance <= 50:
            self.damage += self.boost_damage
            self.health += self.boost_health
            print(f'{self.name} увеличился')
        else:
            self.damage -= self.boost_damage
            self.health -= self.boost_health
            print(f'{self.name} уменьшился')


class Kamikadze(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.health *= 2

    def ability(self):
        chance_to_boom = random.randint(0, 1)

        if chance_to_boom == 0:
            b.health -= self.health
            self.health = 0
            print(f'{self.name} сделал бум')
        else:
            b.health -= self.health // 2
            self.health = 0
            print(f'{self.name} сделал бум, но хуже')


class Samurai(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        shuriken_impact = 10
        chance_to_shoot = random.randint(0, 1)

        if chance_to_shoot == 1:
            b.health -= shuriken_impact
            print(f'{self.name} вдарил')
        else:
            b.health += shuriken_impact
            print(f'{self.name} ПОЧЕМУ ТУТ НЕТУ ПОМОЩИ')


class Bomber(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        for hero in heroes:
            if hero.health == 0:
                b.health -= 100
                self.health = 0
                print(f'{self.name} не Камикадзе, но сделал бум')


class Reaper(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.	thirty_percent = (self.health // 100) * 30
        self.	fifteen_percent = (self.health // 100) * 15
        self.double_damage = self.damage * 2
        self.triple_damage = self.damage * 3

    def ability(self):
        if self.health < self.thirty_percent:
            self.damage = self.double_damage
            print(f'{self.name} увеличил урон вдвое')
        elif self.health < self.fifteen_percent:
            self.damage = self.triple_damage
            print(f'{self.name} увеличил урон втрое')


class Spitfire(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):

        for hero in heroes:
            if hero.health == 0:
                b.health -= 80
                print(f'{self.name} ударил по {b.name} на 80')
                break


class Ludoman(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        if dice_2 == dice_1:
            b.health -= dice_2 * dice_1
            print('ДЖОКЕР В ИГРЕ')

        elif dice_2 != dice_1:
            for hero in heroes:
                hero.health -= dice_2 + dice_1
                print('Я ВНЕ ИГРЫ')
                break


class Avenger(Hero):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)

    def ability(self):
        avenger_chance = random.randint(1, 100)

        if avenger_chance <= 20:
            b.damage = 0
            print(f'{self.name} спас героев')
        else:
            b.damage = bossDamage


heroes = []

bossDamage = 20
hopDamage = 10
b = BossMonster(100, bossDamage, 'Toriel')

mm = Medic(100, 10, 'МЕДИК', 10)
h = Hero(100, 10, 'Герой')
d = Deku(100, 10, 'Мидория')
h1 = King(100, 'Герой без фантазии', 0)
w = Witcher(100, 10, 'Геральд')
m = Magic(100, 10, 'Акакий', 10)
ha = Hacker(100, 10, 'Хакер', 10)
g = Golem(250, 10, 'Голем', b.damage)
a = Avrora(100, 10, 'Аврора')
dd = Druid(100, 10, 'Малфурион', 50)
t = Thor(100, 10, 'Крис', 50)
tb = TrickyBastard(100, hopDamage, 'Хопер')
aaa = Antman(100, 10, 'мураш')
kk = Kamikadze(100, 10, 'Травоман')
ss = Samurai(100, 10, 'Мусаси')
bbb = Bomber(100, 10, 'Супер')
rrr = Reaper(100, 10, 'Артас')
sss = Spitfire(100, 10, 'Блейх')
j = Ludoman(100, 10, 'Горшок')
av = Avenger(100, 10, 'Америка')

heroes.extend((h, mm))
round_number = 0


def show_statistics():
    print(f'Round {round_number} ------------')
    print(b)
    for hero in heroes:
        print(hero)


def game_over():
    if b.health == 0:
        print('изигглмаовпkys')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('ВПОДВАЛ')
        return True

    return False


def play_rounds():
    global round_number
    round_number += 1
    for hero in heroes:
        hero.health -= b.damage
        if hero.health != 0 and b.health != 0:
            b.health -= hero.damage
    show_statistics()


def start_game():
    show_statistics()
    while not game_over():
        play_rounds()


start_game()
