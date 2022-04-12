import os
import logging
import json
from pathlib import Path

CUR_Dir=os.path.dirname(__file__)

Data_File= os.path.join(CUR_Dir,"data","movies.json")



def get_movies():

    with open(Data_File,"r") as f:
        liste = json.load(f)
    
    return [Movie(movie_tilte) for movie_tilte in liste]


class Movie:
    def __init__(self,title):
        self.title=title.title()
        
    def  __str__(self):
        return self.title
    
    def _get_movies(self):
        f=open(Data_File, "r")
        liste = json.load(f)
        f.close()
        return liste
    
    def _write_movies(self,movies):
        
        f=open(Data_File, "w")
        json.dump(movies,f, ensure_ascii= True, indent= 3)
        f.close()
    
    def add_to_movies(self):
        movies = self._get_movies()
    
        if self.title not in movies:
                movies.append(self.title)
                self._write_movies(movies)
                return True
        else:
            logging.warning(f"The movie {self.title} is already registred")
            return False
    
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"The movie {self.title} is not registred")
            return False


if __name__ == "__main__":
    a=get_movies()
    for i in a:
        print(i)