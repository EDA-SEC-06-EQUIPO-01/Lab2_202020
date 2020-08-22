import config as cf
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt


def conocer_director(details, casting, director_name) -> dict:
    pass


# funcion de utilidad para viajar por la lista
def forward_travel(lista, parameter=None):

    iter = it.newIterator(lista)

    while it.hasNext(iter):
        node = it.next(iter)

        if parameter:
            yield node[parameter]
        else:
            yield node
