# WORLD OF AGENTS

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
