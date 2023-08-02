import sqlite3
con = sqlite3.connect('BD_teste.db')
cursor = con.cursor()

#nome = input('Digite seu nome\n')
#idade = int(input('Digite sua idade\n'))

#cursor.execute(f"INSERT INTO Pessoas VALUES ('{nome}', {idade})")
x = cursor.execute(f"SELECT * from Pessoas")
for i in x:
    print(i)
#con.commit()