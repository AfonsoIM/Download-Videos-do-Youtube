from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from pytube import YouTube
import os

class MyApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')

        self.lblTitulo = Label(text="Download de Vídeos do Youtube", font_size=60, color=(1, 1, 1, 1))
        layout.add_widget(self.lblTitulo)

        self.lblSubTitulo1 = Label(text="Insira o link do vídeo", font_size=24, color=(1, 1, 1, 1))
        layout.add_widget(self.lblSubTitulo1)

        self.Link = TextInput(font_size=24, size_hint=(None, None), size=(1366, 100))
        layout.add_widget(self.Link)

        btnDownload = Button(text="Download", font_size=24, background_color=(1, 0, 0, 1))
        btnDownload.bind(on_press=self.download)
        layout.add_widget(btnDownload)

        return layout

    def download(self, instance):
        link = self.Link.text.strip()

        if not link:
            self.lblTitulo.text = "Por favor, insira o link do vídeo."
            return

        try:
            diretorio = os.path.join(os.path.expanduser('~'), 'Downloads')
            youtube_video = YouTube(link)
            video = youtube_video.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=diretorio)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            self.lblTitulo.text = "Download concluído com sucesso!"
            popup = Popup(title="Sucesso", content=Label(text="Download concluído com sucesso!"))
            popup.open()
        except Exception as e:
            self.lblTitulo.text = f"Ocorreu um erro: {str(e)}"
            popup = Popup(title="Erro", content=Label(text=f"Ocorreu um erro: {str(e)}"))
            popup.open()

if __name__ == '__main__':
    MyApp().run()
