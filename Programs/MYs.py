import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1605')
print(mydb.connection_id)