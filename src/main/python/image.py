import os
import platform

from pathlib import Path
from PIL import Image


class CustomImage:
    def __init__(self, path, folder=""):
        self.image = Image.open(path)
        self.format = self.image.format
        self.name = Path(path)
        self.name = self.name.stem
        self.separation = "\\" if platform.system() == "Windows" else "/"
        self.width, self.height = self.image.size
        self.path = path
        self.reduced_path = os.path.join(os.path.dirname(self.path), folder, os.path.basename(self.path))
        if folder == "":
            self.reduced_path = os.path.dirname(self.reduced_path) + self.separation + self.name + "_réduite." \
                                + self.format

    def reduce_image(self, size=0.5, quality=75):
        new_width = round(self.width * size)
        new_height = round(self.height * size)
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)
        parent_dir = os.path.dirname(self.reduced_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        self.image.save(self.reduced_path, self.format, quality=quality)
        return os.path.exists(self.reduced_path)


if __name__ == '__main__':
    custom_image = CustomImage(r"C:\Users\gab01\Pictures\Screenshots\Capture d’écran (10).png")
    custom_image.reduce_image(size=0.75, quality=50)
