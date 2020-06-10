import wpf
from System.Windows import Window

class Zwierzeta(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Zwierzeta.xaml')


