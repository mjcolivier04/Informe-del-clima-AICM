import sys
sys.path.insert(1,'../../proyecto01/programa')
import Proyecto01
import requests
import json

class Test:
	""" 
	pruebas para el proyecto01
	"""
	
	def pruebaPeticiones():
		"""
		método para probar las peticiones al OpenweatherMap
		se hagan de la manera correcta
		"""
		
		diccionarioPrueba={"MEX":["123","456"]}
		assert(Proyecto01.peticiones(diccionarioPrueba)!=200)

	
	def pruebaLecturaCache():
		"""
		método para probar que se lee correctamente el documento y el cache 
		funciona adecuadamente
		"""

		diccionarioPrueba=["49.0128","2.55"]
		assert(Proyecto01.lecturaCache().keys()==diccionarioPrueba)

	def pruebaSalidaClima():
		"""
		método para probar que salidaClima arroja los datos correctos
		"""
		llaveApi="87dd4d6b93bcf3872531c2fecaf51962"
		url="http://api.openweathermap.org/data/2.5/weather?"

		peticionApi=url+"lat=25.7785"+"&"+"lon=-100.107"+"&units=metric&lang=es&appid="+llaveApi

		peticion=requests.get(peticionApi)
		diccionarioPrueba={"MTY":peticion.json()}

		assert("temperatura" in Proyecto01.salidaClima(diccionarioPrueba))
		assert("humedad" in Proyecto01.salidaClima(diccionarioPrueba))
		assert("lugar" in Proyecto01.salidaClima(diccionarioPrueba))
		assert("sensación" in Proyecto01.salidaClima(diccionarioPrueba))

	
