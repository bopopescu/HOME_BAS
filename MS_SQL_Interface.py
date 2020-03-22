import pyodbc

server = 'MILLER-2019-002\SQLEXPRESS'
database = 'BASConfig'
username = 'smiller'
password = 'GWm50s50'
MS_SQL_CONNECTION = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = MS_SQL_CONNECTION.cursor()

root_button_list = []
cursor.execute('SELECT Parent, Text, Command From RootButtons')
i = 0
for row in cursor:
    root_button_list.append(row)
    print(root_button_list[i])
    i = i + 1

print(root_button_list)
def MS_SQL_Select(Table):
    cursor.execute('SELECT * From '+Table)
    for row in cursor:
        print(row)
