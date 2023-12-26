"""
Exercitiul 1

Write a SQL statement to create a table called continents,
with the following columns:
continent_code
continent_name
continent_code – 2 letters code, use this link
https://datahub.io/core/continent-codes
"""

# https://sqlitestudio.pl/
import sqlite3
# conexiune baza de date
connection = sqlite3.connect("mydb.db")
cursor = connection.cursor()
# dupa ce rulam, o sa vedem ca se va crea un nou fisier mydb.db

# SQL statement to create the 'continents' table
cursor.execute(
    """
CREATE TABLE Continents (
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code TEXT CHAR(2) NOT NULL
    );
    """
                )

"""
Exercitiul 2

Using the link above, write all SQL statements needed to
add all the seven continents (INSERT).
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

sql_querry = "INSERT INTO Continents (continent_name, continent_code) VALUES (?, ?)"

cursor.executemany(sql_querry, continent_list)
connection.commit()

"""
Exercitiul 3

Write a SQL statement to create a table called countries,
with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_code – foreign key
population – number
"""
cursor.execute(
    """
    CREATE TABLE Countries(
    country_code CHAR(2) PRIMARY KEY,
    country_name TEXT NOT NULL,
    continent_code INTEGER NOT NULL,
    population INTEGER,
    FOREIGN KEY (continent_code) REFERENCES Continents (continent_code)
    );
    """
)
connection.commit()

"""
Exercitiul 4

Write a few SQL statements to add some countries. Here is a
list of countries with their codes. Feel free to invent or approximate
their populations, and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
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
INSERT INTO countries (country_code, country_name, continent_code, population)
VALUES (?, ?, ?, ?);
"""

cursor.executemany(insert_countries_sql, countries_list)
connection.commit()


# sql_query = "INSERT INTO Countries(country_code, country_name, continent_code, population)
#       VALUES("RO", "Romania", "EU", 19000000)
# cursor.execute(sql_query)
"""
Exercitiul 5

Write a SQL statement to select all countries, ordered by name.
Write another statement to count them all.
"""
# SQL statement to select all countries, ordered by name
select_countries_sql = "SELECT * FROM countries ORDER BY country_name;"
cursor.execute(select_countries_sql)
countries = cursor.fetchall()
for country in countries:
    print(country)

print("#"*20)

# SQL statement to count all countries
count_countries_sql = "SELECT COUNT(*) FROM countries;"
cursor.execute(count_countries_sql)
count = cursor.fetchone()[0]
print(f"\nTotal number of countries: {count}")

print("#"*20)
"""
Exercitiul 6

Write a SQL statement to select only countries with a population
greater than 20 millions.
"""
# SQL statement to select countries with population greater than 20 million
sql = "SELECT * FROM countries WHERE population > 20000000;"
cursor.execute(sql)

# Fetch and print the results
countries = cursor.fetchall()
for country in countries:
    print(country)

print("#"*20)
"""
Exercitiul 7

Write a SQL statement to select only countries that start with a
certain letter (choose one that exists for you, e.g. C in the example above).
"""
# SQL statement to select countries starting with the letter 'C'
sql = "SELECT * FROM countries WHERE country_name LIKE 'C%';"
cursor.execute(sql)

# Fetch and print the results
countries = cursor.fetchall()
for country in countries:
    print(country)

print("#"*20)
"""
Exercitiul 8

Write a SQL statement that groups all countries by continents,
and counts them.
"""
# SQL statement to group countries by continents and count them
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

print("#"*20)
"""
Exercitiul 9

Write a SQL statement that groups all countries by continent,
and computes the total population per continent (SUM).
"""
# SQL statement to group countries by continents and compute total population
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

print("#"*20)
"""
Exercitiul 10

Extra exercises can be found online:
W3Schools
OneCompiler

"""

# Create the cities table
cursor.execute("""
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY,
    city_name TEXT NOT NULL,
    country_code VARCHAR(10) NOT NULL,
    population BIGINT
)
""")

# Insert sample data into cities
cursor.executemany("""
INSERT INTO cities (city_name, country_code, population) VALUES (?, ?, ?)
""", [
    ('New York', 'US', 8175133),
    ('Los Angeles', 'US', 3792621),
    ('London', 'UK', 8787892),
    ('Tokyo', 'JP', 13751500)
])

# Create the history_cities table
cursor.execute("""
CREATE TABLE history_cities (
    history_id INTEGER PRIMARY KEY,
    city_id INTEGER,
    city_name TEXT,
    country_code VARCHAR(10),
    population BIGINT,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Create the trigger for the cities table
cursor.execute("""
CREATE TRIGGER trigger_log_city_deletion 
AFTER DELETE ON cities 
BEGIN 
    INSERT INTO history_cities (city_id, city_name, country_code, population) 
    VALUES (OLD.city_id, OLD.city_name, OLD.country_code, OLD.population); 
END;
""")

# Commit the transactions
connection.commit()


city_to_delete = 'New York'
cursor.execute("DELETE FROM cities WHERE city_name = ?", (city_to_delete,))


cursor.execute("SELECT * FROM history_cities")
rows = cursor.fetchall()

print("\nHistory Cities Table Content:")
print("-------------------------------")
for row in rows:
    print(row)
