class Enemy:
    def __init__(self, name, hp, damage, enemy_type):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.enemy_type = enemy_type

    def attack(self):
        return self.damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True
        return False
    

