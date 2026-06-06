import os
import threading
import tkinter as tk
from tkinter import messagebox

try:
    import pygame
    pygame.mixer.init()
    AUDIO_BACKEND = "pygame"
except Exception:
    pygame = None
    AUDIO_BACKEND = None

# Login validation
def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "admin" and pwd == "1234":
        login_window.destroy()
        open_second_window()
    else:
        messagebox.showerror("Login Failed", "Invalid ID or Password")


# Second window
def open_second_window():
    second = tk.Tk()
    second.title("Second Window")
    second.geometry("300x200")

    btn = tk.Button(
        second,
        text="This is for ",
        font=("Arial", 12),
        command=lambda: open_third_window(second)
    )
    btn.pack(expand=True)

    second.mainloop()


# Third window
def play_background_song(song_file):
    if not os.path.exists(song_file):
        print(f"Audio file not found: {song_file}")
        return

    if AUDIO_BACKEND == "pygame":
        def _play():
            try:
                pygame.mixer.music.load(song_file)
                pygame.mixer.music.play(-1)
            except Exception as e:
                print("Could not play audio:", e)

        threading.Thread(target=_play, daemon=True).start()
    else:
        print("Install pygame (pip install pygame) to enable background music.")


def stop_background_song():
    if AUDIO_BACKEND == "pygame" and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()


def open_third_window(parent):
    parent.destroy()

    third = tk.Tk()
    third.title("Birthday Wishes")
    third.geometry("500x250")

    label = tk.Label(
        third,
        # text="🎉 Wish You Happy Birthday Balaji 🎂",
        text="🎉 wel",
        font=("Arial", 20, "bold"),
        fg="blue"
    )
    label.pack(expand=True)

    audio_file = "birthday.mp3"
    play_background_song(audio_file)

    def on_close():
        stop_background_song()
        third.destroy()

    third.protocol("WM_DELETE_WINDOW", on_close)
    third.mainloop()


# Login Window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("350x250")

tk.Label(login_window, text="User ID", font=("Arial", 12)).pack(pady=5)
entry_user = tk.Entry(login_window)
entry_user.pack()

tk.Label(login_window, text="Password", font=("Arial", 12)).pack(pady=5)
entry_pass = tk.Entry(login_window, show="*")
entry_pass.pack()

tk.Button(
    login_window,
    text="Login",
    font=("Arial", 12),
    command=login
).pack(pady=20)

login_window.mainloop()
