#from ds import Ui_DescomplicadaMente
#from PySide2 import QtWidgets, QtGui, QtCore
from functions.connect import connection

conn = connection()
cursor = conn.cursor()

def getMovies():
    sql = cursor.execute("SELECT `filme_id`, `titulo`, `likes` FROM `filmes`")
    result = cursor.fetchall()

    return result