# Python Modules Cheatsheet

## Module

A module is a single `.py` file.

```python
# calculator.py

def add(a, b):
    return a + b
```

## Import full module

```python
import math
print(math.sqrt(25))
```

## Import with alias

```python
import statistics as stats
print(stats.mean([80, 90, 70]))
```

## Import specific function

```python
from math import sqrt
print(sqrt(25))
```

## Avoid wildcard import

```python
from math import *
```

This is usually avoided because it hides where names come from.

## Package

A package is a folder that contains modules.

```text
student_toolkit/
├── __init__.py
├── cli.py
└── services/
    ├── __init__.py
    └── grade_service.py
```

## `__name__ == "__main__"`

```python
def run_app():
    print("Running app")

if __name__ == "__main__":
    run_app()
```

This prevents app code from running automatically when imported.

## `sys.path`

```python
import sys
for path in sys.path:
    print(path)
```

Python uses this list to find modules.

## `sys.modules`

```python
import sys
import math
print("math" in sys.modules)
```

Python uses this as an import cache.

## Common errors

| Error | Meaning | Fix |
|---|---|---|
| `ModuleNotFoundError` | Python cannot find module | Check spelling and path |
| `ImportError` | Module found but name missing | Check function/class name |
| Circular import | Modules import each other | Move shared logic to common module |
| Shadowing | Local file has standard module name | Rename local file |
