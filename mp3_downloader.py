import tkinter
import customtkinter
from pytube import YouTube

def download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        file = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="white")
        file.download()
        result.configure(text="SUCCESSFULLY DOWNLOADED", text_color="yellow")
    except:
        result.configure(text="FAILED", text_color="red")


# App design
app = customtkinter.CTk()
app.geometry("750x380")
app.title("MP3 Downloader")
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

bg = tkinter.PhotoImage(file=r"C:\Users\tibor\OneDrive\Počítač\MP3_downloader\bg_image\bg.png")
background = tkinter.Label(app, image=bg)
background.place(x=0, y=0, relheight=1, relwidth=1)

# App UI Elements
title = customtkinter.CTkLabel(app, text="INSERT A VALID LINK", font=("Helvetica", 25, "bold"))
title.pack(padx=5, pady=5)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height= 40, textvariable=url)
link.pack(padx=5, pady=5)

button = customtkinter.CTkButton(app, text="DOWNLOAD", font=("Helvetica", 15), command=download)
button.pack(padx=5, pady=5)

# Completion Elements
result = customtkinter.CTkLabel(app, text="", font=("Helvetica", 15, "bold"))
result.pack(padx=5, pady=5)


# RUN
app.mainloop()