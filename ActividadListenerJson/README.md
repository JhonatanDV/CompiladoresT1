# Actividad 2: Conversión de JSON a XML usando ANTLR4 y Python

Este proyecto desarrolla una solución para transformar archivos en formato JSON a XML utilizando ANTLR4 y Python. Se define una gramática JSON.g4 que permite analizar estructuras complejas del JSON, y mediante un Listener personalizado, se recorre el árbol sintáctico para generar una representación equivalente en XML.

##  Objetivo

Analizar archivos .json utilizando ANTLR y exportar su contenido estructurado como etiquetas XML anidadas, preservando la jerarquía y claves del archivo original.

## Herramientas y comandos utilizados
- *ANTLR4*: Generador de analizadores léxicos y sintácticos.
- *Python 3*

##  Comandos utilizados

```bash
pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 JSON.g4
python json_to_xml.py entrada.json
cat salida.xml

Jhonatan Díaz y Natalia Cabrera