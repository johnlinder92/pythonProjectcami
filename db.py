import mysql.connector


class db:

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cami_store")
  mycursor = mydb.cursor()

def createTables(mycursor):
  mycursor.execute("CREATE TABLE cars (id INT AUTO_INCREMENT PRIMARY KEY, precio VARCHAR(255), color VARCHAR(255))")
  mycursor.execute("CREATE TABLE comida (id INT AUTO_INCREMENT PRIMARY KEY, precio VARCHAR(255), description VARCHAR(255))")

def addCar(mycursor, car):
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("John", "Highway 21")
  mycursor.execute(sql, val)

  mydb.commit()
