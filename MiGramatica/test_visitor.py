from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

def main():
    print("Ingrese su código (pulse Ctrl+D o Ctrl+Z cuando termine):")
    input_stream = InputStream(input())
    
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)
    tree = parser.programa()

    visitor = EvalVisitor()
    resultado = visitor.visit(tree)

    print("\nEstado final de variables:")
    for var, valor in resultado.items():
        print(f"{var} = {valor}")

if __name__ == '__main__':
    main()