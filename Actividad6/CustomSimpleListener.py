from SimpleListener import SimpleListener

class CustomSimpleListener(SimpleListener):
    def enterClassDef(self, ctx):
        print(f"Clase encontrada: {ctx.ID().getText()}")
    
    def enterMember(self, ctx):
        if ctx.getChildCount() > 3:  # Es un método
            print(f"Método encontrado: {ctx.ID(0).getText()}")
    
    def enterStat(self, ctx):
        if ctx.getChildCount() > 2:  # Es una asignación
            print(f"Asignación encontrada: {ctx.ID().getText()} = ...")