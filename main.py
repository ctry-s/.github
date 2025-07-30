from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import jmcomic

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text='请输入本子ID:')
        self.layout.add_widget(self.label)
        self.input = TextInput(multiline=False)
        self.layout.add_widget(self.input)
        self.btn = Button(text='开始下载')
        self.btn.bind(on_press=self.download)
        self.layout.add_widget(self.btn)
        self.output = Label(text='')
        self.layout.add_widget(self.output)
        return self.layout

    def download(self, instance):
        album_id = self.input.text.strip()
        if album_id.isdigit():
            try:
                option = jmcomic.create_option_by_file('option.yml')
                jmcomic.download_album(int(album_id), option)
                self.output.text = "下载完成！"
            except Exception as e:
                self.output.text = f"错误: {str(e)}"
        else:
            self.output.text = "请输入有效数字"

if __name__ == '__main__':
    MyApp().run()
