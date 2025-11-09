class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")