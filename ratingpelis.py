# EXTRAE DE UN ARCHIVO CSV UNA LISTA DE PELICULAS
# QUE LAS BUSCA EN LA BASE DE DATOS DE IMDB
# CREANDO UNA LISTA CON SUS RESPECTIVAS CALIFICACIONES (MAXIMA CALIFICACION ES DE 10)

import imdb
import csv

ia = imdb.IMDb()

with open('peliculas.csv') as listacsv:
	reader = csv.reader(listacsv)
	for i in reader:
		str1 = ''.join(i)
		print str1
		# print(i)
		try:
			s_result = ia.search_movie(str1)
			the_unt = s_result[0]
			ia.update(the_unt)
			print the_unt['rating']
			with open('ratingpelis.csv', 'a+') as peliculasrating:
				writer = csv.writer(peliculasrating, delimiter=',')
				writer.writerow([str1 , the_unt['rating']])
		except:
			pass
