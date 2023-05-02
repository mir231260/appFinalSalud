import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
#import pandas as pd
global busqueda_entry
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
global imagen_fondo


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
imagen = imagen.resize((500, 500), Image.ANTIALIAS)
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

# def buscar():
#     # Obtener la palabra clave ingresada por el usuario
#     palabra_clave = busqueda_entry.get()
#     # Verificar si la palabra clave está en el diccionario de enfermedades
#     if palabra_clave in enfermedades:
#         # Mostrar la información correspondiente en una nueva ventana
#         ventana_info = tk.Toplevel(ventana)
#         ventana_info.title("Información sobre {}".format(palabra_clave))
#         texto_info = tk.Text(ventana_info, height=10, width=100)
#         texto_info.pack()
#         texto_info.insert(tk.END, enfermedades[palabra_clave])
#         mensaje_error.config(text="")
#     else:
#         mensaje_error.config(text="Ingrese una palabra clave válida")
# 
# def buscar_prevencion():
#     # Obtener la palabra clave ingresada por el usuario
#     palabra_clave = busqueda_entry.get()
#     # Verificar si la palabra clave está en el diccionario de prevencion
#     if palabra_clave in prevencion:
#         # Mostrar la información correspondiente en una nueva ventana
#         ventana_info = tk.Toplevel(ventana)
#         ventana_info.title("Prevención de {}".format(palabra_clave))
#         texto_info = tk.Text(ventana_info, height=10, width=100)
#         texto_info.pack()
#         texto_info.insert(tk.END, prevencion[palabra_clave])
#         mensaje_error.config(text="")
#     else:
#         mensaje_error.config(text="Ingrese una palabra clave válida para prevención")
# 
# # Agregar un mensaje de error para mostrar en caso de que la palabra clave no esté en el diccionario
# mensaje_error = tk.Label(ventana, text="", fg="red")
# mensaje_error.pack()

# Agregar caja de texto y botón de búsqueda
# busqueda_frame = tk.Frame(ventana, bg="#9e2626", width=200, height=50)
# busqueda_frame.place(x=0, y=385)
# busqueda_label = tk.Label(busqueda_frame, text="Palabra Clave:", font=("Arial", 15, "italic"))
# busqueda_label.pack(side="left", padx=5)
# busqueda_entry = tk.Entry(busqueda_frame, width=30)
# busqueda_entry.pack(side="left", padx=5)
# # Agregar botón de búsqueda
# boton_buscar = tk.Button(busqueda_frame, text="Buscar", command=buscar)
# boton_buscar.pack(side="left", padx=5)
# # Botón para prevención
# boton_prevencion = tk.Button(busqueda_frame, text="Prevención", command=buscar_prevencion)
# boton_prevencion.pack(side="left", padx=10)
# Crear el mensaje de error
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
        imagen_fondo = ImageTk.PhotoImage(Image.open("C:\\Users\\famil\\Desktop\\PROGRA\\saludapp231260\\imagen_fondo.png"))
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
        imagen_fondo = ImageTk.PhotoImage(Image.open("C:\\Users\\famil\\Desktop\\PROGRA\\saludapp231260\\imagen_fondo.png"))
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
opcion2 = tk.Button(menu_frame, text=" ✨ Ejercicios ✨  ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion2.pack(padx=10, pady=10)
opcion2.config(bg='gray')
opcion3 = tk.Button(menu_frame, text=" ⚠ ¡Ayuda! ⚠ ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion3.pack(padx=10, pady=10)
opcion3.config(bg='gray')
opcion4 = tk.Button(menu_frame, text=" ⚠ Salir ⚠ ", font=("Arial", 10, "italic"), padx=20, pady=10, command=salir)
opcion4.pack(padx=10, pady=10)
opcion4.config(bg='gray')
opcion5 = tk.Button(menu_frame, text=" Palabras Clave ", font=("Arial", 10, "italic"), padx=20, pady=10)
opcion5.pack(padx=10, pady=10)
opcion5.config(bg='gray')
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
#     nueva_ventana1.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
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

opcion5.config(command=cambiar_ventana1)

def cambiar_ventana2():
    # Crear nueva ventana
    nueva_ventana2 = tk.Toplevel()
#     nueva_ventana.overrideredirect(True)
#     nueva_ventana1.resizable(False, False) # Deshabilitar botón de agrandar y cerrar ventana
    nueva_ventana2.protocol("WM_DELETE_WINDOW", lambda: None)


    # Configurar nueva ventana
    nueva_ventana2.title(" ✨ Ejercicios en Casa ✨ ")
    nueva_ventana2.geometry("500x500")

    # Agregar imagen y texto a la nueva ventana
    imagen = tk.PhotoImage(file="PalabrasClave.png")
    imagen_label = tk.Label(nueva_ventana2, image=imagen)
    imagen_label.pack()
    texto_label = tk.Label(nueva_ventana2, text="Palabras Clave <3 ")
    texto_label.pack()

    # Agregar botón para volver a la ventana anterior
#     volver_boton = tk.Button(nueva_ventana, text="Volver", command=nueva_ventana.destroy)
#     volver_boton.pack()
    volver_boton3 = tk.Button(nueva_ventana2, text="Volver", command=nueva_ventana2.destroy)
    volver_boton3.place(x=230, y=470)

    # Ocultar ventana actual
    ventana_principal.withdraw()

opcion2.config(command=cambiar_ventana2)

ventana.mainloop()
