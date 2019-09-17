from sect.base import Sect


class ShaoLinSect(Sect):
    """
    少林
    """

    def __init__(self, **kwargs):
        super(ShaoLinSect, self).__init__(**kwargs)

        self.name = "少林"
        self.skill = {
            5: "罗汉拳",
            15: "无相劫指",
            30: "韦陀掌",
            50: "狮吼功",
            75: "如来千叶手",
            105: "金刚般若功",
        }
        self.heart_method = "少林心法"

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.heart_method




