import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all reords from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select Queen from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with the "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is " Queen" fom the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Amy Winehouse"])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [252])
cursor.execute('SELECT * FROM "Track" WHERE "ArtistId" = %s', [51])


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results

for result in results:
    print(results)
