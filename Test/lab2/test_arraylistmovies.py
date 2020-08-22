import pytest
import config
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
import csv
from time import process_time

movies_folder = "theMoviesdb/"
details_csv_name = movies_folder + "SmallMoviesDetailsCleaned.csv"
casting_csv_name = movies_folder + "MoviesCastingRaw-small.csv"


def loadCSVFile(file, sep=";", impl="SINGLE_LINKED"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    # lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList(impl)  # Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lt.addLast(lst, row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return lst


def test_arraylistmovies():

    lista = lt.newList("ARRAY_LIST")

    lista_details = loadCSVFile(config.data_dir + details_csv_name, impl="ARRAY_LIST")

    lista_casting = loadCSVFile(config.data_dir + casting_csv_name, impl="ARRAY_LIST")
