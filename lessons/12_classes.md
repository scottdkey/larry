# Lesson 12: Classes

> **ES:** Lección 12: Clases

Goals: bundle data and behavior in a class, control attribute access with
properties, make objects feel built-in with dunder methods, and choose between
inheritance and composition.

> **ES:** Objetivos: agrupar datos y comportamiento en una clase, controlar el
> acceso a los atributos con properties, hacer que los objetos se sientan
> nativos con métodos dunder, y elegir entre herencia y composición.

## A first class

> **ES:** ## Una primera clase

```python
class Counter:
    def __init__(self, start: int = 0) -> None:
        self._value = start  # instance attribute

    def increment(self) -> None:
        self._value += 1


c = Counter()
c.increment()
print(c._value)  # 1
```

- `__init__` runs when you call `Counter(...)`; it sets up the new object.
- `self` is the object the method was called on. Python passes it for you.
- A leading underscore (`_value`) is a convention meaning "internal, please
  don't touch". Python does not enforce it.

> **ES:**
> - `__init__` se ejecuta cuando llamas a `Counter(...)`; configura el objeto
>   nuevo.
> - `self` es el objeto sobre el cual se llamó el método. Python lo pasa por ti.
> - Un guion bajo al inicio (`_value`) es una convención que significa
>   "interno, por favor no lo toques". Python no lo impone.

## Properties

> **ES:** ## Properties (propiedades)

A property looks like an attribute but runs code. Use it for read-only values
or to validate/convert on assignment.

> **ES:** Una property parece un atributo pero ejecuta código. Úsala para
> valores de solo lectura o para validar/convertir al asignar.

```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self._celsius = (value - 32) * 5 / 9


t = Temperature(100)
print(t.fahrenheit)  # 212.0, no parentheses
t.fahrenheit = 32
```

A property with no setter is read-only: assigning raises `AttributeError`.

> **ES:** Una property sin setter es de solo lectura: asignarle un valor lanza
> `AttributeError`.

## Dunder methods

> **ES:** ## Métodos dunder

"Dunder" means double underscore. They let your class plug into Python syntax.

> **ES:** "Dunder" significa doble guion bajo (double underscore). Permiten que
> tu clase se integre con la sintaxis de Python.

| Method       | Used by              |
|--------------|----------------------|
| `__repr__`   | `repr(x)`, debugging output |
| `__eq__`     | `a == b`             |
| `__add__`    | `a + b`              |
| `__abs__`    | `abs(a)`             |
| `__bool__`   | `if a:`              |
| `__len__`    | `len(a)`             |

> **ES:** Tabla: `__repr__` lo usa `repr(x)` y la salida de depuración; `__eq__`
> lo usa `a == b`; `__add__` lo usa `a + b`; `__abs__` lo usa `abs(a)`;
> `__bool__` lo usa `if a:`; `__len__` lo usa `len(a)`.

```python
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)


print(Vector(1, 2) + Vector(3, 4))  # Vector(4, 6)
```

In `__eq__`, return `NotImplemented` (not `False`) when `other` is a type you
don't understand; Python then tries the other side and falls back to `False`.

> **ES:** En `__eq__`, devuelve `NotImplemented` (no `False`) cuando `other` es
> un tipo que no entiendes; Python entonces prueba el otro lado y, si tampoco
> funciona, recurre a `False`.

## Inheritance

> **ES:** ## Herencia

A subclass reuses and overrides a parent's behavior.

> **ES:** Una subclase reutiliza y sobrescribe el comportamiento de su clase
> padre.

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def sound(self) -> str:
        raise NotImplementedError

    def speak(self) -> str:
        return f"{self.name} says {self.sound()}"


class Dog(Animal):
    def sound(self) -> str:
        return "woof"


class Puppy(Dog):
    def sound(self) -> str:
        return "yip"

    def speak(self) -> str:
        return super().speak() + "!"  # extend, don't copy
```

`super()` calls the parent's version. `isinstance(Puppy("x"), Animal)` is
`True`.

> **ES:** `super()` llama a la versión de la clase padre.
> `isinstance(Puppy("x"), Animal)` es `True`.

## Composition

> **ES:** ## Composición

Inheritance says "is a". Composition says "has a": store another object in an
attribute and delegate to it.

> **ES:** La herencia dice "es un". La composición dice "tiene un": guarda otro
> objeto en un atributo y delégale el trabajo.

```python
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower


class Car:
    def __init__(self, name: str, engine: Engine) -> None:
        self.engine = engine
```

A `Car` is not an `Engine`, so it should not inherit from one. Prefer
composition by default; reach for inheritance only for a real "is a"
relationship, and keep hierarchies shallow.

> **ES:** Un `Car` no es un `Engine`, así que no debería heredar de uno. Prefiere
> la composición por defecto; usa herencia solo para una relación real de "es
> un", y mantén las jerarquías poco profundas.

## Gotchas

> **ES:** ## Trampas comunes

- Forgetting `self` as the first parameter gives a confusing "takes 1
  positional argument but 2 were given" error.
- Attributes defined at class level (outside methods) are shared by all
  instances. Mutable ones (lists, dicts) cause surprising bugs; create them in
  `__init__`.
- Defining `__eq__` without `__hash__` makes instances unhashable (not usable
  in sets or as dict keys).
- Don't overuse classes: a plain function is often enough.

> **ES:**
> - Olvidar `self` como primer parámetro produce un error confuso: "takes 1
>   positional argument but 2 were given".
> - Los atributos definidos a nivel de clase (fuera de los métodos) son
>   compartidos por todas las instancias. Los mutables (lists, dicts) causan
>   errores sorprendentes; créalos en `__init__`.
> - Definir `__eq__` sin `__hash__` hace que las instancias no sean hashables
>   (no se pueden usar en sets ni como claves de dict).
> - No abuses de las clases: a menudo basta con una función simple.

## Exercises

> **ES:** ## Ejercicios

Files:

- Stubs: `exercises/12_classes/classes.py`
- Tests: `exercises/12_classes/test_classes.py`

> **ES:** Archivos: los stubs y los tests indicados arriba.

Implement `Counter`, `Temperature`, `Vector`, `Animal`/`Dog`/`Puppy`, and
`Engine`/`Car`. Run:

> **ES:** Implementa `Counter`, `Temperature`, `Vector`, `Animal`/`Dog`/`Puppy`
> y `Engine`/`Car`. Ejecuta:

```
uv run pytest exercises/12_classes
```
