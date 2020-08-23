import pytest

import config
import helper
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

movies_folder = "theMoviesdb/"
details_csv_name = movies_folder + "SmallMoviesDetailsCleaned.csv"
casting_csv_name = movies_folder + "MoviesCastingRaw-small.csv"


def test_arraylistmovies():

    lista_details = helper.loadCSVFile(
        config.data_dir + details_csv_name, impl="ARRAY_LIST"
    )

    lista_casting = helper.loadCSVFile(
        config.data_dir + casting_csv_name, impl="ARRAY_LIST"
    )

    return lista_details, lista_casting


@pytest.fixture
def load_arraylistmovies():
    return test_arraylistmovies()
