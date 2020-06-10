import wpf, clr

clr.AddReference('System.Data')
from System.Data import SqlClient

from System.Windows import Application, Window

conn = SqlClient.SqlConnection("Server=sql7.freemysqlhosting.net;Database=sql7343753;UID=sql7343753;PWD=JGWVXubSX1")
conn.Open()

cmd = SqlClient.SqlCommand(sql, conn)
exe = cmd.ExecuteReader()

exe.Close()
conn.Close()

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'zoo_proba3.xaml')
    

if __name__ == '__main__':
    Application().Run(MyWindow())
