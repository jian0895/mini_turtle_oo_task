class Tortuga:
    def __init__(self):
        # Estado interno de cada tortuga
        self.posicion_x = 0

    def adelante(self, camina_adelante):
        print((" " * self.posicion_x) + "→" + ("-" * camina_adelante) + "↓")
        self.posicion_x += camina_adelante + 1

    def abajo(self, camina_abajo):
        for _ in range(camina_abajo):
            print((" " * self.posicion_x) + "|")

    def reiniciar(self):
        self.posicion_x = 0
