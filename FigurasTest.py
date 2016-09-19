import unittest
from Figuras import Figuras

class testFiguras(unittest.TestCase):

	def setUp(self):
		self.figura = Figuras()

	def test_area_cuadrado_lado_5(self):
		resultado = self.figura.cuadrado(5)
		self.assertEqual(25,resultado)

	def test_area_cuadrado_lado_6(self):
		resultado = self.figura.cuadrado(6)
		self.assertEqual(36,resultado)	

	def test_area_cuadrado_lado_g(self):
		resultado = self.figura.cuadrado('g')
		self.assertEqual('Dato Incorrecto',resultado)	

	def test_area_cuadrado_lado_4punto5(self):
		resultado = self.figura.cuadrado(4.5)
		self.assertEqual(20.25,resultado)	

	def test_area_rectangulo_basealtura_1020(self):
		resultado = self.figura.rectangulo(10,20)
		self.assertEqual(200,resultado)	

	def test_area_rectangulo_basealtura_g(self):
		resultado = self.figura.rectangulo('g','c')
		self.assertEqual("Dato Incorrecto",resultado)

	def test_area_rectangulo_basealtura_flotantes(self):
		resultado = self.figura.rectangulo(4.5,3.6)
		self.assertEqual(16.2,resultado)	

	def test_area_triangulo_basealturasobre2_1020(self):
		resultado = self.figura.triangulo(10,20)
		self.assertEqual(100,resultado)	

	def test_area_triangulo_basealturasobre2_g(self):
		resultado = self.figura.triangulo('g','c')
		self.assertEqual("Dato Incorrecto",resultado)

	def test_area_triangulo_basealturasobre2_flotantes(self):
		resultado = self.figura.triangulo(4.5,3.6)
		self.assertEqual(8.1,resultado)			

	def test_area_circulo_radiopi(self):
		resultado = self.figura.circulo(20)
		self.assertEqual(1260,resultado)				
		
	def test_area_circulo_radiopi_g(self):
		resultado = self.figura.circulo('g')
		self.assertEqual("Dato Incorrecto",resultado)	

	def test_area_circulo_radiopi_flotante(self):
		resultado = self.figura.circulo(10.5)
		self.assertEqual(347.29,resultado)		
			
	def tearDown(self):
	    pass	
    
if __name__ == '__main__':
	unittest.main()

