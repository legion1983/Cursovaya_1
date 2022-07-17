# Классы_лекция

# print(dir(str))
# # dir дает посмотреть методы класса конкретного
# print(type("Hellow world"))
# type  тип данных показывает, что за класс
#
# peter = Character()
# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)
# print(peter.__dict__)
#
# peter.name = "Peter Parker"
# peter.power = 70
# peter.alias = "Spider-man"
# print(peter.alias)
# print(peter.__dict__)
#
# bruce = Character()
# bruce.name = "Bruce Wayne"
# bruce.power = 85
# bruce.alias = "Batman"
#
# print(bruce.name)
# print(bruce.power)
# print(bruce.energy)
# print(bruce.hands)
# print(bruce.alias)
# print(bruce.__dict__)

# self пишем внутри функции перед переменными и при вызове методов и атрибутов, указывая таким образом их принадлежность к конкретному классу
# self означает что при выводе экземпляра класса надо брать именно значение этого экземпляра класса
# при вызове self указывать не нужно, потому что это то что стоит до точки
class Character:
    name = ""
    power = 0
    energy = 100
    hands = 2
# метод eat класса Character c атрибутом food
    def eat(self, food):
        if self.energy < 100:
           self.energy += food
        else:
            print("Not hungry")

    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print("Too tired")

    def change_alias(self, new_alias):
        print(self)
        self.alias = new_alias
bruce = Character()

# bruce = Character()
# bruce.name = "Bruce Wayne"
# bruce.power = 85
# bruce.change_alias("Batman")
# print(bruce.alias)
# bruce.energy = 80
# bruce.eat(30)
# print(bruce.energy)

# self значит меняй у конкретного экземпляра класса
# __init__ метод, для присвоения переменных корректно, будет изначально присваиваться каждому новому классу заново переменные все. А так можно попасть в жопу со списками, которые в ячейках хранятся и на одну ячейку два экземпляра класса могут сослаться
#
    # def __init__(self, name, power, energy=100, hands=2):
    #     self.name = name
    #     self.power = power
    #     self.energy = energy
    #     self.backpack = []
    #     self.hands = hands
