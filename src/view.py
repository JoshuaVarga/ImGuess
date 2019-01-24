import tkinter as tk
import numpy as np
from PIL import Image, ImageTk, ImageFilter


class View(tk.Tk):
    def __init__(self):
        super().__init__()

        self.controller = None;

        self.preview = tk.Label(borderwidth="0", highlightthickness="0")
        self.button = tk.Button(self, text="Next", command=self.button_click)

        self.init_view()

    def init_view(self):
        self.title("ImGuess")
        self.geometry("640x480")
        self.resizable(0, 0)
        self.configure(bg="#303030")

        self.preview.pack()
        self.button.pack()

    def init_listeners(self, controller):
        self.controller = controller

    def button_click(self):
        image = self.controller.retrieve_image()

        self.preview.configure(image=image)
        self.preview.image = image

    def set_preview(self, image):
        self.preview.config(image=image)
        self.preview.image = image

    def set_button(self, text):
        self.button.configure(text=text)

