import psycopg2

# setting up connection with postgreSQL

conn =  psycopg2.connect(dbname= 'postgres', user = 'postgres')

# printing the connection details
print(conn)

#closing the connection
conn.close()
