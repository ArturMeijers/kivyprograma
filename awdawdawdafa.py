from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.info_label = Label(text="Программа тренировок на неделю!")
        layout.add_widget(self.info_label)
        self.buttons_info = {'День 1': '1aawdadaw1',
                             'День 2': 'awdawwfawd',
                             'День 3': 'Information for button 3',
                             'День 4': 'Information for button 4',
                             'День 5': 'Information for button 5',
                             'День 6': '12312513',
                             'День 7': 'awdafgeaw',}

        for i in range(7):
            btn = Button(text="Button " + str(i + 1))
            btn.bind(on_press=self.open_info)
            layout.add_widget(btn)

        self.add_widget(layout)

    def open_info(self, instance):
        self.manager.current = 'info'
        self.manager.get_screen('info').update_info(instance.text)

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.info_label = Label(text="")
        layout.add_widget(self.info_label)

        back_button = Button(text="Back")
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_info(self, button_text):
        self.info_label.text = "You clicked on " + button_text

    def go_back(self, instance):
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(InfoScreen(name='info'))
        return sm

if __name__ == "__main__":
    MyApp().run()

