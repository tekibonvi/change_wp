import os
import random

folder = "/home/ezequias/Escritorio/projects/Wallpapers/"

os.chdir(folder)

image_formats = ["jpg","png","jpeg", "webp"]

list_of_images = [image for image in os.listdir() if 
image.endswith(tuple(image_formats))]
random_wpp = os.path.join(os.getcwd(),random.choice(list_of_images))
os.system("gsettings set org.gnome.desktop.background picture-uri 'file://{}'".format(random_wpp))

os.system("gsettings set org.gnome.desktop.background picture-uri-dark 'file://{}'".format(random_wpp))
