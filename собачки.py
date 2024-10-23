from cProfile import label
from tkinter import *
import requests #для того чтобы загружать из интернета изображения
from PIL import Image, ImageTk #для того чтобы обрабатывать изображения
from io import BytesIO #для того чтобы обрабатывать картинку

from выводим_список_папок_в_консоль import window

window = Tk()#создаем окно
window.title("Картинки с собачками")#задаем заголовок окну
window.geometry("360x420")#задаем размер окну

label = Label()#создаем метку на которой будут появляться картинки
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)#создаем кнопку и задаем команду(command)
# для загрузки изображений-show_image
button.pack(pady=10)

window.mainloop()
