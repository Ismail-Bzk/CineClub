from PySide2 import QtWidgets , QtCore
from movie import *

class App(QtWidgets.QWidget):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connection()

    
    def setup_ui(self):
        self.layout =QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie= QtWidgets.QPushButton("Add a movie")
        self.lw_movies= QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies= QtWidgets.QPushButton("delete movie(s)")

        
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)
        


    

    def setup_connection(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)


    def add_movie(self):
        texte = self.le_movieTitle.text()
        if not texte:
            return False
        m=Movie(texte)
        if(m.add_to_movies()):
            self.lw_movies.addItem(m.title)
     
        self.le_movieTitle.setText("")
    
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie= selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            # we get the position(row) and we delete it via takeItem
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

    
    def populate_movies(self):
        movies= get_movies()
        for movie in movies:
            """
            self.lw_movies.addItem(movie.title)
            """
            lw_item=QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)




app = QtWidgets.QApplication([])
win=App()
win.show()
app.exec_()

