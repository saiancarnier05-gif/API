import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "user2",
    password = "123456",
    database = "ciel2027"
)

cursor = mydb.cursor()
nom = "TOTO"
prenom = "TITI"
request = f"INSERT INTO etudiant (nom, prenom) VALUES ('{nom}', '{prenom}');"
cursor.execute(request)
mydb.commit()