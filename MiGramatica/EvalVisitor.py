from antlr4 import *
from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.memoria = {}

    def visitPrograma(self, ctx:MiGramaticaParser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.memoria

    def visitForLoop(self, ctx:MiGramaticaParser.ForLoopContext):
        # Inicializar variable de loop
        self.visit(ctx.inicializacion())
        
        # Variable de loop
        var_loop = ctx.inicializacion().ID().getText()
        
        # Ejecutar mientras la condición sea verdadera
        while self.visit(ctx.condicion()):
            # Ejecutar sentencias del cuerpo
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
            
            # Actualizar variable de loop
            self.visit(ctx.actualizacion())

        return None

    def visitAssign(self, ctx:MiGramaticaParser.AssignContext):
        var_name = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memoria[var_name] = valor
        return valor

    def visitCondicion(self, ctx:MiGramaticaParser.CondicionContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.relacional().getText()

        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitAddSub(self, ctx:MiGramaticaParser.AddSubContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        
        if ctx.op.text == '+':
            return left + right
        else:  # '-'
            return left - right

    def visitMulDiv(self, ctx:MiGramaticaParser.MulDivContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        
        if ctx.op.text == '*':
            return left * right
        else:  # '/'
            return left / right

    def visitInt(self, ctx:MiGramaticaParser.IntContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx:MiGramaticaParser.VariableContext):
        var_name = ctx.ID().getText()
        return self.memoria.get(var_name, 0)