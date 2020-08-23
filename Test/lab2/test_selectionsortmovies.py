import config
import pytest
from Sorting import selectionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import helper
from test_arraylistmovies import load_arraylistmovies
from test_singlelinkedlistmovies import load_linkedlistmovies


def test_selectionsort_movies_linkedlist(load_arraylistmovies):
    details, casting = load_arraylistmovies

    sort.selectionSort(details, helper.less)
    sort.selectionSort(casting, helper.less)


def test_selectionsort_movies_array(load_linkedlistmovies):
    details, casting = load_linkedlistmovies

    sort.selectionSort(details, helper.less)
    sort.selectionSort(casting, helper.less)
