

class Sect(object):
    """sect"""
    def __init__(self, **kwargs):
        self.name = None
        self.hear_method = None
        self.skill = None

    def get_sect_name(self):
        return self.name

    def get_skill_name(self, level):
        return self.skill[level]

    def get_heart_method_name(self):
        return self.hear_method





