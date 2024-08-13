import mysql.connector 

conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
my_cursor=conn.cursor()
my_cursor.execute("select * from mydata.firstfile")
            
conn.commit()
conn.close()
print("connection succesfull")