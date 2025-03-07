# -*- coding: utf-8 -*-
"""untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/MariapazSantamaria/77c05b4c4071fa3a1a24aaa6d102cfeb/untitled5.ipynb
"""

class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años")

    def felicitar(self):
        print(f"¡Felicidades, {self.nombre}! Tienes todas tus vacunas al día y ya estás esterilizad@.")

mi_perro = Perro("Abana", "Criolla", 1)

mi_perro.mostrar_info()

mi_perro.ladrar()

mi_perro.felicitar()