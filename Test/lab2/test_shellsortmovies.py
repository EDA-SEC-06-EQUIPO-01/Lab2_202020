import config
import pytest
from Sorting import shellsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import helper
from test_arraylistmovies import load_arraylistmovies
from test_singlelinkedlistmovies import load_linkedlistmovies


def test_shellsort_movies_linkedlist(load_arraylistmovies):
    details, casting = load_arraylistmovies

    sort.shellSort(details, helper.less)
    sort.shellSort(casting, helper.less)


def test_shellsort_movies_array(load_linkedlistmovies):
    details, casting = load_linkedlistmovies

    sort.shellSort(details, helper.less)
    sort.shellSort(casting, helper.less)
