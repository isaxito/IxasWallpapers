import ctypes, random, nekos, requests, os, threading
from time import sleep


lista_de_tags = [ 'feet', 'yuri', 'trap', 'hololewd', 'lewdkemo', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
        'meow', 'tickle', 'lewd', 'feed', 'solo', 'anal', 'slap', 'hentai', 'erofeet',
        'keta', 'blowjob', 'pussy', 'tits', 'lizard', 'pussy_jpg', 'classic', 'kuni', 'waifu', 'pat', 'kiss',
        'neko', 'spank', 'cuddle', 'fox_girl', 'boobs',
        'smallboobs', 'hug', 'ero' ]
# Función para bajar img de url especifica, retorna el nombre completo de la imagen
def bajar_imagen(url):
    primera_p = random.randrange(1,1001)
    segunda_p = random.randrange(1,1001)
    nombre_completo = str(primera_p) + "-" + str(segunda_p) + ".jpg"
    img_data = requests.get(url).content
    with open(nombre_completo, "wb") as img:
        img.write(img_data)
        img.close()
    return nombre_completo

# Función que pone el wallpaper aleatorio de internet diferente
def cambio_fondo(direccion, tagaso):
    url = nekos.img(tagaso)
    dir_imagen = direccion + bajar_imagen(url)
    img_nombre = dir_imagen.replace(direccion,'')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, dir_imagen , 0)
    return img_nombre
    

#Start

#Leer la configuración del txt
f_config = open('config.txt', 'r')
config_string = f_config.read()
f_config.close()
# Variables de dirección y tiempo de cambio entre fondos de pantalla (en segundos)
# No estoy seguro de que sea un string asi que por las dudas va eso:
config_string = str(config_string)
# Hace una lista con strings, siendo la primera el tiempo
config_list = config_string.split("\n")

try:
    t_cambio = int(config_list[0])
except ValueError:
    print("No pusiste un numero en la configuracion.")
    print("Podes hacerlo ahora: ", end='')
    tiempin = input()
    try:
        tiempin = int(tiempin)
        t_cambio = tiempin
        f_config = open("config.txt", "w")
        f_config.write(str(tiempin))
        f_config.close()
    except ValueError:
        print("Te di varias oportunidades flaco, anda pone el tiempo en el txt ahora.")
        sleep(3)
        quit()
# Obtener dirección absoluta de la carpeta donde esta el programa
abs_dir = str(os.path.dirname(os.path.abspath(__file__))) + "\\"

# Indice de imagenes
index = 1
# Prints y loop principal
print("Hecho con la API de nekos.life por Isaquito. Lee las instrucciones si no te funca. \n", end='')
print("Tiempo actual entre cambio de imagenes: " + str(t_cambio))
delete_choice = input("Queres que las imagenes se borren? s/n: ")
# Si no ponen 's' o 'n'
while((delete_choice != 's') and (delete_choice != 'n')):
    delete_choice = ''
    delete_choice = input("s/n: ")
        
print("Lista de tags recomendados/disponibles:")
print(lista_de_tags)
tagg = input("Inserte un tag como 'feet' o 'trap': ")
tagg = tagg.lower()
if tagg in lista_de_tags:
    while True:
        print("Imagen numero " + str(index))
        nombre_img = cambio_fondo(str(abs_dir), tagg)
        index += 1
        sleep(int(t_cambio))
        if (delete_choice == 's'):
            try:
                os.remove(str(nombre_img))
            except FileNotFoundError:
                pass
else:
    print("El tag que pusiste no es de los disponibles o compatibles.")
    sleep(3)