"""
<__main__.PersonajeRaza object at 0x000001AE449B3EB0>
La respuesta que obtienes al imprimir el objeto personaje1 es la representación 
predeterminada de un objeto de clase en Python. Para obtener una representación 
más legible y útil, puedes definir el método especial __str__ en la clase PersonajeRaza 
para personalizar la salida al imprimir el objeto.
"""
import random

# Lista de razas disponibles
razas = ["Humano", "Elfo", "Enano", "Orco", "Goblin", "Hada", "Vampiro", "Lobo", "Dragón"]

# Diccionario para almacenar los personajes creados
listaPersonajes = {}

# Definición de la clase base Personaje
class Personaje:
    def __init__(self, nombre):
        # Inicialización de atributos básicos del personaje
        self.nombre = nombre.capitalize()
        self.nivel = 1
        self.fuerza = 0
        self.destreza = 0
        self.inteligencia = 0
    
    def crear_personaje(self):
        # Método para crear un personaje personalizado
        atributos = ["nivel", "fuerza", "destreza", "inteligencia"]
        for atributo in atributos:
            # Asignar valores a los atributos del personaje
            setattr(self, atributo, int(input(f"{atributo.capitalize()} para personaje del 1-10: ")))
# setattr() función de Python se utiliza para establecer el valor de 
# un atributo de un objeto. Toma tres argumentos: el objeto al que se le desea establecer 
# el atributo, el nombre del atributo y el valor.
    
    def crear_random(self, nuevo_nombre):
        # Método para crear un personaje aleatorio
        self.nombre = nuevo_nombre
        self.nivel = random.randint(1, 10)
        self.fuerza = random.randint(1, 10)
        self.destreza = random.randint(1, 10)
        self.inteligencia = random.randint(1, 10)
    
    def editar_atributos(self, nivel, fuerza, destreza, inteligencia):
        # Método para editar los atributos de un personaje
        self.nivel = nivel
        self.fuerza = fuerza
        self.destreza = destreza
        self.inteligencia = inteligencia
    
    def eliminar_personaje(self):
        # Método para eliminar un personaje
        self.nombre = ""
        self.nivel = 1
        self.fuerza = 0
        self.destreza = 0
        self.inteligencia = 0

# Definición de la clase PersonajeRaza que hereda de Personaje
class PersonajeRaza(Personaje):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def editar_raza(self, nueva_raza):
        # Método para editar la raza de un personaje
        self.raza = nueva_raza
    
    def __str__(self):
        # Método para representar el personaje como una cadena de texto
        return f"Personaje: {self.nombre}, Raza: {self.raza}, Nivel: {self.nivel}, Fuerza: {self.fuerza}, Destreza: {self.destreza}, Inteligencia: {self.inteligencia}"

# Función para mostrar las opciones de raza
def mostrar_razas():
    print("Seleccione una raza:")
    for i, raza in enumerate(razas, 1):
        print(f"{i}. {raza}")

# Función para automatizar la creación de personajes
def automatizarCreacion():
    while True:
        opcion = input("¿Desea crear un personaje aleatorio o personalizado? (a/p): ")
        if opcion.lower() == 'a':
            # Crear personaje aleatorio
            nombre = input("Ingrese el nombre del personaje: ")
            raza = random.choice(razas)
            personaje = PersonajeRaza(nombre, raza)
            personaje.crear_random(nombre.capitalize())
            listaPersonajes[nombre] = personaje
        elif opcion.lower() == 'p':
            # Crear personaje personalizado
            nombre = input("Ingrese el nombre del personaje: ")
            mostrar_razas()
            opcion = int(input("Opción: "))
            while opcion < 1 or opcion > len(razas):
                print("Opción inválida. Intente nuevamente.")
                opcion = int(input("Opción: "))
            raza = razas[opcion - 1]
            personaje = PersonajeRaza(nombre, raza)
            personaje.crear_personaje()
            listaPersonajes[nombre] = personaje
        else:
            print("Opción inválida. Intente nuevamente.")
            continue
        
        opcion = input("¿Desea crear más personajes? (s/n): ")
        if opcion.lower() != 's':
            break

# Ejemplo de uso
automatizarCreacion()

# Imprimir la lista de personajes
for nombre, personaje in listaPersonajes.items():
    print(nombre,personaje)
    # en este ejemplo estamos imprimiendo key - value

"""
Humano
Elfo
Enano
Orco
Goblin
Hada
Vampiro
Lobo humanoide
Elemental de fuego
Dragón
"""


"""
setattr() es una función integrada de Python que se utiliza para establecer el valor de 
un atributo de un objeto. Toma tres argumentos: el objeto al que se le desea establecer 
el atributo, el nombre del atributo y el valor que se desea asignar.

En el código proporcionado, se utiliza setattr() en el método crear_personaje() de la 
clase Personaje. En esta línea de código:

setattr(self, atributo, int(input(f"{atributo.capitalize()} para personaje del 1-10: ")))
self se refiere al objeto de la clase Personaje 

setattr() función de Python se utiliza para establecer el valor de 
un atributo de un objeto. Toma tres argumentos: el objeto al que se le desea establecer 
el atributo, el nombre del atributo y el valor.
"""

"""
__str__() es un método en Python que se utiliza para obtener una representación de cadena 
legible para humanos de un objeto. Es una convención en Python y se invoca cuando se llama 
a la función str() en un objeto.
"""

# __ejemplo
# doble guión bajo hace que sean variables privadas y no se puede acceder desde
# fuera de su contexto