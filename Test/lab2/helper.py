import config
import csv
from time import process_time

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt


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


def less(element1, element2):
    if int(element1["id"]) < int(element2["id"]):
        return True
    return False
