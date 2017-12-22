import mysql.connector



conn = mysql.connector.connect(host='addr', user='username', password='password', database='databaseName')
cursor = conn.cursor()
st= 'UC0000026392'
cursor.execute('select * from table_name where row_name ="%s"' %st)
value = cursor.fetchall()
for i in value:
    print(i)
    print('***************************\n'*3)
cursor.close()
conn.close()