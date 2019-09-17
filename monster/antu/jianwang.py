from monster.antu.base import AntuMonster


class JianWang(AntuMonster):

    def __init__(self):
        super(JianWang, self).__init__()
        self.name = "扶桑剑王"
        self.blood = 500
        self.attack = 50
        self.experience = 500
        self.defense = 100
        self.agile = 100
        self.level = 10
        self.survive = True
