from sect.base import Sect


class TangMenSect(Sect):
    """
    唐门
    """

    def __init__(self, **kwargs):
        super(TangMenSect, self).__init__(**kwargs)

        self.name = "唐门"
        self.skill = {
            5: "唐花乍现",
            15: "百步穿杨",
            30: "含沙射影",
            50: "风卷残云",
            75: "乱泼狂风",
            105: "唐花怒放",
        }
        self.heart_method = "唐门心法"

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.heart_method




