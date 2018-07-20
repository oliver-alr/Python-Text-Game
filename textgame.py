print("=" * 100)
print("""         >>> AVENTURA ZOMBIE <<<
Creado por Oliver ALR. Version 1.0.1. Desarrollado en Python 3.6.x""")
print("=" * 100)

import time
measure = time.time()
class room_3:
    def enter(self):
        survive_0 = ["tomarlo","guardar","tomar","agarrar","añadir","añadirlo","coger","cogerlo"]
        print("""
        Estas en la línea del metro, te encuentras justo en
        una habitación. Sólo recuerda que tu misión debe ser
        encontrar el botón maestro y presionarlo
        asi harás volar la ciudad de México entera para erradicar el virus,
        tienes enfrente una linterna, un cuchillo y una granada.
        ¿Qué quieres hacer?""")

        a_0 = input("> ")
        if a_0 in survive_0:
            print("""
            Has añadido los accesorios a tu bolsillo, ahora
            tienes una puerta enfrente de ti, ¿qué quieres hacer? """)
            a_1 = input("> ")
            if "abrir" in a_1:
                print("""
                Has abierto la puerta,ahora te encuentras en la
                estación Nezahuacoyotl,estás seguro por ahora.""")
                return grantsStation.enter(self)
            else:
                return death.death_0(self)

        else:
            return death.death_0(self)

class grantsStation:
    def enter(self):
        print("""
        Tienes enfrente de ti una camino hacia el tren y un
        cuarto oscuro tú puedes seleccionar uno de estos para
        arrivar a tu destino, ¿pero qué camino escogerás?""")
        b_0 = input("> ")
        if "tren" in b_0:
            return train.enter(self)
    elif "cuarto" in b_0:
            return room_2.enter(self)
        else:
            return death.death_1(self)

class room_2:
    def enter(self):
        print("""
        Genial este lugar es seguro, debes tomarlo
        el camino hacia el drenaje para llegar a
        tu objetivo, ¿Quieres continuar o ya te dió
        miedito?""")
        d_0 = input("> ")
        if "si" in d_0:
            return Drain.enter(self)
        else:
            return death.death_0(self)

class train:
    def enter(self):
        attack = ["usar cuchillo","golpear","defenderse","cuchillo","atacar","pelear"]
        print("""
        Estás adentro del tren ahora pero tienes
        un zombi en frente de ti, esta a punto de
        atacar, ¿Qué quieres hacer?""")
        c_0 = input("> ")
        if c_0 in attack:
            print("Bien has matado al zombi, estás seguro por ahora.")
        else:
            return death.death_2(self)

class engine(room_3):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        return room_3.enter(self)

class death:
    def death_0(self):
        print("""
        One zombie enter in the room, you don´t have time to take
        the weapons, and now you´re dead!""")

    def death_1(self):
        print("""
        You´ve stay in the station an now is dangerous, you attack with
        the knife but there are a lot of zombies, you can´t fight with all
        and they eat your brain, you´re dead now.""")

    def death_2(self):
        print("""The Zombie eat your brain!, now you´re dead.""")

    def death_3(self):
        print("""
        One zombie found you!,
        you don´t have time to run, you´re dead now""")

    def death_4(self):
        print("""
        There are a huge amount of zombies in front of you.
        and all attack at the same time.You´re dead now.""")
        print("""

        ++             ++
        ++             ++
        ++             ++
        ++             ++
        ++_____________++
          (  **   **  )
          (     ^     )
          (_____O_____)
               ¡¡¡

        FUCK YOU BITCH!""")

class Drain:
    def enter(self):
        print("""
        You´ve been entered into the Drain
        you have two path left and right, what do you want to choose?""")
        e_0 = input("> ")
        if "left" in e_0:
            print("""
            Cool!, you´re now in the safe area,
            are you sure to continue?""")
            input("> ")
            print("""
            There are 2 path, left and right again
            what do you want to choose?""")
            des_01 = input("> ")
            if "left" in des_01:
                city.enter(self)
            else:
                finalZone.enter(self)
        else:
            return death.death_3(self)


class finalZone:
    def enter(self):
        print("""
        You´ve been entered at the Final Zone!.
        You have door 1 and door 2 in front of you, what
        do you want to open?""")
        select = input("> ")
        if "door 1" in select:
            print("""
            You´ve found a family, but
            they are in danger!, what you want to do?""")
            select_0 = input("> ")
            if "save" in select_0:
                return death.death_4(self)
            else:
                print("""
                You´re safe now,
                but you don´t have time to press the button""")
                return death.death_3(self)
        else:
            print("""
            You´ve been arrived at the final room.
            You´ve found the button, do you want
            to scape and do not press the button?,
            or you want to die saving the city?""")
            select_1 = input("> ")
            options = ["prees","button","press","touch"]
            options_1 = ["scape", "run","exit","end"]
            if select_1 in options:
                print("""
                You´re a hero, all the world loves you!

                        *******************
                        *                 *
                         *      HERO     *
                          *             *
                           *************
                                ****
                                ****
                                ****
                            ************
                                """)
            else:
                return death.death_4(self)

class city():
    def enter(self):
        print("""
        You access at Downtown, there are a lot of
        zombies, you can´t protect yourself
        """)
        return death.death_4(self)

class Map(engine):
    def __init__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass

start = Map("Room 3")
start.play()
print(" ----- ---- ---- END OF THE GAME ---- ---- -----")
measure_0 = time.time()
print("Your elapsed time is: ", measure_0 - measure, "seconds.")
print("=" * 100)
