import time
import random


class Personaje:
    def __init__(self, nombre, vitalidad, daño):
        self.nombre = nombre
        self.vitalidad = vitalidad
        self.daño = daño

    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

    def recibir_daño(self, daño):
        self.vitalidad -= daño


class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, daño, habilidades):
        super().__init__(nombre, vitalidad, daño)
        self.habilidades = habilidades

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

    # 2. Agregar lógica de contraataque del jugador.
    # 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

    def contraataque(self, enemigo):
        daño = self.daño
        probabilidad = 0.30

        if (random.random() > probabilidad):
            daño *= 1.3
            print(
                f"Jugador {self.nombre} contraatacó al enemigo {enemigo.nombre} con daño critico: {daño}")
        else:
            print(
                f"Jugador {self.nombre} contraatacó al enemigo {enemigo.nombre} con daño: {daño}")

        enemigo.recibir_daño(daño)


class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad, daño)
        self.ataque_esp = ataque_esp

    def atacar_jugador(self, jugador):
        print(
            f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {self.daño}")
        jugador.recibir_daño(self.daño)
        jugador.contraataque(self)

    # 1. Agregar logica de daño aleatorio al enemigo.
    def daño_aleatorio(self, jugador):
        daño_aleatorio = random.randint(1, 40)
        print(
            f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño aleatorio: {daño_aleatorio}")
        jugador.recibir_daño(daño_aleatorio)
        jugador.contraataque(self)


jugador = Jugador("Juan", 100, 10, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 10, 70)

while (jugador.esta_vivo() and enemigo.esta_vivo()):
    # enemigo.atacar_jugador(jugador)
    enemigo.daño_aleatorio(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")
    print(" ")
    time.sleep(2)
    if not (jugador.esta_vivo()):
        print(f"El jugador {jugador.nombre} ha muerto")

    if not (enemigo.esta_vivo()):
        print(f"El enemigo {enemigo.nombre} ha muerto")
