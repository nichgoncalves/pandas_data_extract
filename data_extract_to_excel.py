import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"path of oracle instaclient")
import pandas as pd

uid = " "    # user
pwd = " "   # password
db = "  "  # Connection configured on tnsnames.ora
 
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) #Db Connect
cursor = connection.cursor() # Cursor

df1 = pd.read_sql("select * from table were condition is", connection)

writer = pd.ExcelWriter(r"path to save file")
df1.to_excel(writer, sheet_name='name of sheet1', index=False)
df2.to_excel(writer, sheet_name='name of sheet2', index=False)

writer.save()

print ("End")
                
cursor.close()
connection.close()