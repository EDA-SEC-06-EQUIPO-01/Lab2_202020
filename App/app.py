"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""


import config as cf
import req
import sys
import helper
from ADT import list as lt
from time import process_time
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
movies_folder = "theMoviesdb/"
details_csv_name = movies_folder + "SmallMoviesDetailsCleaned.csv"
casting_csv_name = movies_folder + "MoviesCastingRaw-small.csv"


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Ordenar elementos por palabra clave")
    print("6- Crear un ranking")
    print("7- Conocer a un director")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst["size"] == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            element = it.next(iterator)
            # filtrar por palabra clave
            if criteria.lower() in element[column].lower():
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter


def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if lst["size"] == 0:
        print("La lista está vacía")
        return 0
    else:
        t1 = process_time()
        cont = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            el = it.next(iterator)
            if criteria.lower() in el[column].lower():
                cont += 1
        t2 = process_time()
        print(f"Tiempo de ejecución {t2-t1} segundos")
    return cont


def orderElementsByCriteria(criteria, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    r_list = lt.newList()
    if lst["size"] == 0:
        print("La lista está vacía")
        return 0
    else:
        t1 = process_time()
        cont = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            el = it.next(iterator)
            if criteria.lower() in el[column].lower():
                lt.addLast(r_list, el)
                cont += 1
            if cont == elements:
                return r_list
        return r_list
    


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_details = lt.newList()  # se require usar lista definida
    lista_casting = lt.newList()
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input("Seleccione una opción para continuar\n")
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                # llamar funcion cargar datos
                lista_details = helper.loadCSVFile(
                    "Data/" + details_csv_name)
                print("Datos cargados, ",
                      lista_details["size"], " elementos cargados")
                lista_casting = helper.loadCSVFile(
                    "Data/" + casting_csv_name)
                print("Datos cargados, ",
                      lista_casting["size"], " elementos cargados")
            elif int(inputs[0]) == 2:  # opcion 2
                # obtener la longitud de la lista
                if lista_details == None or lista_details["size"] == 0:
                    print("La lista esta vacía")
                else:
                    print("La lista tiene ",
                          lista_details["size"], " elementos")
            elif int(inputs[0]) == 3:  # opcion 3
                # obtener la longitud de la lista
                if lista_details == None or lista_details["size"] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input("Ingrese el criterio de búsqueda\n")
                    counter = countElementsFilteredByColumn(
                        criteria, "nombre", lista_details
                    )  # filtrar una columna por criterio
                    print(
                        "Coinciden ", counter, " elementos con el crtierio: ", criteria
                    )
            elif int(inputs[0]) == 4:  # opcion 4
                # obtener la longitud de la lista
                if lista_details == None or lista_details["size"] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input("Ingrese el criterio de búsqueda\n")
                    counter = countElementsByCriteria(
                        criteria, 0, lista_details)
                    print(
                        "Coinciden ",
                        counter,
                        " elementos con el crtierio: '",
                        criteria
                    )
            elif int(inputs[0]) == 5:
                if lista_details == None or lista_details["size"] == 0:
                    print("La lista está vacía")
                else:
                    criteria = input("Ingrese el criterio de búsqueda\n")
                    num_el = int(input("Ingrese el número de elementos de la sublista:\n"))
                    subl = orderElementsByCriteria(criteria, 0, lista_details, num_el)
                    print(f"Se obtuvo una sublista de {lt.size(subl)} elementos:\n")
                    print(subl)
            elif int(inputs[0]) == 6: # requisito 2
                asc = bool(int(input('Digite:\n' +
                                     '1 si desea se muestren las peliculas mejor calificadas\n' +
                                     '0 si desea que se muestren las peor calificadas\n')))
                rank = req.crear_ranking(lista_details, x=10, ascendent=asc)

                cont = 0
                pal = 'ascendentemente' if asc else 'descendentemente'
                print(f'Ranking ordenado por Votos {pal}:\n')
                for i in rank[0]:
                    cont += 1
                    spc = 25 - len(i["title"])
                    print(
                        f'{cont}. {i["title"]}{" "*spc} - vote count: {i["vote_count"]}')
                cont = 0
                print(f'\nRanking ordenado por Calificacion {pal}:\n')
                for i in rank[1]:
                    cont += 1
                    spc = 25 - len(i["title"])
                    print(
                        f'{cont}. {i["title"]}{" "*spc} - vote average: {i["vote_average"]}')
                print()

            elif int(inputs[0]) == 7:  # opcion 5 reto 4
                director = input("Ingrese el nombre del director\n")
                information = req.conocer_director(
                    lista_details, lista_casting, director
                )
                for d in information:
                    print(
                        "id:",
                        d["id"],
                        " - " "title:",
                        d["title"],
                        " - ",
                        "vote average:",
                        d["vote_average"],
                    )
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
