import config as cf
import helper as h
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt


def conocer_director(details, casting, director_name) -> dict:

    lst = [
        node["id"]
        for node in h.forward_travel(casting)
        if node["director_name"] == director_name
    ]

    info = []
    for node in h.forward_travel(details):
        if node["id"] in lst:
            d = {
                "id": node["id"],
                "title": node["title"],
                "vote_average": node["vote_average"],
            }
            info.append(d)

    return info
