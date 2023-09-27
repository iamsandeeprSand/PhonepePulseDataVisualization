import psycopg2
import csv
import pandas as pd
conn = psycopg2.connect(host="localhost",user="postgres",password="sandeep",port=5432,database="PhonePe")
sand = conn.cursor()

#Pushing the Aggregated transaction details from CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\aggregated_transaction.csv")
values = df.values.tolist()
query = "INSERT INTO aggregated_transaction(State,Year,Quarter,Transaction_type,Transaction_count,Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()

#Pushing the Aggregated user details from  CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\aggregated_user.csv")
values = df.values.tolist()
query = "INSERT INTO aggregated_user(State,Year,Quarter,Brands,User_Count,User_Percentage) VALUES (%s, %s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()


#Pushing the map transaction details from CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\map_transaction.csv")
values = df.values.tolist()
query = "INSERT INTO map_transaction(State,Year,Quarter,District,Transaction_Count,Transaction_Amount) VALUES (%s, %s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()



#Pushing the map user details from CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\map_user.csv")
values = df.values.tolist()
query = "INSERT INTO map_user(State,Year,Quarter,District,Registered_User) VALUES (%s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()



#Pushing the top transaction details from CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\top_transaction.csv")
values = df.values.tolist()
query = "INSERT INTO top_transaction(State,Year,Quarter,District_Pincode,Transaction_count,Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()




#Pushing the top user details from CSV file to SQL table
df = pd.read_csv("D:\\Pulse\\top_user.csv")
values = df.values.tolist()
query = "INSERT INTO top_user(State,Year,Quarter,District_Pincode,Registered_User) VALUES (%s, %s, %s, %s, %s)"
sand.executemany(query,values)
conn.commit()