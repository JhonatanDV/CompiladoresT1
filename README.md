# CompiladoresT1
# Análisis de Ciclo For con ANTLR4 y Python

## Requisitos Previos
- Python 3.x
- Java (para ANTLR4)
- pip (gestor de paquetes de Python)

## Configuración del Entorno

### 1. Instalación de Dependencias
```bash
# Instalar antlr4-python3-runtime
pip install antlr4-python3-runtime
```

### 2. Generar Archivos del Parser
```bash
# Genera los archivos de lexer, parser, listener y visitor
antlr4 -Dlanguage=Python3 -visitor -listener MiGramatica.g4
```

## Estructura del Proyecto
```
/proyecto
├── MiGramatica.g4        # Archivo de gramática
├── MyListener.py         # Implementación del Listener
├── EvalVisitor.py        # Implementación del Visitor
├── test_listener.py      # Pruebas para Listener
├── test_visitor.py       # Pruebas para Visitor
└── README.md             # Este archivo
```

## Ejecución de Pruebas

### Ejecutar Listener
```bash
python3 test_listener.py
```

### Ejecutar Visitor
```bash
python3 test_visitor.py
```

## Ejemplos de Entrada
Puedes probar el código con ejemplos como:
```
for (i = 0; i < 3; i = i + 1) {
    x = x + 2;
};

for (contador = 10; contador > 0; contador = contador - 1) {
    resultado = contador * 2;
};
```

## Solución de Problemas

### Error de Importación
Si encuentras errores de importación, asegúrate de:
1. Estar en el directorio correcto
2. Haber generado los archivos del parser
3. Tener instalada la librería `antlr4-python3-runtime`

### Permisos
Si encuentras problemas de permisos:
```bash
# En sistemas Unix/Linux
chmod +x test_listener.py
chmod +x test_visitor.py
```

## Comandos Útiles

### Limpiar Archivos Generados
```bash
# Eliminar archivos generados por ANTLR4
rm MiGramaticaLexer.py
rm MiGramaticaParser.py
rm MiGramaticaListener.py
rm MiGramaticaVisitor.py
```

### Regenerar Archivos del Parser
```bash
# Borrar archivos antiguos y regenerar
rm MiGramatica*.py
antlr4 -Dlanguage=Python3 -visitor -listener MiGramatica.g4
```

## Notas Adicionales
- Asegúrate de tener Java instalado para ejecutar ANTLR4
- La versión de ANTLR4 debe ser compatible con Python 3
- Consulta la documentación oficial de ANTLR4 para más detalles

## Licencia
[Especificar la licencia del proyecto]
```

Este README proporciona:
- Instrucciones de instalación
- Estructura del proyecto
- Comandos para ejecutar y probar
- Solución de problemas comunes
- Comandos útiles para mantenimiento
