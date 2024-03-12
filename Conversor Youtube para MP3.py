from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os

#função que faz o download
def download():
    link = Link.get("1.0", "end-1c").strip() #aqui vai buscar qual foi o link inserido na text box
    diretorio = Diretorio.get("1.0", "end-1c").strip() #aqui vai buscar o diretorio para onde pretende que seja feito o download
    if not link or not diretorio: #se não houver link ou diretorio colocado ele mostra uma message box a avisar que falta algo
        messagebox.showwarning("Aviso", "Por favor, insira o link e o diretório.")
        return
    try:
        youtube_video = YouTube(link) #transforma o link num link do tipo Youtube
        video = youtube_video.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=diretorio)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Sucesso", "Download concluido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

root = tk.Tk()
root.state('zoomed')
root.geometry("1366x768")
root.title("Download de Vídeos do Youtube")
root.configure(bg="white")

frame1 = tk.Frame(root, bg="white")
frame1.pack()

lblred = tk.Label(frame1, text="red", bg="red", fg="red", width=300, height=7)
lblred.pack(pady=1)

lblTitulo = tk.Label(frame1, text="Download de Vídeos do Youtube", font=("Digit", 50), bg="red", foreground="White")
lblTitulo.place(y=10, x=250)

lblSubTitulo1 = tk.Label(frame1, text="Insira o link do vídeo", font=("Digit", 20), bg="white", fg="black")
lblSubTitulo1.pack(pady=10)

btnDownload = tk.Button(frame1, text='Download', font=('Digit', 20), width=50, height=0, bg="red", fg="white", command=download)
btnDownload.pack(pady=250)

btnBordaTxtBox = tk.Label(frame1, text="Border", width=117, height=4, bg="black", fg="black")
btnBordaTxtBox.place(y=165, x=270)

btnBordaTxtBoxD = tk.Label(frame1, text="Border", width=117, height=4, bg="black", fg="black")
btnBordaTxtBoxD.place(y=305, x=270)

Link = tk.Text(root, font=('Calibri', 16), width=73, height=2)
Link.place(x=278, y=170)

Diretorio = tk.Text(root, font=('Calibri', 16), width=73, height=2)
Diretorio.place(x=278, y=310)

lblSubTitulo2 = tk.Label(frame1, text="Insira o diretório para onde pretende fazer o Download", font=("Digit", 20), bg="white", fg="black")
lblSubTitulo2.place(y=260, x=350)

root.mainloop()