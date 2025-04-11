# Actividad 1: Extender funcionalidad para archivos CSV

Este proyecto tiene como objetivo transformar datos desde un archivo .csv utilizando ANTLR y Python, aplicando un Listener personalizado para generar una salida estructurada en formato JSON. Esta actividad se centra en aplicar reglas de limpieza de datos y estadísticas simples sobre los montos procesados.

##  Objetivo

Utilizar ANTLR4 con Python para interpretar un archivo CSV, limpiar campos numéricos, organizar los datos en una estructura válida y exportarlos a un archivo JSON.

##  Gramática utilizada

Se usó una gramática CSV.g4 para definir cómo interpretar cada línea del archivo .csv, separando campos y permitiendo trabajar fila por fila usando un Listener generado automáticamente.

##  Comandos utilizados

```bash
pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 CSV.g4
python main.py
cat salida.json

Jhonatan Díaz y Natalia Cabrera