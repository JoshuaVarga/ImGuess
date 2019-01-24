import numpy as np
import pickle as pk
from PIL import Image, ImageTk, ImageFilter
from model import Model
from view import View


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        view.init_listeners(self)

        model.initialize_image()
        view.set_preview(model.get_image())

    def initialize_dataset(self, file):
        path = "cifar-10-batches-py/"

        with open(path + file, "rb") as batch:
            dictionary = pk.load(batch, encoding="bytes")
            batch.close()

        self.model.set_images(dictionary[b"data"])
        self.model.set_labels(dictionary[b"labels"])

    def retrieve_image(self):
        single_image = np.array(self.model.get_images()[self.model.increment_index()])
        single_image_reshaped = np.transpose(np.reshape(single_image, (3, 32, 32)), (1, 2, 0))

        photo = Image.fromarray(single_image_reshaped)
        photo = photo.resize((256, 256), Image.ANTIALIAS)
        photo = photo.filter(ImageFilter.SHARPEN)

        return ImageTk.PhotoImage(photo)

    def run(self):
        self.initialize_dataset("data_batch_1")
        self.view.mainloop()
