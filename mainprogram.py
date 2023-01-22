from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        title = Label(text='Программа тренировок')
        layout.add_widget(title)
        button1 = Button(text='День 1', on_press=self.open_info1, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button2 = Button(text='День 2', on_press=self.open_info2, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button3 = Button(text='День 3', on_press=self.open_info3, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button4 = Button(text='День 4', on_press=self.open_info4, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button5 = Button(text='День 5', on_press=self.open_info5, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button6 = Button(text='День 6', on_press=self.open_info6, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        button7 = Button(text='День 7', on_press=self.open_info7, size_hint=(1, 1), background_color=(0, 1, 0, 1))
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        layout.add_widget(button6)
        layout.add_widget(button7)
        self.add_widget(layout)

    def open_info1(self, instance):
        self.manager.current = 'info1'

    def open_info2(self, instance):
        self.manager.current = 'info2'

    def open_info3(self, instance):
        self.manager.current = 'info3'

    def open_info4(self, instance):
        self.manager.current = 'info4'

    def open_info5(self, instance):
        self.manager.current = 'info5'

    def open_info6(self, instance):
        self.manager.current = 'info2'

    def open_info7(self, instance):
        self.manager.current = 'info2'


class InfoWindow1(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 1')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class InfoWindow2(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 2')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

class InfoWindow3(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 3')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class InfoWindow4(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow4, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 4')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class InfoWindow5(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow5, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 5')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class InfoWindow6(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow6, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 6')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class InfoWindow7(Screen):
    def __init__(self, **kwargs):
        super(InfoWindow7, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='This is some information 7')
        back_button = Button(text='Back', on_press=self.go_back, size_hint=(1, 0.1), background_color=(0, 1, 0, 1))
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(InfoWindow1(name='info1'))
        sm.add_widget(InfoWindow2(name='info2'))
        sm.add_widget(InfoWindow3(name='info3'))
        sm.add_widget(InfoWindow4(name='info4'))
        sm.add_widget(InfoWindow5(name='info5'))
        sm.add_widget(InfoWindow6(name='info6'))
        sm.add_widget(InfoWindow7(name='info7'))
        return sm


if __name__ == '__main__':
    MyApp().run()
