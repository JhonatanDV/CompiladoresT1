from CSVListener import CSVListener
from CSVParser import CSVParser
from collections import defaultdict, Counter
import json
import re

class CSVLoader(CSVListener):
    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []
        self.emptyFieldCount = 0

        self.mes_counter = Counter()
        self.filas_repetidas = []
        self.filas_vistas = set()
        self.cantidad_mal_formateada = []
        self.totales_por_mes = defaultdict(float)

    def enterRow(self, ctx):
        self.currentRowFieldValues = []

    def exitText(self, ctx):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx):
        self.currentRowFieldValues.append(ctx.getText())

    def exitEmpty(self, ctx):
        self.currentRowFieldValues.append("")
        self.emptyFieldCount += 1

    def exitRow(self, ctx):
        # Si es header
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            self.header = self.currentRowFieldValues
            return

        # Validar longitud
        if len(self.currentRowFieldValues) != len(self.header):
            print(f" Fila inválida: {self.currentRowFieldValues}")
            return

        fila = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i] if i < len(self.header) else f"col_{i}"
            fila[key] = val

        # Filas duplicadas
        clave_fila = tuple(fila.items())
        if clave_fila in self.filas_vistas:
            self.filas_repetidas.append(fila)
        else:
            self.filas_vistas.add(clave_fila)

        # Contar por mes
        if "Mes" in fila:
            self.mes_counter[fila["Mes"]] += 1

        # Verificar cantidad
        if "Cantidad" in fila:
            monto = fila["Cantidad"].replace('"', '').replace('$','').replace(',', '').strip()
            if not monto or not re.match(r'^-?\d+(\.\d+)?$', monto):
                self.cantidad_mal_formateada.append(fila)
            else:
                try:
                    valor = float(monto)
                    self.totales_por_mes[fila["Mes"]] += valor
                    fila["Cantidad"] = str(valor)
                except:
                    self.cantidad_mal_formateada.append(fila)

        self.rows.append(fila)

    def print_column_stats(self, column_name="Cantidad"):
        print(f"\n Estadísticas para columna '{column_name}':")
        for fila in self.rows:
            if column_name in fila:
                print(f"• {fila[column_name]}")

    def exportar_a_json(self, filename="salida.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)
