import wpf
import clr
clr.AddReference('System.Data')
from System.Data import SqlClient
from System.Windows import Application, Window
from Zwierzeta import *



class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'zoo4.xaml')

        
    def Button_Click(self, sender, e):
        form = Zwierzeta()
        form.Show()
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
