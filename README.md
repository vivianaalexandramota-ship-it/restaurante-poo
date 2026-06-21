# Sistema básico de gestión de restaurante

**Estudiante:** Geovanny José Velasco Paredes  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 4

## Descripción del sistema

Este proyecto presenta un sistema básico de gestión de restaurante desarrollado en Python aplicando Programación Orientada a Objetos. El sistema permite registrar productos y clientes, además de mostrar la información organizada en consola.

El objetivo principal no es crear un programa complejo, sino demostrar el uso de clases, objetos, constructores, atributos, métodos, método especial `__str__()`, importaciones y organización modular del código.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
README.md
```

## Explicación de los archivos

- `modelos/producto.py`: contiene la clase `Producto`, que representa un plato, bebida o producto del restaurante.
- `modelos/cliente.py`: contiene la clase `Cliente`, que representa a una persona registrada en el restaurante.
- `servicios/restaurante.py`: contiene la clase `Restaurante`, encargada de gestionar los productos y clientes.
- `main.py`: es el punto de arranque del programa. Aquí se crean los objetos y se ejecutan los métodos para demostrar el funcionamiento del sistema.

## Conceptos aplicados

- Clases y objetos.
- Constructores `__init__()`.
- Atributos y métodos.
- Método especial `__str__()`.
- Importaciones entre archivos.
- Separación de responsabilidades.
- Organización modular del proyecto.

## Cómo ejecutar el programa

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Entrar a la carpeta `restaurante_app`.
3. Ejecutar el archivo principal:

```bash
python main.py
```

## Reflexión

La modularización es importante porque permite organizar mejor el código y separar las responsabilidades de cada archivo. En este proyecto, los modelos representan las entidades del restaurante, el servicio administra las operaciones principales y el archivo `main.py` coordina la ejecución. Esta forma de trabajo ayuda a que el programa sea más claro, ordenado y fácil de modificar.
