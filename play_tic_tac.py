# Импортируем необходимые нам элементы:
from kivy.app import App
 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
 
from kivy.uix.button import Button
from kivy.config import Config

# С помощью Config и функции set зададим параметры нашего окна 300х300: 
Config.set("graphics","resizable","0")
Config.set("graphics","width","300")
Config.set("graphics","height","300")
 
 
class MainApp(App):
    """Класс для нового хода, крестик, сменяется ноликом и наоборот"""
    def __init__(self):
        super().__init__() # инициализирует родительский класс App.
        self.switch = True 
 
    def tic_tac_toe(self, arg):
        #  функция исполняет всю логику нашего приложения
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch
 
        coordinate = (
            (0,1,2), (3,4,5), (6,7,8), # X
            (0,3,6), (1,4,7), (2,5,8), # Y
            (0,4,8), (2,4,6),          # D
        )
 
        vector = lambda item: [self.buttons[x].text for x in item]
 
        color = [0,1,0,1]
 
        for item in coordinate:
            # цикл, который будет определять победную комбинацию нажатых кнопок
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break
 
    def restart(self, arg):
        # : функция, которую мы будем вызывать для того, чтобы перезапустить игру,
        #  по сути сбросив все значения кнопок и переменных до начального состояния
        self.switch = True
 
        for button in self.buttons:
            button.color = [0,0,0,1]
            button.text = ""
            button.disabled = False
 
    def build(self):
        # Функция строит наш инрефейс процесса игры
        self.title = "Крестики-нолики"
 
        root = BoxLayout(orientation="vertical", padding=5)
 
        grid = GridLayout(cols=3)
        self.buttons = []
        for _ in range(9):
            button = Button(
                color = [0,0,0,1],
                font_size = 24,
                disabled = False,
                on_press = self.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)
 
        root.add_widget(grid)
        # виджет для кнопки Restart
        root.add_widget(
            Button(
               text = "Restart",
               size_hint = [1,.1],
               on_press = self.restart
            )
        )
 
        return root
 
 
if __name__ == "__main__":
    MainApp().run()