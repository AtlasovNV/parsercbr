import psycopg2

connection = psycopg2.connect(database="gps_heatmap", user="postgres", password="1234", host="localhost", port=5433)
