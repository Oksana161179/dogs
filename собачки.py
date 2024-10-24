from tkinter import *
from tkinter import ttk # полосочка для загрузки
from tkinter import messagebox as mb
import requests # для того чтобы загружать из интернета изображения
from PIL import Image, ImageTk # для того чтобы обрабатывать изображения
from io import BytesIO # для того чтобы обрабатывать картинку


def get_dog_image():# создаем функцию получения изображения
    try:# обрабатываем исключения
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()# узнаем статус существует ли сайт
        data = response.json()# в дате лежит ответ от json
        return data['message']# возвращается сообщение о сайте
    except Exception as e:# обрабатываем исключения
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")

def show_image():#создаем функцию, которая будет выводить изображения
    image_url = get_dog_image()#получаем ссылку на изображение
    if image_url:#если ссылка не пустая
        try:#обрабатываем исключения
            response = requests.get(image_url, stream=True)#ответ(response) будет равен запросу(requests).
            # т.е. в ответ получаем что-то по ссылке(image_url)
            response.raise_for_status()#обрабатываем ошибки: получаем статус ответа
            img_data = BytesIO(response.content)#по ссылке загружаем изображение в двоичном коде
            # в переменную-img_data
            img_size =(int (with_spinbox.get()), int(height_spinbox.get()))
            img = Image.open(img_data)#обрабатываем в нормальную картинку
            img.thumbnail(img_size)#размер тот, который укажет пользователь
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel(window)#создаем новое окно
            new_window.title("Случайное изображение")#заголовок нового окна
            lb = ttk.Label(new_window, image=img)#создаем новую метку для нового окна(new_window).
            # параметр-image равен тому где лежит наша картинка-img
            lb.pack()
            lb.image = img#чтобы сборщик мусора не собрал картинку
        except Exception as e:#обрабатываем исключения
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")
    progress.stop()#останавливаем полосочку загрузки изображения

def prog():#создаем функцию виджета(полосочки) загрузки изображения
    progress['value'] = 0#изначальное значение-ноль
    progress.start(30)#полосочка заполняется по мере загрузки-один раз в 30 миллисекунд
    window.after(3000, show_image)#затем ждем 3000 миллисекунды и запускаем функцию-show_image

window = Tk()#создаем окно
window.title("Картинки с собачками")#задаем заголовок окну
window.geometry("360x420")#задаем размер окну

label = ttk.Label()#создаем метку на которой будут появляться картинки
label.pack(pady=10)

button = ttk.Button(text="Загрузить изображение", command=prog)#создаем кнопку и задаем команду(command).
# для загрузки изображений-prog
button.pack(pady=10)

progress = ttk.Progressbar(mode="determinate", length=300)#создаем виджет-полосочку для загрузки изображений,
# длиной=300
progress.pack(pady=10)

width_label = ttk.Label(text="Ширина:")#для ширины спинбокса создаем метку ширины
width_label.pack(side="left", padx=(10, 0))#side="left" означает, что метка будет прижата влево. padx=(10, 0) означает,
# что слева будет 10 пикселей, а справа будет ноль пикселей
with_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)#создаем спинбокс
with_spinbox.pack(side="left", padx=(0, 10))

height_label = ttk.Label(text="Высота:")#создаем метку, которая отвечает за высоту
height_label.pack(side="left", padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side="left", padx=(0, 10))


window.mainloop()
