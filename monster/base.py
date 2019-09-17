class Monster:

    def __init__(self):
        self.name = None
        self.scenes = None
        self.blood = None
        self.attack = None
        self.defense = None
        self.agile = None
        self.experience = None
        self.level = None
        self.combat_value = {}
        self.survive = True

        self.info = {}

    def do_attack(self, value):
        if self.survive:
            self.blood -= value
            if self.blood <= 0:
                self.survive = False
                self.blood = 0
        return self.blood, self.survive

    def get_combat_value(self):
        self.combat_value = {
            "attack": self.attack,
            "defense": self.defense,
            "agile": self.agile
        }
        return self.combat_value

    def get_monster_info(self):
        self.info = {
            "name": self.name,
            "scenes": self.scenes,
            "element": {
                "level": self.level,
                "experience": self.experience,
                "blood": self.blood,
                "attack": self.attack,
                "agile": self.agile,
                "defense": self.defense,
            },
            "survive": self.survive
        }
        return self.info

    def get_monster_experience(self):
        return self.experience
