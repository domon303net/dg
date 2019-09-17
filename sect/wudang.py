from sect.base import Sect


class WuDangSect(Sect):
    """
    武当
    """

    def __init__(self, **kwargs):
        super(WuDangSect, self).__init__(**kwargs)

        self.name = "武当"
        self.skill = {
            5: "武当绵掌",
            15: "真武七绝剑",
            30: "柔云剑法",
            50: "八卦剑法",
            75: "神门十三剑",
            105: "太极拳",
        }
        self.heart_method = "武当心法"

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.heart_method




