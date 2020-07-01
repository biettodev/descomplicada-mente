from functions.connect import connection

conn = connection()
if conn != False:
    cursor = conn.cursor()
else:
    cursor = False

def getMovies():
    
    if cursor:
        select = "SELECT * FROM `filmes`"
        cursor.execute(select)
        result = cursor.fetchall()

        return result
        
    else:
        return False