import math


class Figuras:

    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception, e:
            return 'Dato Incorrecto'

    def rectangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            return base * altura
        except Exception, e:
            return "Dato Incorrecto"

    def triangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            return base * altura / 2
        except Exception, e:
            return "Dato Incorrecto"

    def circulo(self, radio):
        try:
            radio = float(radio)
            return round((3.15) * (math.pow(radio, 2)), 2)
        except Exception, e:
            return "Dato Incorrecto"
