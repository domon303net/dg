from sect.base import Sect


class EMeiSect(Sect):
    """
    峨眉派
    """

    def __init__(self, **kwargs):
        super(EMeiSect, self).__init__(**kwargs)

        self.name = "峨眉"
        self.skill = {
            5: "回风拂柳",
            15: "飘雪穿云",
            30: "慈航普度",
            50: "截手九式",
            75: "佛光普照",
            105: "九阴白骨爪",
        }
        self.heart_method = "峨眉心法"

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.heart_method




