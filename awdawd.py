import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)

        self.text_label = Label(text='Welcome')
        layout.add_widget(self.text_label)

        button1 = Button(text='Button 1', on_press=self.change_text1)
        layout.add_widget(button1)

        button2 = Button(text='Button 2', on_press=self.change_text2)
        layout.add_widget(button2)

        return layout

    def change_text1(self, instance):
        self.text_label.text = 'Text for button 1'

    def change_text2(self, instance):
        self.text_label.text = 'Text for button 2'

if __name__ == '__main__':
    MyApp().run()