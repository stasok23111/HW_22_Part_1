class Warrior:
    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass
class Healer:

    def heal(self):
        pass
    def defense(self):
        pass

    def move(self):
        pass
class Tree:
    def tree_defense(self):
        pass

    def on_fire(self):
        pass
class Trap:
    def trap_attack(self):
        print("It's a trap!") #Like


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
