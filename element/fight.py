

def combat(character_combat, monster_combat):
    # 对角色和怪的攻击和防御进行计算
    character_value = character_combat['internal_work'] + character_combat['external_work'] - monster_combat['defense']
    monster_value = monster_combat['attack'] - character_combat['defense']
    if monster_value < 1:
        monster_value = 1
    if character_value < 1:
        character_value = 1
    return character_value, monster_value


def do_attack(chara, npc, c_value, m_value):
    """
    怪和角色进行攻击判定
    :param chara: 角色对象
    :param npc: 怪物对象
    :param c_value: 角色最终输出
    :param m_value: 怪最终输出
    :return: 角色血量，怪血量，角色生存状态，怪生存状态
    """
    m_blood, m_survive = npc.do_attack(c_value)
    c_blood, c_survive = chara.less_blood(m_value)
    if c_survive and not m_survive:
        chara.increase_experience(npc.experience)
    return c_blood, m_blood, c_survive, m_survive





