grammar MiGramatica;

// Regla principal
programa: (sentencia ';')+ EOF;

// Tipos de sentencias
sentencia 
    : forLoop 
    | assign
    ;

// Estructura de for loop más detallada
forLoop 
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' sentencia+ '}' 
    ;

// Inicialización de variable
inicializacion 
    : ID '=' expresion 
    ;

// Condición con operadores relacionales
condicion 
    : expresion relacional expresion 
    ;

// Actualización de variable
actualizacion 
    : ID '=' expresion 
    ;

// Asignación de variable
assign 
    : ID '=' expresion 
    ;

// Expresiones con diferentes niveles de precedencia
expresion 
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Operadores relacionales
relacional 
    : '<' | '>' | '<=' | '>=' | '==' | '!=' 
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;