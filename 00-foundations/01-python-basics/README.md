
# Python Basics

## Español

### Propósito

Esta sección presenta los fundamentos de Python necesarios para comenzar a
trabajar con datos y construir scripts mantenibles. Los ejemplos son pequeños,
ejecutables y progresivos: empiezan con la sintaxis del lenguaje y avanzan
hacia lectura y escritura de archivos, configuración, logging y transformación
de registros.

### Contenido trabajado

- Variables, tipos básicos, operadores, mutabilidad y conversiones.
- Funciones, argumentos, valores de retorno, `lambda`, `map` y `filter`.
- Anotaciones de tipos, aliases, `Literal`, valores opcionales y estructuras
	tipadas.
- Control de flujo: decisiones, bucles, `break`, `continue`, `range`,
	`enumerate`, `zip` y `match/case`.
- Colecciones: listas, tuplas, diccionarios, sets, slicing, métodos y
	estructuras anidadas.
- Comprensiones de listas, diccionarios y sets, además de expresiones
	generadoras.
- Iterables, iteradores, `iter()`, `next()`, `yield`, evaluación perezosa y
	procesamiento registro por registro.
- Strings: slicing, parsing, normalización y construcción de texto con
	f-strings.
- Fechas, horas, ISO 8601, zonas horarias y conversiones.
- Excepciones recuperables, validación y errores de dominio.
- `dataclasses` para representar entidades y validar sus datos.
- Archivos JSON y CSV, incluyendo headers, encoding, conversión de tipos,
	campos faltantes y procesamiento incremental.
- Variables de entorno, defaults, validación, configuración y `.env` de forma
	conceptual.
- Logging con niveles, handlers, formatters, timestamps y tracebacks.
- Módulos, imports y utilidades de la biblioteca estándar como `math` y
	`statistics`.
- `pathlib` para navegar, leer, escribir y limpiar archivos y directorios.

### Requisitos

- Python 3.10 o superior. `match/case` y varias anotaciones modernas de tipos
	requieren esta versión mínima.
- No se necesitan dependencias externas: los ejemplos usan la biblioteca
	estándar de Python.

### Cómo ejecutar los scripts

Desde la raíz del repositorio, en PowerShell:

```powershell
python .\00-foundations\01-python-basics\scripts\variables.py
python .\00-foundations\01-python-basics\scripts\control_flow.py
python .\00-foundations\01-python-basics\scripts\csv_example.py
```

Desde macOS, Linux o Git Bash:

```bash
python3 00-foundations/01-python-basics/scripts/variables.py
python3 00-foundations/01-python-basics/scripts/control_flow.py
python3 00-foundations/01-python-basics/scripts/csv_example.py
```

También se puede entrar en esta carpeta y ejecutar cualquier archivo:

```powershell
cd .\00-foundations\01-python-basics
python .\scripts\strings.py
```

Cada script tiene un bloque `if __name__ == "__main__":`, por lo que puede
ejecutarse de forma independiente. Los scripts que crean archivos de prueba
usan recursos temporales o limpian lo generado al finalizar. Los archivos
compartidos de ejemplo están en [`src/`](src/), incluyendo `info.json` y
`random-csv.csv`.

### Descripción de los scripts

| Script | Qué explica |
| --- | --- |
| `variables.py` | Variables, tipos, operadores, conversiones, mutabilidad e inspección de tipos. |
| `control_flow.py` | Decisiones, bucles, `break`, `continue`, `range`, `enumerate`, `zip` y `match/case`. |
| `collections.py` | `list`, `tuple`, `dict`, `set`, indexing, slicing, métodos y estructuras anidadas. |
| `comprehensions.py` | Comprensiones, filtros, transformaciones, generadores y ejemplos con datos. |
| `strings.py` | Métodos de strings, parsing y normalización de una línea de pedido. |
| `functions.py` | Funciones, argumentos, `lambda`, `map`, `filter`, ordenamiento y cálculos. |
| `type_hints.py` | Anotaciones, aliases, `Literal`, tipos opcionales y datos tipados. |
| `generators.py` | Iterables, iteradores, `iter`, `next`, `yield`, expresiones generadoras y lazy evaluation. |
| `csv_example.py` | Lectura y escritura CSV, headers, encoding UTF-8, delimitadores, conversión y filas faltantes. |
| `json_example.py` | Lectura y escritura JSON, validación, dataclasses, fechas ISO y estructuras anidadas. |
| `environment.py` | `os.environ`, `os.getenv`, defaults, variables requeridas, validación y configuración separada. |
| `logging_example.py` | Logger, niveles, handler, formatter, timestamps y logging de excepciones. |
| `exceptions.py` | Manejo de excepciones, validación y errores personalizados de dominio. |
| `dataclasses_test.py` | Entidades mutables e inmutables, defaults, validación y serialización con dataclasses. |
| `datetime_test.py` | Fechas, horas, zonas horarias, ISO 8601, intervalos y operaciones temporales. |
| `pathlib_test.py` | Rutas, globbing, lectura y escritura de archivos, directorios anidados y limpieza. |
| `modules.py` | Imports, módulos de la biblioteca estándar y el paquete local `data_tools`. |

### Conclusiones

Estos ejemplos forman una base práctica para escribir scripts de datos claros,
validables y fáciles de ejecutar. La progresión importante es pasar de valores
simples a estructuras, de estructuras a archivos y de archivos a procesos que
validan, registran y transforman datos. Los siguientes pasos naturales son
tests automatizados, un CLI de validación y una estructura de proyecto lista
para producción.

## English

### Purpose

This section introduces the Python fundamentals needed to start working with
data and building maintainable scripts. The examples are small, executable,
and progressive: they begin with language syntax and move toward file I/O,
configuration, logging, and record transformation.

### Topics covered

- Variables, basic types, operators, mutability, and conversions.
- Functions, arguments, return values, `lambda`, `map`, and `filter`.
- Type annotations, aliases, `Literal`, optional values, and typed structures.
- Control flow: decisions, loops, `break`, `continue`, `range`, `enumerate`,
	`zip`, and `match/case`.
- Collections: lists, tuples, dictionaries, sets, slicing, methods, and nested
	structures.
- List, dictionary, and set comprehensions, plus generator expressions.
- Iterables, iterators, `iter()`, `next()`, `yield`, lazy evaluation, and
	record-by-record processing.
- Strings: slicing, parsing, normalization, and f-string formatting.
- Dates, times, ISO 8601, time zones, and conversions.
- Recoverable exceptions, validation, and domain errors.
- `dataclasses` for representing entities and validating their data.
- JSON and CSV files, including headers, encoding, type conversion, missing
	fields, and incremental processing.
- Environment variables, defaults, validation, configuration, and the `.env`
	concept.
- Logging with levels, handlers, formatters, timestamps, and tracebacks.
- Modules, imports, and standard-library utilities such as `math` and
	`statistics`.
- `pathlib` for navigating, reading, writing, and cleaning files and folders.

### Requirements

- Python 3.10 or newer. `match/case` and several modern type annotations
	require this minimum version.
- No external dependencies are required; the examples use Python's standard
	library.

### Running the scripts

From the repository root in PowerShell:

```powershell
python .\00-foundations\01-python-basics\scripts\variables.py
python .\00-foundations\01-python-basics\scripts\control_flow.py
python .\00-foundations\01-python-basics\scripts\csv_example.py
```

From macOS, Linux, or Git Bash:

```bash
python3 00-foundations/01-python-basics/scripts/variables.py
python3 00-foundations/01-python-basics/scripts/control_flow.py
python3 00-foundations/01-python-basics/scripts/csv_example.py
```

You can also enter this folder and run any file:

```powershell
cd .\00-foundations\01-python-basics
python .\scripts\strings.py
```

Every script has an `if __name__ == "__main__":` block and can therefore be
run independently. Scripts that create test files use temporary resources or
clean up generated files when they finish. Shared example files are stored in
[`src/`](src/), including `info.json` and `random-csv.csv`.

### Script overview

| Script | What it explains |
| --- | --- |
| `variables.py` | Variables, types, operators, conversions, mutability, and type inspection. |
| `control_flow.py` | Decisions, loops, `break`, `continue`, `range`, `enumerate`, `zip`, and `match/case`. |
| `collections.py` | `list`, `tuple`, `dict`, `set`, indexing, slicing, methods, and nested structures. |
| `comprehensions.py` | Comprehensions, filtering, transformations, generators, and data examples. |
| `strings.py` | String methods, parsing, and normalization of an order line. |
| `functions.py` | Functions, arguments, `lambda`, `map`, `filter`, sorting, and calculations. |
| `type_hints.py` | Annotations, aliases, `Literal`, optional types, and typed data. |
| `generators.py` | Iterables, iterators, `iter`, `next`, `yield`, generator expressions, and lazy evaluation. |
| `csv_example.py` | CSV reading and writing, headers, UTF-8 encoding, delimiters, conversion, and missing fields. |
| `json_example.py` | JSON I/O, validation, dataclasses, ISO dates, and nested structures. |
| `environment.py` | `os.environ`, `os.getenv`, defaults, required variables, validation, and separated configuration. |
| `logging_example.py` | Loggers, levels, handlers, formatters, timestamps, and exception logging. |
| `exceptions.py` | Exception handling, validation, and custom domain errors. |
| `dataclasses_test.py` | Mutable and immutable entities, defaults, validation, and dataclass serialization. |
| `datetime_test.py` | Dates, times, time zones, ISO 8601, intervals, and time operations. |
| `pathlib_test.py` | Paths, globbing, file I/O, nested directories, and cleanup. |
| `modules.py` | Imports, standard-library modules, and the local `data_tools` package. |

### Conclusions

These examples provide a practical foundation for writing clear, testable, and
easy-to-run data scripts. The key progression is from simple values to
structures, from structures to files, and from files to processes that validate,
log, and transform data. Natural next steps are automated tests, a validation
CLI, and a production-ready project structure.
