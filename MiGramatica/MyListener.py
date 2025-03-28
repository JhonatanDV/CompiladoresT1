from antlr4 import *
from MiGramaticaListener import MiGramaticaListener
from MiGramaticaParser import MiGramaticaParser

class MyListener(MiGramaticaListener):
    def __init__(self):
        self.nivell = 0
        self.eventos = []

    def exitForLoop(self, ctx:MiGramaticaParser.ForLoopContext):
        print(" " * self.nivell + "ForLoop detectado:", ctx.getText())
        self.eventos.append(f"ForLoop: {ctx.getText()}")

    def exitInicializacion(self, ctx:MiGramaticaParser.InicializacionContext):
        print(" " * self.nivell + "Inicialización:", ctx.getText())
        self.eventos.append(f"Inicialización: {ctx.getText()}")

    def exitCondicion(self, ctx:MiGramaticaParser.CondicionContext):
        print(" " * self.nivell + "Condición:", ctx.getText())
        self.eventos.append(f"Condición: {ctx.getText()}")

    def exitActualizacion(self, ctx:MiGramaticaParser.ActualizacionContext):
        print(" " * self.nivell + "Actualización:", ctx.getText())
        self.eventos.append(f"Actualización: {ctx.getText()}")

    def exitAssign(self, ctx:MiGramaticaParser.AssignContext):
        print(" " * self.nivell + "Asignación:", ctx.getText())
        self.eventos.append(f"Asignación: {ctx.getText()}")

    def get_eventos(self):
        return self.eventos