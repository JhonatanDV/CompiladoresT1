from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from SimpleListener import SimpleListener

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

class CustomSimpleListener(SimpleListener):
    def enterClassDef(self, ctx):
        print(f"Clase encontrada: {ctx.ID().getText()}")
    
    def enterMember(self, ctx):
        if ctx.getChildCount() > 3:  # Es un método
            print(f"Método encontrado: {ctx.ID(0).getText()}")
    
    def enterStat(self, ctx):
        if ctx.getChildCount() > 2:  # Es una asignación
            print(f"Asignación encontrada: {ctx.ID().getText()} = ...")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)
    
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())
    
    try:
        tree = parser.prog()
        print("✅ Entrada válida.")
        
        # Añadir y ejecutar el listener
        listener = CustomSimpleListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("class A { int x; }")
    
    print("\n=== Entrada con error 1 ===")
    parse_input("class B { int f(x) { a = 3 4 5; } }")
    
    print("\n=== Entrada con error 2 ===")
    parse_input("class C { int f(x) { a = 3 + 5; } }")
    
    # Entrada adicional para probar expresiones aritméticas
    print("\n=== Entrada con expresiones aritméticas ===")
    parse_input("class D { int f(x) { a = 3 + 5 * 2; } }")