import wpf
import clr
clr.AddReference('System.Data')
from System.Data import SqlClient
from System.Windows import Application, Window

conn = SqlClient.SqlConnection("Server=sql7.freemysqlhosting.net;Database=sql7343753;UID=sql7343753;PWD=JGWVXubSX1")
conn.Open()

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'zoo4.xaml')

        
    def Button_Click(self, sender, e):
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
