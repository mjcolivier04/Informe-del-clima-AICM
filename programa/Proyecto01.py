import requests
import json
import csv 
from io import open
from dotenv import load_dotenv, find_dotenv

"""
Archivo que se encarga de hacer lo que pide el proyecto 1
"""	
def peticiones(diccionario):

	"""
	Método para las peticiones
	"""	
	diccionarioClima={} 
	print("Ingresa tu clave de la API")
	llaveApi = input()
	url="http://api.openweathermap.org/data/2.5/weather?"


	for clave in diccionario.keys():
			
		peticionApi=url+"lat="+diccionario[clave][0]+"&"+"lon="+diccionario[clave][1]+"&units=metric&lang=es&appid="+llaveApi

		peticion=requests.get(peticionApi)
			
		if peticion.status_code!=404:
			diccionarioClima[clave]=peticion.json() 
				

	return diccionarioClima


	
def lecturaCache():
	"""
	Método para leer el csv para almacenar los datos en un diccionario(cache) el cual 
	se podra consultar
	"""
	cache={}

	documento = csv.DictReader(open("entrada/dataset1.csv"))
	
	for row in documento:
			
		origenCoordenadas=[row["origin_latitude"],row["origin_longitude"]]
		ciudadOrigen=row["origin"]

			
		destinoCoordenadas=[row["destination_latitude"],row["destination_longitude"]]
		ciudadDestino=row["destination"]

			
		cache[ciudadOrigen]=origenCoordenadas
		cache[ciudadDestino]=destinoCoordenadas

	
	return cache

		
def salidaClima(peticiones):
	"""
	Método que mostrara los datos del clima de la ciudad dada con su iata
	la información la consultara con lo guardado en el diccionario de
	peticiones
	"""
	for iata in peticiones.keys():	
		datosDelClima=peticiones[iata]

		temperatura=str(datosDelClima["main"]["temp"])
		humedad=str(datosDelClima["main"]["humidity"])
		sensacion=str(datosDelClima["main"]["feels_like"])
		presion=str(datosDelClima["main"]["pressure"])
		
		datoTemperatura=iata+"\n lugar: "+datosDelClima["name"]+"\n temperatura: "+temperatura
		datoHumedad="\n humedad: "+humedad+"\n descripcion: "+datosDelClima["weather"][0]["description"]
		datoSensacion="\n con sensación de: "+sensacion+"\n presion: "+presion
		informacion=datoTemperatura+datoHumedad+datoSensacion
		
		print(informacion)
			
	return informacion

def main():
	"""
	Ejecuta el proyecto completo
	"""

	salidaClima(peticiones(lecturaCache()))
	
if __name__=="__main__":

	main()
