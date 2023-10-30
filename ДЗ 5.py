from colorama import *
init(autoreset=True)

print(Fore.GREEN + "Hello dear student!")
print(Fore.YELLOW +"Bye Bye!")
print(Style.BRIGHT + Fore.BLUE + "LOL")

import colorama



colorama_attributes = dir(colorama)

for attribute in colorama_attributes:
    print(attribute)


print("init(autoreset=False): Этот метод используется для инициализации Colorama.autoreset управляет автоматическим сбросом цвета после его применения к тексту."
"Fore: Это класс который содержит цветовые константы для (текста). Например, Fore.YELLOW представляет желтенький цвет текста. Back: Это класс, который содержит цветовые константы для заднего плана (фона)."
 " Например, Back.BLUE представляет синий фон.Style: Это класс, который содержит стили для текста, такие как жирный (Style.BRIGHT) или подчеркнутый"
" (Style.UNDERLINE) init() и deinit)")
print("Учитель если вы хотите сами проверить colorama то уберите текст с 18-22 строку!")




