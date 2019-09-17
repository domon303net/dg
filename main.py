"""侠义岛"""
from character.base import Character
from element.fight import combat, do_attack
from monster.antu import JianWang, ZuQing
from sect import ShaoLinSect, EMeiSect, WuDangSect, MoJiaoSect, TangMenSect


def main():
    print("welcome to xia yi dao!")
    input("please Enter to continue!")

    name = input(">>>请输入角色名：")
    if name:
        print("welcome %s !!!" % name)
        sect = None
        sect_input = input(""">>>请选择门派：
                              1: 少林
                              2: 武当
                              3: 魔教
                              4: 峨眉
                              5: 唐门""")
        if sect_input == "1":
            sect = ShaoLinSect()

        chara = Character(name, 'nan', 'daxia', sect)
        npc2 = JianWang()
        while True:
            print(chara.get_character_info())
            do = input(">>>input 'S' attacked monster!")
            if do == "s":
                npc1 = ZuQing()
                character_value, monster_value = combat(chara.get_combat_value(), npc1.get_combat_value())
                while True:
                    c_blood, m_blood, c_survive, m_survive = do_attack(chara, npc1, character_value, monster_value)
                    print(">>>monster's blood:", m_blood)
                    print(">>>chara's blood:", c_blood)
                    if not m_survive:
                        print("你杀死了怪物！")
                        break
                    if not c_survive:
                        print("你死了！")
                        exit(1)
            elif do == "e":
                exit(1)
            elif do == "x":
                character_value, monster_value = combat(chara.get_combat_value(), npc2.get_combat_value())
                while True:
                    c_blood, m_blood, c_survive, m_survive = do_attack(chara, npc2, character_value, monster_value)
                    print(">>>monster's blood:", m_blood)
                    print(">>>chara's blood:", c_blood)
                    if not m_survive:
                        print("你杀死了怪物！")
                        break
                    if not c_survive:
                        print("你死了！")
                        exit(1)


if __name__ == '__main__':
    main()
