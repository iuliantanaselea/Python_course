#Exercitiul 1
"""
Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link: https://www.google.com/url?q=https://datahub.io/core/continent-codes&sa=D&source=docs&ust=1692979436921941&usg=AOvVaw0CoR1pQkoc6FTrQULfJpYo

"""
import sqlite3
connection = sqlite3.connect("mydb.db")
cursor = connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE Continents(
#         continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         continent_name TEXT NOT NULL,
#         continent_code TEXT CHAR(2) NOT NULL
#         );
#     """
# )
#Exercitiul 2
"""
Using the link above, write all SQL statements needed to add all the seven 
continents (INSERT).

"""
continent_list = [
    ("Asia", "AS"),
    ("Africa", "AF"),
    ("North America", "NA"),
    ("South America", "SA"),
    ("Oceania", "OC"),
    ("Europe", "EU"),
    ("Antarctica", "AN")
]

sql_query = "INSERT INTO Continents (continent_name, continent_code) VALUES(?,?)"
cursor.executemany(sql_query,continent_list)
connection.commit()
#Exercitiul 3
"""
Write a SQL statement to create a table called countries, with the following columns:
    a. country_code – 2 letters code (e.g. RO, US, IT, etc)
    b. country_name
    c. continent_id – foreign key
    d. population – number

"""

# cursor.execute(
#     """
#     CREATE TABLE Countries(
#     country_code CHAR(2) PRIMARY KEY,
#     country_name TEXT NOT NULL,
#     continent_code INTEGER NOT NULL,
#     population INTEGER,
#     FOREIGN KEY (continent_code) REFERENCES Continents (continent_code)
#     );
#     """
# )
# connection.commit()

#Exercitiul 4
"""
Write a few SQL statements to add some countries. Here is a list of countries
    with their codes. Feel free to invent or approximate their populations, and 
    use your geography knowledge for their continent. Add at least 10 countries, 
    as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil

"""
countries_list = [
    ("RO", "Romania", "EU", 19000000),
    ("US", "USA", "NA", 330000000),
    ("FR", "France", "EU", 70000000),
    ("HU", "Hungary", "EU", 9000000),
    ("CA", "Canada", "NA", 40000000),
    ("CH", "China", "AS", 1450000000),
    ("BE", "Belgium", "EU", 12000000),
    ("EG", "Egypt", "AF", 110000000),
    ("AU", "Australia", "OC", 25000000)
]

insert_countries_sql = """
INSERT INTO Countries (country_code, country_name, continent_code, population)
VALUES (?, ?, ?, ?);
"""
# cursor.executemany(insert_countries_sql,countries_list)
# connection.commit()

#Exercitiul 5
"""
Write a SQL statement to select all countries, ordered by name.
Write another statement to count them all.
"""
select_countries_sql = "SELECT * FROM Countries ORDER BY country_name;"
cursor.execute(select_countries_sql)
countries = cursor.fetchall()
for country in countries:
    print(country)

count_countries_sql = "SELECT COUNT(*) FROM Countries ;"
cursor.execute(count_countries_sql)
count = cursor.fetchone()[0]
print(f"Numarul total este {count}")
#Exercitiul 6
"""
Write a SQL statement to select only countries with a population 
greater than 20 millions. 
"""
sql = "SELECT * FROM countries WHERE population > 20000000;"
cursor.execute(sql)

# Fetch and print the results
countries = cursor.fetchall()
for country in countries:
    print(country)

#Exercitiul 7
"""
Write a SQL statement to select only countries that start with a certain letter 
(choose one that exists for you, e.g. C in the example above).
"""
sql = "SELECT * FROM countries WHERE country_name LIKE 'C%';"
cursor.execute(sql)

# Fetch and print the results
countries = cursor.fetchall()
for country in countries:
    print(country)

#Exercitiul 8
"""
Write a SQL statement that groups all countries by continents, and counts them.
"""
sql = """
SELECT continent_code, COUNT(*) AS number_of_countries
FROM countries
GROUP BY continent_code;
"""
cursor.execute(sql)

# Fetch and print the results
continent_counts = cursor.fetchall()
for continent, count in continent_counts:
    print(f"Continent: {continent}, Number of countries: {count}")

#Exercitiul 9
"""
Write a SQL statement that groups all countries by continent, 
and computes the total population per continent (SUM).
"""
sql = """
SELECT continent_code, SUM(population) AS total_population
FROM countries
GROUP BY continent_code;
"""
cursor.execute(sql)

# Fetch and print the results
continent_populations = cursor.fetchall()
for continent, population in continent_populations:
    print(f"Continent: {continent}, Total Population: {population}")

