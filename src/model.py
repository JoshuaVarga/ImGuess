import tkinter as tk
from PIL import Image, ImageTk


class Model:
    def __init__(self):
        self.images = None
        self.labels = None
        self.image = None

        self.index = -1

    def initialize_image(self):
        self.image = ImageTk.PhotoImage(Image.open("default.png", "r").resize((256, 256)))

    def increment_index(self):
        self.index += 1

        return self.index

    def get_images(self):
        return self.images

    def get_labels(self):
        return self.labels

    def get_image(self):
        return self.image

    def set_images(self, images):
        self.images = images

    def set_labels(self, labels):
        self.labels = labels

    def set_image(self, image):
        self.image = image
