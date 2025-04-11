import sys
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVLoader import CSVLoader

def main(input_file):
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = CSVLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # No necesitas llamar estas si ya se ejecutan dentro del listener
    # loader.limpiar_montos()
    # loader.contar_por_mes()
    # loader.detectar_repetidas()
    # loader.validar_cantidades()

    loader.exportar_a_json("salida.json")

    print(f"\n Total de campos vacíos: {loader.emptyFieldCount}")

    print("\n Meses que se encontraron:")
    for mes, count in loader.mes_counter.items():
        print(f"{mes}: {count} veces")

    print("\n Filas que se repiten:")
    for fila in loader.filas_repetidas:
        print(fila)

    print("\n Cantidad mal formateada o vacía:")
    for fila in loader.cantidad_mal_formateada:
        print(fila)

    print("\n Total por cada mes:")
    for mes, total in loader.totales_por_mes.items():
        print(f"{mes}: ${total:.2f}")

if __name__ == '__main__':
    main("datos.csv")
