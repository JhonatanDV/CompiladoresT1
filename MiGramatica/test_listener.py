from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

def main():
    print("Ingrese su código (pulse Ctrl+D o Ctrl+Z cuando termine):")
    input_stream = InputStream(input())
    
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)
    tree = parser.programa()

    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, tree)

    print("\nEventos detectados:")
    for evento in listener.get_eventos():
        print(evento)

if __name__ == '__main__':
    main()