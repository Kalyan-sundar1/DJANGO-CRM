

import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print("All done")