from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout as Grid 

# grid Layout
class GridBerg(Grid):
  def __init__(self,*args):
    super().__init__(*args)
    self.cols=2
    self.rows= 2

    self.lbl = Label(text = "Твой ответ")
    self.btn = Button(text="Старт")
    self.input = TextInput()

    def getInputValue(instance):
      if self.input.text != "":
        self.lbl.text = self.input.text

    self.btn.bind(on_press = getInputValue)

    self.add_widget(self.lbl)
    self.add_widget(self.btn)
    self.add_widget(self.input)

# главный класс
class Main(App):
  def __init__(self,what,**kwargs):
    super().__init__(**kwargs)
    self.what = what
    self.router = [GridBerg(),"none"]
# gg - Get Grid
  def build(self):
    if self.what == "gg":
      return self.router[0]

    return Label(text="Что не так в вызове")


def start(request):
  Main(request).run()