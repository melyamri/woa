# WORLD OF AGENTS

## Cambios del 22 y 23 de abril
### Añadido sistema de reglas y estructura correcta
  - Ahora las tareas son independientes de los agentes y tienen su propio manager
  - Los objetivos son objetivos simples y no están mezclados con las tareas
  - Se ha creado un sistema de reglas básico y eficiente
  - Se ha mejorado el estilo visual y se ha incluido un log de las tareas que se van ejecutando
  - Ahora los agentes son capaces de razonar
  - Se han descartado los siguientes sistemas de reglas:
    - *Intellect (Versión necesaria Python 2.7)*
    - *Pyke (No válido para el funcionamiento esperado)*
    - *durable_rules (Necesita permisos de super usuario y base de datos REDIS, además necesita que se escriba en esa base de datos para leer los objetos)*


## Cambios del 15 de abril
### Añadido sistema de objetivos para los agentes
  - Ahora los agentes tienen un array de objetivos
  - En cada paso ejecutarán los objetivos asociados al agentes
  - Cada objetivo puede ser para un tipo determinado de agente

### Meroras en el sistema
- Mejorada jerarquía de clases
- Mejorada la función de extensión de los recursos

_____

## Cambios significativos
- Añadida separación de clases
- Añadidos métodos de dibujo en cada uno de los agentes
- Añadida generación aleatoria de recursos
- Añadida posibilidad de que los agentes árbol se extiendan
- Añadida posibilidad de cortar el árbol al recoger la madera
- Añadidas diferentes formas para los agentes
- Ahora los agentes recolectores se vuelven rojos cuando tienen 10 de madera


## Setup (opcional)

```
virtualenv -p python3 venv
```

## Run

```
source venv/bin/activate #sólo con virtualenv
pip install -r requirements.txt
```

## Freeze Requirements (Only to save new installed packages with pip)
```
pip freeze > requirements.txt
```
