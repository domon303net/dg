from sect.base import Sect


class MoJiaoSect(Sect):
    """
    魔教
    """

    def __init__(self, **kwargs):
        super(MoJiaoSect, self).__init__(**kwargs)

        self.name = "魔教"
        self.skill = {
            5: "一刀两断",
            15: "十步一杀",
            30: "盛者必衰",
            50: "生者必灭",
            75: "血战八方",
            105: "屠龙刀法",
        }
        self.heart_method = "魔教心法"

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.heart_method




