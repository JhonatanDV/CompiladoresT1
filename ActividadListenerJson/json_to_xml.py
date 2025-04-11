from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONListener import JSONListener

class XMLEmitter(JSONListener):
    def __init__(self):
        self.xml_map = {}
        self.indent_level = 0

    def getXML(self, ctx):
        return self.xml_map.get(ctx, '')

    def setXML(self, ctx, value):
        self.xml_map[ctx] = value

    def indent(self):
        return '  ' * self.indent_level

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.jsonObject()))

    def exitPair(self, ctx):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        ind = self.indent()
        xml = f"{ind}<{tag}>\n{val}\n{ind}</{tag}>\n"
        self.setXML(ctx, xml)

    def exitAnObject(self, ctx):
        self.indent_level += 1
        xml = ''.join(self.getXML(p) for p in ctx.pair())
        self.indent_level -= 1
        self.setXML(ctx, xml)

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, '')

    def exitArrayOfValues(self, ctx):
        self.indent_level += 1
        body = ''.join(f"{self.indent()}<element>{self.getXML(v)}</element>\n" for v in ctx.value())
        self.indent_level -= 1
        self.setXML(ctx, body)

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, '')

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "entrada.json"

    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = JSONLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()

    emitter = XMLEmitter()
    walker = ParseTreeWalker()
    walker.walk(emitter, tree)

    salida = emitter.getXML(tree)
    print("\nResultado XML:\n")
    print(salida)

    with open("salida.xml", "w", encoding="utf-8") as f:
        f.write(salida)
    print("\n XML exportado a salida.xml")
