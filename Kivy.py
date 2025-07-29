import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import jmcomic
from kivy.core.text import LabelBase
import os

# 设置kivy版本号
kivy.require('1.9.1')

# 注册支持中文的字体 - 尝试多种方式
def register_chinese_font():
    # 尝试使用系统字体
    system_fonts = [
        os.path.join(os.environ.get('WINDIR', ''), 'Fonts', 'simhei.ttf'),  # Windows
        '/System/Library/Fonts/PingFang.ttc',  # macOS
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
        'simhei.ttf',  # 相对路径
        'DroidSansFallback.ttf'  # Android
    ]
    
    for font_path in system_fonts:
        if os.path.exists(font_path):
            try:
                LabelBase.register(name='ChineseFont',
                                 fn_regular=font_path,
                                 fn_bold=font_path,
                                 fn_italic=font_path,
                                 fn_bolditalic=font_path)
                print(f"成功注册字体: {font_path}")
                return True
            except Exception as e:
                print(f"注册字体失败 {font_path}: {e}")
                continue
    
    # 如果所有字体都失败，使用默认字体
    LabelBase.register(name='ChineseFont',
                      fn_regular=None,
                      fn_bold=None,
                      fn_italic=None,
                      fn_bolditalic=None)
    print("使用默认字体")
    return False

register_chinese_font()

class ComicDownloaderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ComicDownloaderLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # 创建配置对象
        self.option = jmcomic.create_option_by_file('E:/TEST/option.yml')

        # 标签提示输入本子ID - 指定中文字体
        self.label = Label(
            text="请输入本子ID:",
            font_name='ChineseFont',
            font_size=20
        )
        self.add_widget(self.label)

        # 文本输入框
        self.input = TextInput(
            multiline=False,
            font_name='ChineseFont',
            font_size=20
        )
        self.add_widget(self.input)

        # 下载按钮 - 指定中文字体
        self.button = Button(
            text="下载",
            font_name='ChineseFont',
            font_size=20
        )
        self.button.bind(on_press=self.download_comic)
        self.add_widget(self.button)

        # 结果显示标签 - 指定中文字体
        self.result_label = Label(
            text="",
            font_name='ChineseFont',
            font_size=18
        )
        self.add_widget(self.result_label)

    def download_comic(self, instance):
        album_id = self.input.text
        # 验证输入是否为数字
        if album_id.isdigit():
            try:
                jmcomic.download_album(int(album_id), self.option)
                self.result_label.text = "下载成功"
            except Exception as e:
                self.result_label.text = f"运行错误: {e}"
        else:
            self.result_label.text = "输入无效，请输入数字ID"

class ComicDownloaderApp(App):
    def build(self):
        return ComicDownloaderLayout()

if __name__ == '__main__':
    ComicDownloaderApp().run()