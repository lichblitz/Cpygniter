from pyignite import Client

from connections import Connection

## Open a connection
# client = Client()
# with client.connect('localhost', 10800):
    # my_cache = client.get_or_create_cache('my cache')
    # my_cache.put('my key', 34)
    # result = my_cache.get('my key')

    # print (result)

conn = Connection(port=10800,host="localhost")
conn.connect()

CREATE_TABLE='''CREATE TABLE City (
    ID INT(11),
    Name CHAR(35),
    CountryCode CHAR(3),
    District CHAR(20),
    Population INT(11),
    PRIMARY KEY (ID, CountryCode)
) WITH "affinityKey=CountryCode"'''

CITY_INSERT_QUERY = '''INSERT INTO City(
    ID, Name, CountryCode, District, Population
) VALUES (3793, 'Bogota', 'COL', 'Bogota DC', 10000000)'''

# conn.query(sql=CITY_INSERT_QUERY)

# conn.query(sql=CREATE_TABLE)
result = conn.query(sql="SELECT * from City")

for city in result:
    print (city)
