# Nombre del programa: Bienestar GT
# Descripción:Programa que proporciona información clara y accesible sobre hábitos saludables, prevención de enfermedades
# y cuidado personal a través de una aplicación móvil.
# Autor(es): ♥ David Miranda ♥ y derivados; Dulce Ambrosio, Javier Linares, Marcos Ambrocio, Gadiel Ocaña.
# Fecha de creación: 25-05-2023
# Última fecha de modificación: 9-05-2023
# Entradas: Información sobre hábitos saludables, prevención de enfermedades y cuidado personal.
# Salidas: Información clara y accesible sobre hábitos saludables, prevención de enfermedades y cuidado personal.
# Restricciones: No especificado N/A.
# Criterios de compatibilidad: No especificado N/A

# Librerías
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
#import pandas as pd
global busqueda_entry
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
global imagen_fondo
# import cv2
import imageio
from PIL import Image, ImageTk
import webbrowser
global DIETASALUDABLE1
import random

# crear la ventana
ventana = tk.Tk()
ventana.title("♥ Bienestar GT by JAMT COMPANY ♥")
ventana.geometry("700x500")
ventana.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
ventana.protocol("WM_DELETE_WINDOW", lambda: None)
# crear un lienzo en la parte izquierda
lienzo = tk.Canvas(ventana, width=500, height=500)
lienzo.pack(side="left")
# cargar imagen en el lienzo
imagen = Image.open("Bienestar GT.jpg")
# imagen = imagen.resize((500, 500), Image.ANTIALIAS)
imagen = imagen.resize((500, 500), Image.LANCZOS)
imagen_render = ImageTk.PhotoImage(imagen)
lienzo.create_image(0, 0, image=imagen_render, anchor="nw")

#▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
#▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
# Agregar caja de texto y botón de búsqueda
# Creamos un diccionario vacío
enfermedades = {}
# agregamos informacion 
enfermedades["1"] = "Enfermedad coronaria: Una enfermedad que afecta al corazón y los vasos sanguíneos, y que puede causar ataques cardíacos y otros problemas cardíacos graves."
enfermedades["2"] = "Accidente cerebrovascular: Una enfermedad en la que se produce una interrupción del flujo sanguíneo al cerebro, lo que puede    causar daño cerebral permanente o incluso la muerte."
enfermedades["3"] = "Enfermedad pulmonar obstructiva crónica (EPOC): Una enfermedad que causa dificultad para respirar y se asocia con una serie de problemas pulmonares crónicos, incluyendo enfisema y bronquitis crónica."
enfermedades["4"] = "Influenza (gripe): Una enfermedad viral que puede causar síntomas leves a graves, y en casos graves, puede resultar          en la muerte."
enfermedades["5"] = "Diabetes: Una enfermedad crónica en la que el cuerpo no produce suficiente insulina o no la usa eficazmente,    lo que puede causar niveles elevados de azúcar en la sangre y dañar los órganos y los tejidos."
enfermedades["6"] = "Tuberculosis: Una enfermedad infecciosa causada por una bacteria que afecta principalmente a los pulmones, pero    también puede afectar otros órganos."
enfermedades["7"] = "VIH/SIDA: Una enfermedad infecciosa causada por el virus de la inmunodeficiencia humana (VIH) que debilita el sistema inmunológico del cuerpo y puede llevar a una variedad de enfermedades y a la muerte."
enfermedades["8"] = "Hepatitis B: Una enfermedad viral que afecta el hígado y puede causar una variedad de problemas de salud,        incluyendo cáncer de hígado y cirrosis."
enfermedades["9"] = "Cáncer de pulmón: Un tipo de cáncer que se origina en los pulmones y puede ser causado por factores como el tabaquismo y la exposición a sustancias químicas tóxicas."
enfermedades["10"] = "Neumonía: Una infección que afecta los pulmones y que puede ser causada por una variedad de virus, bacterias y otros organismos."
enfermedades["11"] = "Enfermedad renal crónica: Una enfermedad en la que los riñones pierden gradualmente su capacidad para filtrar la sangre y     eliminar los desechos del cuerpo."
enfermedades["12"] = "Enfermedades cardíacas congénitas: Un grupo de trastornos que afectan la estructura y la función del corazón desde el nacimiento, y que pueden ser causados por factores genéticos o ambientales."
enfermedades["13"] = "Malnutrición: Una enfermedad causada por una dieta deficiente que puede llevar a una variedad de problemas de     salud, incluyendo la desnutrición y el retraso del crecimiento."
enfermedades["14"] = "Esquizofrenia: Una enfermedad mental grave que afecta la forma en que una persona piensa, siente y se comporta, y    que puede afectar su capacidad para llevar una vida normal."
enfermedades["15"] = "Artritis reumatoide: Una enfermedad autoinmunitaria que causa dolor, inflamación y daño en las articulaciones, y que     puede limitar la capacidad de una persona para realizar actividades cotidianas."
# enfermedades[""] = ""
prevencion = {}
prevencion["1"] = "Enfermedad coronaria: Mantener una dieta saludable, hacer ejercicio regularmente, controlar la presión arterial y el colesterol, dejar de fumar y controlar el estrés pueden ayudar a prevenir la enfermedad coronaria. Si se diagnostica la enfermedad, es posible que se necesiten medicamentos y cambios en el estilo de vida para controlarla."
prevencion["2"] = "Accidente cerebrovascular: Mantener una dieta saludable, hacer ejercicio regularmente, controlar la presión arterial y el colesterol, y evitar el tabaquismo pueden ayudar a prevenir un accidente cerebrovascular. Si se sospecha un accidente cerebrovascular, es importante buscar atención médica de inmediato."
prevencion["3"] = "Enfermedad pulmonar obstructiva crónica (EPOC): Dejar de fumar y evitar la exposición al humo de segunda mano y a otros contaminantes del aire pueden ayudar a prevenir la EPOC. Si se diagnostica EPOC, es posible que se necesiten medicamentos y cambios en el estilo de vida para controlarla."
prevencion["4"] = "Influenza (gripe): La mejor manera de prevenir la gripe es vacunarse todos los años. También es importante lavarse las manos con frecuencia, evitar tocarse la cara y cubrirse la boca y la nariz al toser o estornudar."
prevencion["5"] = "Diabetes: Mantener una dieta saludable, hacer ejercicio regularmente, controlar los niveles de azúcar en la sangre y tomar medicamentos según las indicaciones pueden ayudar a controlar la diabetes. También es importante hacerse chequeos regulares con un médico."
prevencion["6"] = "Tuberculosis: La mejor manera de prevenir la tuberculosis es vacunarse si se encuentra en una población de alto riesgo y evitar el contacto con personas enfermas. Si se diagnostica tuberculosis, es importante seguir el tratamiento prescrito por un médico y tomar todas las medicinas según las indicaciones."
prevencion["7"] = "VIH/SIDA: La prevención del VIH implica tomar medidas para reducir el riesgo de exposición al virus, como usar preservativos durante las relaciones sexuales y no compartir agujas o jeringas. Si se diagnostica VIH, es posible que se necesiten medicamentos antirretrovirales para controlar la enfermedad."
prevencion["8"] = "Hepatitis B: La vacunación es la mejor manera de prevenir la hepatitis B. También es importante evitar el contacto con sangre y líquidos corporales de otras personas, y utilizar preservativos durante las relaciones sexuales."
prevencion["9"] = "Cáncer de pulmón: Dejar de fumar y evitar la exposición al humo de segunda mano y a otros contaminantes del aire pueden ayudar a prevenir el cáncer de pulmón. Si se diagnostica cáncer de pulmón, es posible que se necesiten tratamiento como cirugía, radioterapia y quimioterapia."
prevencion["10"] = "Neumonía: La vacunación es la mejor manera de prevenir algunas formas de neumonía. También es importante lavarse las manos con frecuencia, evitar tocarse la cara y cubrirse la boca y la nariz al toser o estornudar."
prevencion["11"] = "Enfermedad renal crónica: Para prevenir la enfermedad renal crónica, se recomienda mantener una dieta saludable y equilibrada, beber suficiente agua, hacer ejercicio regularmente, evitar el consumo de tabaco y limitar el consumo de alcohol. Si se ha diagnosticado la enfermedad renal crónica, es importante seguir las recomendaciones del médico en cuanto a la dieta, el tratamiento y el monitoreo regular de la función renal."
prevencion["12"] = "Enfermedades cardíacas congénitas: La prevención de las enfermedades cardíacas congénitas puede ser difícil ya que la mayoría de los casos son causados por factores genéticos. Sin embargo, existen medidas que pueden ayudar a reducir el riesgo de problemas cardíacos, como llevar una vida saludable, evitar el consumo de tabaco y alcohol durante el embarazo y hacerse pruebas genéticas si hay antecedentes familiares de enfermedades cardíacas congénitas. Si se ha diagnosticado una enfermedad cardíaca congénita, es importante seguir las recomendaciones del médico en cuanto al tratamiento, la monitorización regular y las medidas preventivas adicionales, como la toma de antibióticos antes de ciertos procedimientos dentales o médicos."
prevencion["13"] = "Malnutrición: Para prevenir la malnutrición, es importante llevar una dieta equilibrada y saludable, rica en frutas, verduras, proteínas y carbohidratos complejos. Si se sospecha de malnutrición, se debe buscar atención médica para evaluar la causa y recibir tratamiento adecuado, que puede incluir cambios en la dieta y suplementos nutricionales."
prevencion["14"] = "Esquizofrenia: La esquizofrenia es una enfermedad mental grave que requiere tratamiento médico especializado y a largo plazo. Es importante buscar ayuda médica si se sospecha de esquizofrenia o si se experimentan síntomas como alucinaciones, delirios o problemas de pensamiento y comportamiento. El tratamiento puede incluir terapia, medicación y apoyo de la familia y amigos cercanos."
prevencion["15"] = "Artritis reumatoide: Para prevenir la artritis reumatoide, se recomienda mantener un estilo de vida saludable, hacer ejercicio regularmente, mantener un peso saludable y evitar el consumo de tabaco. Si se ha diagnosticado artritis reumatoide, es importante seguir las recomendaciones del médico en cuanto al tratamiento y la gestión de los síntomas, que puede incluir medicamentos, terapia física y ocupacional, y apoyo emocional."
# prevencion[""] = ""

mensaje_error = tk.Label(ventana, fg="red")
mensaje_error.pack()
imagen_fondo = None

# Función para buscar una enfermedad
def buscar_enfermedad():
    # Obtener la palabra clave ingresada por el usuario
    palabra_clave = busqueda_entry.get()

    # Verificar si la palabra clave está en la lista de enfermedades
    if palabra_clave in enfermedades:
        # Mostrar la información correspondiente en una nueva ventana
        ventana_enfermedad = tk.Toplevel(ventana)
        ventana_enfermedad.title("Información de {}".format(palabra_clave))
        ventana_enfermedad.geometry("500x400")

        # Cargar la imagen de fondo
        global imagen_fondo
#         imagen_fondo = ImageTk.PhotoImage(Image.open("C:\\Users\\famil\\Desktop\\PROGRA\\saludapp231260\\imagen_fondo.png"))
        imagen_fondo = ImageTk.PhotoImage(Image.open("imagen_fondo.png"))
        fondo = tk.Label(ventana_enfermedad, image=imagen_fondo)
        fondo.place(x=0, y=0)

        texto_enfermedad = tk.Text(ventana_enfermedad, height=15, width=60)
        texto_enfermedad.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        texto_enfermedad.insert(tk.END, enfermedades[palabra_clave])
        mensaje_error.config(text="")
    else:
        mensaje_error.config(text="Ingrese una palabra clave válida")

# Función para buscar una prevención
def buscar_prevencion():
    # Obtener la palabra clave ingresada por el usuario
    palabra_clave = busqueda_entry.get()

    # Verificar si la palabra clave está en el diccionario de prevención
    if palabra_clave in prevencion:
        # Mostrar la información correspondiente en una nueva ventana
        ventana_prevencion = tk.Toplevel(ventana)
        ventana_prevencion.title("Prevención de {}".format(palabra_clave))
        ventana_prevencion.geometry("500x400")

        # Cargar la imagen de fondo
        global imagen_fondo
#         imagen_fondo = ImageTk.PhotoImage(Image.open("C:\\Users\\famil\\Desktop\\PROGRA\\saludapp231260\\imagen_fondo.png"))
        imagen = tk.PhotoImage(file="imagen_fondo.png")
        fondo = tk.Label(ventana_prevencion, image=imagen_fondo)
        fondo.place(x=0, y=0)

        texto_prevencion = tk.Text(ventana_prevencion, height=15, width=60)
        texto_prevencion.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        texto_prevencion.insert(tk.END, prevencion[palabra_clave])
        mensaje_error.config(text="")
    else:
        mensaje_error.config(text="Ingrese una palabra clave válida")
# Agregar caja de texto y botón de búsqueda
busqueda_frame = tk.Frame(ventana, bg="#9e2626", width=50, height=50)
busqueda_frame.place(x=0, y=385)
busqueda_label = tk.Label(busqueda_frame, text="Palabra Clave:", font=("Arial", 15, "italic"))
busqueda_label.pack(side="left", padx=5)
busqueda_entry = tk.Entry(busqueda_frame, width=30)
busqueda_entry.pack(side="left", padx=5)
busqueda_entry.config(width=15, font=('Arial', 10, "italic"))
# Agregar botón de búsqueda
boton_buscar = tk.Button(busqueda_frame, text="Buscar", command=buscar_enfermedad)
boton_buscar.pack(side="left", padx=5)
# Agregar botón de prevención
boton_prevencion = tk.Button(busqueda_frame, text="Prevención", command=buscar_prevencion)
boton_prevencion.pack(side="left", padx=10)


# el def de salir
def salir():
    if messagebox.askyesno("Salir", "¿Desea salir de la aplicación?"):
        ventana.destroy()
        ventana.quit()
#▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
#▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
# crear el marco para el menú
menu_frame = tk.Frame(ventana, bg="#9e2626", width=200)
menu_frame.pack(side="right", fill="y")
# agregar opciones al menú
opcion1 = tk.Button(menu_frame, text=" ♠ Descripción del Programa ♠ ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion1.pack(padx=10, pady=10)
opcion1.config(bg='gray')
opcion4 = tk.Button(menu_frame, text="✨ Palabras Clave ✨", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion4.pack(padx=10, pady=10)
opcion4.config(bg='gray')
opcion3 = tk.Button(menu_frame, text=" ⚠ ¡Ayuda! ⚠ ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion3.pack(padx=10, pady=10)
opcion3.config(bg='gray')
opcion2 = tk.Button(menu_frame, text=" ✨ Ejercicios ✨  ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion2.pack(padx=10, pady=10)
opcion2.config(bg='gray')
opcion5 = tk.Button(menu_frame, text="✨ Dieta Saludable ✨", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion5.pack(padx=10, pady=10)
opcion5.config(bg='gray')
opcion6 = tk.Button(menu_frame, text="✨ Consejos Diarios ✨", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion6.pack(padx=10, pady=10)
opcion6.config(bg='gray')
opcion7 = tk.Button(menu_frame, text=" ⚠ Salir ⚠ ", font=("Arial", 10, "italic"), padx=20, pady=10, command=salir)
opcion7.pack(padx=10, pady=10)
opcion7.config(bg='gray')
# opcion8 = tk.Button(menu_frame, text="Resumen Diario", font=("Aria", 10, "italic"), padx=20, pady=10)
# opcion8.pack(padx=10, pady=10)
# opcion8.config(bg='gray')
# agregar el contenido principal
# contenido = tk.Label(ventana, text="♥ Bienestar GT ♥", font=("Arial", 20, "italic"))
# contenido.pack()

def cambiar_ventana():
    # Crear nueva ventana
    nueva_ventana = tk.Toplevel()
#     nueva_ventana.overrideredirect(True)
    nueva_ventana.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana.protocol("WM_DELETE_WINDOW", lambda: None)


    # Configurar nueva ventana
    nueva_ventana.title("♥ Descripción del Programa ♥")
    nueva_ventana.geometry("500x500")

    # Agregar imagen y texto a la nueva ventana
    imagen = tk.PhotoImage(file="DescripcionAPP.png")
    imagen_label = tk.Label(nueva_ventana, image=imagen)
    imagen_label.pack()
    texto_label = tk.Label(nueva_ventana, text="Descripción del programa <3 ")
    texto_label.pack()

    # Agregar botón para volver a la ventana anterior
#     volver_boton = tk.Button(nueva_ventana, text="Volver", command=nueva_ventana.destroy)
#     volver_boton.pack()
    volver_boton = tk.Button(nueva_ventana, text="Volver", command=nueva_ventana.destroy)
    volver_boton.place(x=230, y=470)

    # Ocultar ventana actual
    ventana_principal.withdraw()
    
opcion1.config(command=cambiar_ventana)

def cambiar_ventana1():
    # Crear nueva ventana
    nueva_ventana1 = tk.Toplevel()
#     nueva_ventana.overrideredirect(True)
    nueva_ventana1.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana1.protocol("WM_DELETE_WINDOW", lambda: None)


    # Configurar nueva ventana
    nueva_ventana1.title("♥ Palabras Clave ♥")
    nueva_ventana1.geometry("500x500")

    # Agregar imagen y texto a la nueva ventana
    imagen = tk.PhotoImage(file="PalabrasClave.png")
    imagen_label = tk.Label(nueva_ventana1, image=imagen)
    imagen_label.pack()
    texto_label = tk.Label(nueva_ventana1, text="Palabras Clave <3 ")
    texto_label.pack()

    # Agregar botón para volver a la ventana anterior
#     volver_boton = tk.Button(nueva_ventana, text="Volver", command=nueva_ventana.destroy)
#     volver_boton.pack()
    volver_boton2 = tk.Button(nueva_ventana1, text="Volver", command=nueva_ventana1.destroy)
    volver_boton2.place(x=230, y=470)

    # Ocultar ventana actual
    ventana_principal.withdraw()

opcion4.config(command=cambiar_ventana1)


def cambiar_ventana2(ventana_principal):
    # Crear nueva ventana
    nueva_ventana2 = tk.Toplevel()
    nueva_ventana2.protocol("WM_DELETE_WINDOW", lambda: None)
    # Configurar nueva ventana
    nueva_ventana2.title(" ✨ Ejercicios en Casa ✨ ")
    nueva_ventana2.geometry("500x500")
    # Agregar texto a la nueva ventana
    texto_label = tk.Label(nueva_ventana2, text="Ejercicios <3 ")
    texto_label.pack()
    # Agregar botón para volver a la ventana anterior
    volver_boton3 = tk.Button(nueva_ventana2, text="Volver", command=nueva_ventana2.destroy)
    volver_boton3.place(x=230, y=470)
    # Ocultar ventana actual
    ventana.withdraw()
    # Mostrar video en un cuadro
    video_path = "Mazda Vision Coupe.mp4" # nombrar el video debe estar en la misma carpeta del py appfinal 
    video_reader = imageio.get_reader(video_path)
    fps = video_reader.get_meta_data()['fps']
    for frame in video_reader:
        # Convertir el marco a una imagen de la biblioteca PIL
        image = Image.fromarray(frame)
        # Redimensionar la imagen a 480x360
        image = image.resize((480, 360), Image.ANTIALIAS)
        # Crear objeto de imagen tkinter desde la imagen PIL
        photo = ImageTk.PhotoImage(image)
        # Crear etiqueta de imagen tkinter y mostrar la imagen
        video_label = tk.Label(nueva_ventana2, image=photo)
        video_label.image = photo
        video_label.pack()
        nueva_ventana2.update()
        # Esperar el tiempo adecuado antes de mostrar el siguiente fotograma
        nueva_ventana2.after(int(1000/fps), lambda: None)
    video_reader.close()

# opcion2.config(command=cambiar_ventana2)


estilo_boton = {'font': ('Arial', 16, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 10,
                'height': 2}
estilo_boton1 = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 9,
                'height': 1}
estilo_boton2 = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 15,
                'height': 1}
estilo_boton3 = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 29,
                'height': 1}
# Definir la función que se ejecutará cuando se presione el botón
def push_ups():
    webbrowser.open('https://www.fitliferegime.com/push-up-for-beginners/')
def squats():
    webbrowser.open('https://www.fitliferegime.com/best-bodyweight-leg-exercises-that-you-can-do-anywhere/')
def plank():
    webbrowser.open('https://www.fitliferegime.com/10-easy-core-strengthening-exercises-for-beginners/')
def Hip_Thrust():
    webbrowser.open('https://www.fitliferegime.com/best-bodyweight-leg-exercises-that-you-can-do-anywhere/')
def fondosenbanca():
    webbrowser.open('https://www.fitliferegime.com/scapula-dip-how-to-do-muscles-worked-benefits/')
def RetenciónHueca():
    webbrowser.open('https://www.fitliferegime.com/10-easy-core-strengthening-exercises-for-beginners/')
def CrunchInverso():
    webbrowser.open('https://www.fitliferegime.com/10-easy-core-strengthening-exercises-for-beginners/')
def RodillasAltas():
    webbrowser.open('https://www.fitliferegime.com/10-easy-core-strengthening-exercises-for-beginners/')
def LevantamientoDePantorrilla():
    webbrowser.open('https://www.fitliferegime.com/bodyweight-calf-raise-to-build-mass-and-strength-of-calves/')
    
def cambiar_ventanaayuda():
    # Crear nueva ventana
    nueva_ventana2 = tk.Toplevel()
#     nueva_ventana.overrideredirect(True)
    nueva_ventana2.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana2.protocol("WM_DELETE_WINDOW", lambda: None)
    # Configurar nueva ventana
    nueva_ventana2.title("✨ Ejercicios ✨")
    nueva_ventana2.geometry("1200x600")

    # Agregar imagen y texto a la nueva ventana
    imagen = tk.PhotoImage(file="EJERCICIO.png")
    imagen_label = tk.Label(nueva_ventana2, image=imagen)
    imagen_label.pack()
    texto_label = tk.Label(nueva_ventana2, text=" ✨ Ejercicios ✨ ")
    texto_label.pack()
    volver_boton3 = tk.Button(nueva_ventana2, text="Volver", command=nueva_ventana2.destroy, **estilo_boton)
    volver_boton3.place(x=30, y=10)
    volver_boton4 = tk.Button(nueva_ventana2, text="Push Ups", **estilo_boton1, command=push_ups)
    volver_boton4.place(x=100, y=225)
    volver_boton5 = tk.Button(nueva_ventana2, text="Squats", **estilo_boton1, command=squats)
    volver_boton5.place(x=180, y=340)
    volver_boton6 = tk.Button(nueva_ventana2, text="Plank", **estilo_boton1, command=plank)
    volver_boton6.place(x=460, y=115)
    volver_boton7 = tk.Button(nueva_ventana2, text="Hip Thrust", **estilo_boton1, command=Hip_Thrust)
    volver_boton7.place(x=290, y=432)
    volver_boton8 = tk.Button(nueva_ventana2, text="Fondos en Banca", **estilo_boton2, command=fondosenbanca)
    volver_boton8.place(x=605, y=95)
    volver_boton9 = tk.Button(nueva_ventana2, text="Retención Hueca", **estilo_boton2, command=RetenciónHueca)
    volver_boton9.place(x=600, y=445)
    volver_boton10 = tk.Button(nueva_ventana2, text="Crunch Inverso", **estilo_boton2, command=CrunchInverso)
    volver_boton10.place(x=1050, y=100)
    volver_boton11 = tk.Button(nueva_ventana2, text="Rodillas Altas", **estilo_boton2, command=RodillasAltas)
    volver_boton11.place(x=990, y=470)
    volver_boton12 = tk.Button(nueva_ventana2, text="Levantamiento De Pantorrilla", **estilo_boton3, command=LevantamientoDePantorrilla)
    volver_boton12.place(x=950, y=310)
    
    # Agregar botón para volver a la ventana anterior
#     volver_boton3 = tk.Button(nueva_ventana3, text="Volver", font=("Arial", 20, "italic"), command=nueva_ventana3.destroy)
#     volver_boton3.place(x=120, y=100)


    # Ocultar ventana actual
    ventana_principal.withdraw()

opcion2.config(command=cambiar_ventanaayuda)

#-----------------------------------------------------------------------------------------------------
estilo_botonvtnayuda = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 10,
                'height': 3}

def cambiar_ventanaayuda():
    # Crear nueva ventana
    nueva_ventana3 = tk.Toplevel()
#     nueva_ventana.overrideredirect(True)
    nueva_ventana3.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana3.protocol("WM_DELETE_WINDOW", lambda: None)
    # Configurar nueva ventana
    nueva_ventana3.title("⚠ ¡Ayuda! ⚠")
    nueva_ventana3.geometry("1100x600")

    # Agregar imagen y texto a la nueva ventana
    imagen = tk.PhotoImage(file="AYUDA.png")
    imagen_label = tk.Label(nueva_ventana3, image=imagen)
    imagen_label.pack()
    texto_label = tk.Label(nueva_ventana3, text=" ⚠ ¡Ayuda! ⚠ ")
    texto_label.pack()
    volver_boton3 = tk.Button(nueva_ventana3, text="Volver", command=nueva_ventana3.destroy, **estilo_botonvtnayuda)
    volver_boton3.place(x=10, y=30)
    # Agregar botón para volver a la ventana anterior
#     volver_boton3 = tk.Button(nueva_ventana3, text="Volver", font=("Arial", 20, "italic"), command=nueva_ventana3.destroy)
#     volver_boton3.place(x=120, y=100)
    # Ocultar ventana actual
    ventana_principal.withdraw()
opcion3.config(command=cambiar_ventanaayuda)


#-----------------------------------------------------------------------------------------------------
# DIETA SALUDABLE
estilo_boton4 = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 20,
                'height': 1}
# boton_buscar = tk.Button(busqueda_frame, text="Buscar", command=buscar_enfermedad)
# boton_buscar.pack(side="left", padx=5)
# volver_boton12 = tk.Button(nueva_ventana2, text="Levantamiento De Pantorrilla", **estilo_boton3, command=LevantamientoDePantorrilla)
# volver_boton12.place(x=950, y=310)
estilo_botonrd = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 15,
                'height': 1}
boton_xd = tk.Button(ventana, text="Resumen Diario", **estilo_botonrd) 
boton_xd.place(x=10, y=460)


# def abrir_ventana_grupos(ventana_padre):
#     # Crear nueva ventana
#     nueva_ventana5 = tk.Toplevel(ventana_padre)
#     nueva_ventana5.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
#     nueva_ventana5.protocol("WM_DELETE_WINDOW", lambda: None)
#     # Configurar nueva ventana
#     nueva_ventana5.title("♥ Grupos Alimenticios ♥")
#     nueva_ventana5.geometry("500x500")
#     imagen = tk.PhotoImage(file="GRUPOSALIMENTICIOS1.png")
#     imagen_label = tk.Label(nueva_ventana5, image=imagen)
#     imagen_label.pack()
#     
#     # Agregar texto a la nueva ventana
#     texto_label = tk.Label(nueva_ventana5, text="Aquí iría el contenido de la ventana Grupos Alimenticios")
#     texto_label.pack()
#         # Agregar botón para volver a la ventana anterior
#     volver_boton5 = tk.Button(nueva_ventana5, text="Volver", command=nueva_ventana5.destroy, **estilo_boton5)
#     volver_boton5.place(x=200, y=300)
# def abrir_ventana_grupos():
#     # Crear nueva ventana
#     nueva_ventana5 = tk.Toplevel()
#     nueva_ventana5.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
#     nueva_ventana5.protocol("WM_DELETE_WINDOW", lambda: None)
#     # Configurar nueva ventana
#     nueva_ventana5.title("♥ Grupos Alimenticios ♥")
#     nueva_ventana5.geometry("500x500")
#     imagen = tk.PhotoImage(file="GRUPOSALIMENTICIOS1.png")
#     imagen_label = tk.Label(nueva_ventana5, image=imagen)
#     imagen_label.pack()
#     
#     # Agregar texto a la nueva ventana
#     texto_label = tk.Label(nueva_ventana5, text="Aquí iría el contenido de la ventana Grupos Alimenticios")
#     texto_label.pack()
#         # Agregar botón para volver a la ventana anterior
#     volver_boton5 = tk.Button(nueva_ventana5, text="Volver", command=nueva_ventana5.destroy, **estilo_boton5)
#     volver_boton5.place(x=100, y=300)
#     volver_boton6 = tk.Button(nueva_ventana5, text="Alimentos Ambos Origenes")
#     volver_boton6.place(x=100, y=400)
    
def ambos():
    nueva_ventanaambos = tk.Toplevel()
    nueva_ventanaambos.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanaambos.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventanaambos.title("Ambos grupos")
    nueva_ventanaambos.geometry("1100x600")
    try:
        imagen_path = os.path.join(os.path.dirname(__file__), "GRUPOSALIMENTICIOS3.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((1100, 600), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanaambos, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
    volver_boton5 = tk.Button(nueva_ventanaambos, text="Volver", **estilo_botonsg2, command=nueva_ventanaambos.destroy)
    volver_boton5.place(x=10, y=90)
estilo_botonsg2 = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 10,
                'height': 1}
estilo_botonsg = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 10,
                'height': 1}
def sietegrupos():
    nueva_ventanasiete = tk.Toplevel()
    nueva_ventanasiete.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanasiete.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventanasiete.title("Ambos grupos")
    nueva_ventanasiete.geometry("1100x600")
    try:
        imagen_path = os.path.join(os.path.dirname(__file__), "GRUPOSALIMENTICIOS2.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((1100, 600), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanasiete, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
    volver_boton5 = tk.Button(nueva_ventanasiete, text="Volver", **estilo_botonsg, command=nueva_ventanasiete.destroy)
    volver_boton5.place(x=0, y=80)

estilo_botongrupos = {'font': ('Arial', 10, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 20,
                'height': 2}
estilo_botongrupos1 = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 10,
                'height': 1}  

def abrir_ventana_grupos():
    # Crear nueva ventana
    nueva_ventana5 = tk.Toplevel()
    nueva_ventana5.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana5.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventana5.title("Grupos Alimenticios")
    nueva_ventana5.geometry("500x500")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "GRUPOSALIMENTICIOS1.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((500, 500), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventana5, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
        
    texto_label = tk.Label(nueva_ventana5, text="Grupos Alimenticios")
    texto_label.pack()
    volver_boton5 = tk.Button(nueva_ventana5, text="Volver", **estilo_botongrupos1, command=nueva_ventana5.destroy)
    volver_boton5.place(x=10, y=400)
    volver_boton6 = tk.Button(nueva_ventana5, text="Alimentos Ambos Origenes", **estilo_botongrupos, command=ambos)
    volver_boton6.place(x=145, y=400)
    volver_boton7 = tk.Button(nueva_ventana5, text="Los 7 grupos alimenticios", **estilo_botongrupos, command=sietegrupos)
    volver_boton7.place(x=320, y=400)

def abrir_hidratacion():
    # Crear nueva ventana
    nueva_ventanah = tk.Toplevel()
    nueva_ventanah.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanah.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventanah.title("♥ Recomendaciones sobre Hidratacion ♥")
    nueva_ventanah.geometry("800x600")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "HIDRATACION.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((800, 600), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanah, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
        
    texto_label = tk.Label(nueva_ventanah, text="Grupos Alimenticios")
    texto_label.pack()
    volver_boton5 = tk.Button(nueva_ventanah, text="Volver", **estilo_botongrupos1, command=nueva_ventanah.destroy)
    volver_boton5.place(x=100, y=500)

def abrir_alimentosprocesados():
    # Crear nueva ventana
    nueva_ventanaap = tk.Toplevel()
    nueva_ventanaap.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanaap.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventanaap.title("♥ Alimentos Procesados ♥")
    nueva_ventanaap.geometry("800x600")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "ALIMENTOSPROCESADOS.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((800, 600), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanaap, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
        
    texto_label = tk.Label(nueva_ventanaap, text="Alimentos Procesados")
    texto_label.pack()
    volver_boton5 = tk.Button(nueva_ventanaap, text="Volver", **estilo_botongrupos1, command=nueva_ventanaap.destroy)
    volver_boton5.place(x=600, y=15)
estilo_botonne = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 5,
                'height': 1}  
def nutrientesesenciales():
    # Crear nueva ventana
    nueva_ventanaNE= tk.Toplevel()
    nueva_ventanaNE.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanaNE.protocol("WM_DELETE_WINDOW", lambda: None)
    nueva_ventanaNE.title("♥ Informacion sobre Nutrientes Esenciales ♥")
    nueva_ventanaNE.geometry("1100x600")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "NUTRIENTES.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((1100, 600), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanaNE, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
        
    texto_label = tk.Label(nueva_ventanaNE, text="nueva_ventanaNE")
    texto_label.pack()
    volver_boton5 = tk.Button(nueva_ventanaNE, text="Volver", **estilo_botonne, command=nueva_ventanaNE.destroy)
    volver_boton5.place(x=622, y=0)
    
def cambiar_ventanadieta(ventana_principal):
    # Crear nueva ventana
    nueva_ventana4 = tk.Toplevel(ventana_principal)
    nueva_ventana4.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana4.protocol("WM_DELETE_WINDOW", lambda: None)
    # Configurar nueva ventana
    nueva_ventana4.title("✨ Dieta Saludable ✨")
    nueva_ventana4.geometry("500x500")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "DIETASALUDABLE.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((500, 500), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventana4, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
        
    texto_label = tk.Label(nueva_ventana4, text="✨ Dieta Saludable ✨")
    texto_label.pack()
    volver_boton4 = tk.Button(nueva_ventana4, text="Volver", **estilo_boton5, command=nueva_ventana4.destroy)
    volver_boton4.place(x=40, y=400)
#     btn1 = tk.Button(nueva_ventana4, text="Grupos Alimenticios", **estilo_boton5, command=lambda: abrir_ventana_grupos(nueva_ventana4))
#     btn1 = tk.Button(nueva_ventana4, text="Grupos Alimenticios", **estilo_boton5, command=abrir_ventana_grupos)
    btn1 = tk.Button(nueva_ventana4, text="Grupos Alimenticios", **estilo_boton5, command=abrir_ventana_grupos)
    btn1.place(x=40, y=350)
    btn2 = tk.Button(nueva_ventana4, text="Hidratación", **estilo_boton5, command=abrir_hidratacion)
    btn2.place(x=40, y=300)
    btn3 = tk.Button(nueva_ventana4, text="Alimentos procesados", **estilo_boton5, command=abrir_alimentosprocesados)
    btn3.place(x=40, y=250)
    btn4 = tk.Button(nueva_ventana4, text="Nutrientes Esenciales", **estilo_boton5, command=nutrientesesenciales)
    btn4.place(x=40, y=200)
    # Ocultar ventana actual
    ventana_principal.withdraw()

estilo_boton5 = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 20,
                'height': 1}
    
opcion5.config(command=lambda: cambiar_ventanadieta(tk.Toplevel()))

FrasesMotivadoras = {
    "No te rindas, cada fracaso es una oportunidad para empezar de nuevo con más experiencia.",
    "Lo que te hace diferente es lo que te hace hermoso.",
    "A veces el éxito no es más que levantarse una vez más que caíste.",
    "No hay atajos para cualquier lugar que valga la pena llegar.",
    "La felicidad no es algo que encuentres, es algo que creas.",
    "La motivación te lleva a empezar, el hábito te lleva a continuar.",
    "No esperes oportunidades, créalas.",
    "Cada día es una nueva oportunidad para ser la mejor versión de ti mismo.",
    "El fracaso es un evento, no una persona.",
    "Si no te gustan las cosas que suceden en tu vida, entonces crea nuevas cosas para que sucedan.",
    "Tu única limitación es la que te pones a ti mismo.",
    "No hay nada más poderoso que una mente positiva y un corazón agradecido.",
    "Haz lo que puedas, con lo que tienes, donde estás.",
    "El éxito no es final, el fracaso no es fatal, es el coraje de seguir lo que cuenta.",
    "La vida es un 10% lo que te sucede y un 90% cómo reaccionas a ello.",
    "El fracaso es solo una oportunidad para comenzar de nuevo, esta vez de forma más inteligente. - Henry Ford",
    "Cada día es una oportunidad para ser mejor de lo que fuiste ayer. - Anónimo",
    "Si buscas resultados diferentes, no hagas siempre lo mismo. - Albert Einstein",
    "No esperes a que las oportunidades lleguen a ti, sal ahí y créalas tú mismo. - Sonia Sotomayor",
    "No importa cuántas veces fracases, debes seguir adelante. Esto es lo que te llevará al éxito. - Ellen DeGeneres",
    "La clave del éxito es la perseverancia. - Harold Augenbraum",
    "La disciplina es el puente entre metas y logros. - Jim Rohn",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que estás haciendo, tendrás éxito. - Albert Schweitzer",
    "La confianza en sí mismo es el primer secreto del éxito. - Ralph Waldo Emerson",
    "La vida no se trata de encontrarte a ti mismo, sino de crearte a ti mismo. - George Bernard Shaw",
    "No te rindas, cada fracaso es una oportunidad para comenzar de nuevo con más experiencia. - Henry Ford",
    "La felicidad no es algo hecho. Viene de tus propias acciones. - Dalai Lama",
    "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "No busques el éxito, encuéntralo en ti mismo. - Bo Bennett",
    "No hay nada imposible, la palabra misma lo dice: ¡soy posible! - Audrey Hepburn",
    "Las dificultades no existen para hacerte abandonar, sino para hacerte más fuerte. - Unknown",
    "La felicidad es una mariposa, cuanto más la persigues, más huye de ti. Pero si te sientas en silencio, puede posarse sobre ti. - Nathaniel Hawthorne",
    "Las oportunidades no ocurren. Las creas. - Chris Grosse",
    "La vida es como una cámara, enfoca en lo bueno, captura momentos felices y desarrolla a partir de lo negativo. - Unknown",
    "No importa lo lentamente que vayas mientras no te detengas. - Confucio",
    "No tengas miedo de fracasar. Ten miedo de no intentarlo. - Unknown",
    "Si te caes siete veces, levántate ocho. - Proverbio Chino",
    "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "Si puedes soñarlo, puedes lograrlo. - Walt Disney",
    "El éxito no es para los más fuertes, sino para los que nunca se rinden. - Zig Ziglar",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que haces, tendrás éxito. - Buddha",
    "Buscad primeramente el reino de Dios y su justicia, y todas estas cosas os serán añadidas. - Mateo 6:33",
    "Cualquier cosa que pidáis en mi nombre, yo la haré. - Juan 14:14",
    "El Señor es mi fortaleza y mi escudo; en él confía mi corazón, y fui ayudado. - Salmo 28:7",
    "Mirad las aves del cielo, que no siembran, ni siegan, ni recogen en graneros; y, sin embargo, vuestro Padre celestial las alimenta. ¿No valéis vosotros mucho más que ellas? - Mateo 6:26",
    "Porque yo sé los pensamientos que tengo acerca de vosotros, dice Jehová, pensamientos de paz, y no de mal, para daros el fin que esperáis. - Jeremías 29:11",
    "Porque donde están dos o tres congregados en mi nombre, allí estoy yo en medio de ellos. - Mateo 18:20",
    "Bendice, alma mía, a Jehová, y no olvides ninguno de sus beneficios. - Salmo 103:2",
    "Porque nada hay imposible para Dios. - Lucas 1:37",
    "Honra a tu padre y a tu madre, para que tus días se alarguen en la tierra que Jehová tu Dios te da. - Éxodo 20:12",
    "Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos en Cristo Jesús. - Filipenses 4:7",
    "Buscad primeramente el reino de Dios y su justicia, y todas estas cosas os serán añadidas. - Mateo 6:33",
    "Cualquier cosa que pidáis en mi nombre, yo la haré. - Juan 14:14",
    "El Señor es mi fortaleza y mi escudo; en él confía mi corazón, y fui ayudado. - Salmo 28:7",
    "Mirad las aves del cielo, que no siembran, ni siegan, ni recogen en graneros; y, sin embargo, vuestro Padre celestial las alimenta. ¿No valéis vosotros mucho más que ellas? - Mateo 6:26",
    "Porque yo sé los pensamientos que tengo acerca de vosotros, dice Jehová, pensamientos de paz, y no de mal, para daros el fin que esperáis. - Jeremías 29:11",
    "Porque donde están dos o tres congregados en mi nombre, allí estoy yo en medio de ellos. - Mateo 18:20",
    "Bendice, alma mía, a Jehová, y no olvides ninguno de sus beneficios. - Salmo 103:2",
    "Porque nada hay imposible para Dios. - Lucas 1:37",
    "Honra a tu padre y a tu madre, para que tus días se alarguen en la tierra que Jehová tu Dios te da. - Éxodo 20:12",
    "Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos en Cristo Jesús. - Filipenses 4:7",
    "Y todo lo que hagáis, hacedlo de corazón, como para el Señor y no para los hombres. - Colosenses 3:23",
    "Dios es nuestro amparo y fortaleza, nuestro pronto auxilio en las tribulaciones. - Salmo 46:1",
    "El que confía en su riqueza caerá, pero los justos reverdecerán como ramas frondosas. - Proverbios 11:28",
    "Jesús le dijo: Yo soy el camino, y la verdad, y la vida; nadie viene al Padre, sino por mí. - Juan 14:6",
    "De cierto, de cierto os digo: El que cree en mí, tiene vida eterna. - Juan 6:47",
    "Porque el amor de Cristo nos constriñe, pensando esto: que si uno murió por todos, luego todos murieron. - 2 Corintios 5:14",
    "Bendice, alma mía, a Jehová, y no olvides ninguno de sus beneficios. - Salmo 103:2",
    "El que teme al Señor tiene una vida segura y protegida; sus hijos también tendrán un refugio. - Proverbios 14:26",
    "Porque el Señor tu Dios está contigo, por dondequiera que vayas. - Josué 1:9",
    "Pero en todas estas cosas somos más que vencedores por medio de aquel que nos amó. - Romanos 8:37",
    "Porque yo sé los planes que tengo para ustedes, planes para su bienestar y no para su mal, para darles un futuro y una esperanza. - Jeremías 29:11",
    "El Señor es mi luz y mi salvación, ¿a quién temeré? El Señor es la fortaleza de mi vida, ¿de quién tendré temor? - Salmo 27:1",
    "Encomienda al Señor tus obras, y tus planes se cumplirán. - Proverbios 16:3",
    "Toda buena dádiva y todo don perfecto descienden de lo alto, del Padre de las luces, en quien no hay cambio ni sombra de variación. - Santiago 1:17",
    "El Señor es mi pastor, nada me faltará. - Salmo 23:1",
    "Ama al Señor tu Dios con todo tu corazón, con toda tu alma, con toda tu mente y con todas tus fuerzas. - Marcos 12:30",
    "Yo les he dicho estas cosas para que en mí tengan paz. En este mundo tendrán aflicción. Pero ¡ánimo! Yo he vencido al mundo. - Juan 16:33",
    "Busquen primeramente el reino de Dios y su justicia, y todas estas cosas les serán añadidas. - Mateo 6:33",
    "Cristo vive en mí. La vida que ahora vivo en el cuerpo, la vivo por la fe en el Hijo de Dios, quien me amó y se entregó por mí. - Gálatas 2:20",
    "Por tanto, si alguno está en Cristo, es una nueva creación. ¡Lo viejo ha pasado, ha llegado ya lo nuevo! - 2 Corintios 5:17",
    "Cree en ti mismo y todo lo que eres. Sé consciente de que hay algo dentro de ti que es más grande que cualquier obstáculo. - Christian D. Larson",    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. - Albert Schweitzer", "Si amas lo que estás haciendo, tendrás éxito. - Albert Schweitzer",    "No te detengas hasta que estés orgulloso. - Unknown",    "No busques oportunidades, crea las tuyas propias. - Unknown",    "No es el tamaño de la montaña lo que importa, sino la determinación para escalarla. - Unknown",    "La felicidad no es algo hecho. Viene de tus propias acciones. - Dalai Lama",    "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",    "El fracaso no es una opción. Todos tenemos caídas, lo importante es levantarnos y seguir adelante. - Kobe Bryant",    "El éxito no es una llave maestra para la felicidad. La felicidad es la llave maestra para el éxito. - Herman Cain",    "El éxito no es para los más fuertes, sino para los que nunca se rinden. - Zig Ziglar",    "Si puedes soñarlo, puedes lograrlo. - Walt Disney",    "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",    "Si te caes siete veces, levántate ocho. - Proverbio Chino",    "No tengas miedo de fracasar. Ten miedo de no intentarlo. - Unknown",    "No importa lo lentamente que vayas mientras no te detengas. - Confucio",    "La vida es como una cámara, enfoca en lo bueno, captura momentos felices y desarrolla a partir de lo negativo. - Unknown",    "Las oportunidades no ocurren. Las creas. - Chris Grosser",    "La felicidad es una mariposa, cuanto más la persigues, más huye de ti. Pero si te sientas en silencio, puede posarse sobre ti. - Nathaniel Hawthorne",
    "Las dificultades no existen para hacerte abandonar, sino para hacerte más fuerte. - Unknown" 
}
ConsejosSaludables1 = {
    "Empieza el día con un desayuno saludable y equilibrado.",
    "Realiza alguna actividad física moderada durante al menos 30 minutos al día.",
    "Mantén una buena hidratación a lo largo del día bebiendo suficiente agua.",
    "Asegúrate de incluir una variedad de frutas y verduras frescas en tus comidas diarias.",
    "Trata de reducir el consumo de alimentos procesados y ricos en grasas saturadas y azúcares.",
    "Dedica al menos 15 minutos al día para relajarte y despejar la mente.",
    "Trata de dormir al menos 7 horas al día y mantener una buena higiene del sueño.",
    "Evita fumar y reducir el consumo de alcohol.",
    "Realiza actividades sociales y de ocio que te hagan sentir bien.",
    "Aprende a manejar el estrés y la ansiedad, utilizando técnicas como la meditación o la respiración profunda.",
    "Evita saltarte comidas y mantén un horario regular de comidas para regular el apetito.",
    "Reduce el consumo de sal y opta por utilizar especias y hierbas para dar sabor a tus comidas.",
    "Incorpora alimentos ricos en fibra, como granos enteros y legumbres, para mejorar la digestión y prevenir enfermedades crónicas.",
    "Dedica tiempo a la lectura, ya sea un libro o una revista, para mantener el cerebro activo y en constante aprendizaje.",
    "Realiza estiramientos y ejercicios de movilidad para mantener una buena postura y prevenir lesiones.",
    "Intenta incluir proteínas magras, como pescado, pollo o tofu, en tus comidas principales para mantener los niveles de energía.",
    "Utiliza protector solar para prevenir el daño solar y el envejecimiento prematuro de la piel.",
    "Mantén una buena higiene bucal, cepillando tus dientes dos veces al día y utilizando hilo dental para prevenir enfermedades dentales.",
    "Trata de incluir una actividad creativa en tu día, como pintar o tocar un instrumento, para estimular la creatividad y reducir el estrés.",
    "Mantén una actitud positiva y agradecida, enfocándote en las cosas buenas que tienes en la vida, para mejorar tu bienestar emocional.",
    "Limita el consumo de cafeína y opta por infusiones naturales o té verde para mantener una buena hidratación.",  "Trata de caminar al menos 10,000 pasos al día para mantener una buena salud cardiovascular y mejorar el estado de ánimo.",  "Practica la gratitud escribiendo al menos tres cosas por las que estás agradecido cada día.",  "Dedica tiempo a cultivar tus relaciones interpersonales, ya sea llamando a un amigo o pasando tiempo con tu familia.",  "Toma descansos regulares durante el día para estirarte y evitar estar sentado por largos periodos de tiempo.",  "Aprende una nueva habilidad o toma un curso en línea para estimular tu cerebro y mantenerlo activo.",  "Disminuye el consumo de carnes rojas y opta por proteínas vegetarianas como lentejas o garbanzos para mantener una buena salud digestiva.",  "Dedica tiempo a la reflexión y la introspección para conocer tus propias emociones y pensamientos.",  "Practica la empatía y la compasión hacia los demás para mejorar tus relaciones interpersonales y tu bienestar emocional.",  "Realiza actos de bondad y ayuda a los demás de forma desinteresada para sentirte mejor contigo mismo y mejorar tu bienestar emocional.",
    "Evita estar demasiado tiempo frente a pantallas, ya sea de computadoras, televisores o dispositivos móviles, y haz descansos frecuentes para descansar tus ojos.",    "Trata de hacer una buena gestión del tiempo para evitar el estrés y la sensación de abrumamiento.",    "Asegúrate de tener un ambiente limpio y ordenado en casa y en el trabajo para reducir el estrés y aumentar la productividad.",    "Aprende a decir 'no' cuando necesites priorizar tu tiempo y energía.",    "Dedica tiempo a establecer metas realistas y alcanzables para mantenerte motivado y enfocado.",    "Mantén una buena postura mientras trabajas o realizas actividades físicas para prevenir dolores de espalda y lesiones.",    "Trata de pasar tiempo en la naturaleza, como ir a caminar por el parque o hacer un picnic al aire libre.",    "Aprende a cocinar comidas saludables y nutritivas para evitar la tentación de recurrir a comida rápida o procesada.",    "Dedica tiempo a cuidar y mimar a tus mascotas, si las tienes, ya que pueden mejorar tu bienestar emocional y reducir el estrés.",    "Practica la auto-compasión y aprende a tratarte con amabilidad y paciencia cuando te enfrentas a situaciones difíciles."

}

def consejodiarios1():
    global consejo_label1, consejo_label2, ConsejosSaludables1, FrasesMotivadoras
    consejo1 = random.choice(list(ConsejosSaludables1))
    consejo2 = random.choice(list(FrasesMotivadoras))
    consejo_label1.config(text=consejo1)
    consejo_label2.config(text=consejo2)
    
def consejosdiarios(ventana_principal):
    global consejo_label1, consejo_label2, ConsejosSaludables1, FrasesMotivadoras
    # Crear nueva ventana
    nueva_ventanacd = tk.Toplevel()
    nueva_ventanacd.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventanacd.protocol("WM_DELETE_WINDOW", lambda: None)
    # Configurar nueva ventana
    nueva_ventanacd.title("✨ Consejos Diarios ✨")
    nueva_ventanacd.geometry("1200x300")

    # Agregar imagen y texto a la nueva ventana
    try:
        # Obtener la ruta completa de la imagen
        imagen_path = os.path.join(os.path.dirname(__file__), "CONSEJOS.png")
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((1200, 300), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(nueva_ventanacd, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()
    except Exception as e:
        print("Error al cargar la imagen:", e)
# font: especifica la fuente, tamaño y estilo del texto (por ejemplo, "Helvetica 12 bold italic").
# fg: especifica el color del texto (por ejemplo, "blue", "#FF0000").
# bg: especifica el color de fondo del widget (por ejemplo, "white", "#FFFFFF").
# justify: especifica la alineación del texto dentro del widget (por ejemplo, "left", "center", "right").

    texto_label = tk.Label(nueva_ventanacd, text="✨ Consejos Diarios ✨")
    texto_label.pack()
    # Crear dos cuadros de texto para mostrar los consejos
    consejo_label1 = tk.Label(nueva_ventanacd, text="", font=("Helvetica", 10, "bold italic"), fg="white", bg="black")
    consejo_label1.place(x=10, y=50)
    consejo_label2 = tk.Label(nueva_ventanacd, text="", font=("Helvetica", 10, "bold italic"), fg="white", bg="black")
    consejo_label2.place(x=10, y=150)
    
    volver_boton4 = tk.Button(nueva_ventanacd, text="Volver", **estilo_botonCONSEJO, command=nueva_ventanacd.destroy)
    volver_boton4.place(x=50, y=235)
    btn001 = tk.Button(nueva_ventanacd, text="Consejo diario", **estilo_botonCONSEJO, command=consejodiarios1)
    btn001.place(x=400, y=235)
    ventana_principal.withdraw()
estilo_botonCONSEJO = {'font': ('Arial', 15, "italic"),
                'fg': 'white',
                'bg': 'black',
                'width': 15,
                'height': 1}
opcion6.config(command=lambda: consejosdiarios(tk.Toplevel()))
#     ventana_principal.withdraw()
# opcion6.config(command=consejosdiarios)
ventana.mainloop()
