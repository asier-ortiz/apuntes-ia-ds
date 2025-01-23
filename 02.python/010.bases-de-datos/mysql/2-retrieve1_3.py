import mysql.connector as con


class Country:
    def __init__(self, country_id, country, last_update):
        self.country_id = country_id
        self.country = country
        self.last_update = last_update

    def __str__(self):
        return "(country_id {}, name {}) ".format(self.country_id, self.country)

    def __repr__(self):
        return self.__str__()


db = con.connect(
    host="127.0.0.1",
    port="3300",
    user="root",
    password="admin",
    database="sakila"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM country;")

rows = cursor.fetchall()

countries = []
for row in rows:
    country = Country(row[0], row[1], row[2])
    countries.append(country)

print(countries)

cursor.close()
db.close()