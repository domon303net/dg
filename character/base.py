
class Character:
    """角色"""
    def __init__(self, name, gender, title, sect):
        """
        角色信息
        name: 名称
        gender: 性别
        title: 称号
        sect: 门派
        info: 信息
        element: 属性
        internal_work: 内功
        external_work: 外功
        agile: 身法
        defense: 防御
        level: 等级
        experience: 经验值
        blood: 血量
        magic: 魔法
        body: 体力
        """
        self.name = name
        self.gender = gender
        self.title = title
        self.sect = sect

        self.info = {}
        self.element = {}

        self.internal_work = 10
        self.external_work = 10
        self.agile = 10
        self.defense = 10

        self.level = 1
        self.experience = 0

        self.blood = 100
        self.magic = 100
        self.body = 100

        self.survive = True

        self.combat_value = {}

    def increase_experience(self, exp):
        """增加经验值"""
        self.experience += exp
        if self.experience == 100:
            self.level += 1
            self.experience = 0
        return self.experience

    def add_blood(self, value):
        """血量恢复"""
        if self.blood < 100:
            self.blood += value
            if self.blood >= 100:
                self.blood = 100
        else:
            self.blood = 100
        return self.blood

    def less_blood(self, value):
        """血量消耗"""
        if self.blood > 0:
            self.blood -= value
            if self.blood <= 0:
                self.blood = 0
                self.survive = False
        else:
            self.survive = False
        return self.blood, self.survive

    def add_magic(self, value):
        """魔法恢复"""
        if self.magic < 100:
            self.magic += value
            if self.magic >= 100:
                self.magic = 100
        else:
            self.magic = 100
        return self.magic

    def less_magic(self, value):
        """魔法消耗"""
        if self.magic > 0:
            self.magic -= value
            if self.magic <= 0:
                self.magic = 0
        return self.magic

    def add_body(self, value):
        """恢复体力"""
        if self.body < 100:
            self.body += value
            if self.body >= 100:
                self.body = 100
        else:
            self.body = 100
        return self.body

    def less_body(self, value):
        """体力消耗"""
        if self.body > 0:
            self.body -= value
            if self.body <= 0:
                self.body = 0
        return self.body

    def get_character_info(self):
        """返回角色的所有信息"""
        self.info = {
            "name": self.name,
            "gender": self.gender,
            "title": self.title,
            "sect": self.sect.get_sect_name(),
            "element": {
                "level": self.level,
                "experience": self.experience,
                "blood": self.blood,
                "magic": self.magic,
                "body": self.body,
                "internal_work": self.internal_work,
                "external_work": self.external_work,
                "agile": self.agile,
                "defense": self.defense,
            },
            "survive": self.survive
        }
        return self.info

    def get_combat_value(self):
        """获取角色的攻击属性"""
        self.combat_value = {
            "internal_work": self.internal_work,
            "external_work": self.external_work,
            "agile": self.agile,
            "defense": self.defense
        }
        return self.combat_value
