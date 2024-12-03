"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""
from email.message import EmailMessage  # Construir la estructura del email
import smtplib  # Conectar con el servidor y enviarlo
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

"------------INTERFAZ TKINTER------------"
ventana = Tk()
ventana.title("APLICACIÓN DE MENSAJERÍA")
ventana.geometry("350x350")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(ventana, text="ENVIAR CORREO VIA GMAIL", fg="black", font=("Arial", 15, "bold"), padx=5, pady=5).grid(row=0, column=0, columnspan=2)

# Imagen GMAIL (asegúrate de que tienes una imagen en formato .gif)
try:
    imagen= Image.open("mamani.png")
    imagen_nueva=imagen.resize((125,84))
    render=ImageTk.PhotoImage(imagen_nueva)
    label_imagen = Label(ventana, image=render)
    label_imagen.grid(row=1, column=0, columnspan=2)
except Exception as e:
    print("Error al cargar la imagen:", e)
    Label(ventana, text="Imagen no disponible", fg="red", font=("Arial", 10)).grid(row=1, column=0, columnspan=2)

# Variables
destinatario = StringVar(ventana)
asunto = StringVar(ventana)

Label(ventana, text="Destinatario:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=3, column=0)
Entry(ventana, textvariable=destinatario, width=34).grid(row=3, column=1)

combobox=ttk.Combobox(ventana, textvariable=destinatario, font=("Arial", 10,"bold"), width=30,
                      values=["danielprogramacion53@gmail.com", "studiof443@gmail.com", "programacionsabattini@gmail.com", "tabareslisandro5@gmail.com", "fjcoronati@gmail.com", "lafortaleza246@gmail.com"])
combobox.grid(row=3, column=1)

Label(ventana, text="Asunto:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=4, column=0)
Entry(ventana, textvariable=asunto, width=34).grid(row=4, column=1)

Label(ventana, text="Mensaje:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=5, column=0)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=5, column=1)
mensaje.config(font=("Arial", 9), padx=5, pady=5)


"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = "urielcortez10.2007@gmail.com"
    # Estructura de email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario.get()
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, 'end')))
    
    try:
        # Envio de email
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente, "uopjffjdmjgxpwyd")  # Cambia "clave-personal" por la contraseña real
        smtp.sendmail(remitente, destinatario.get(), email.as_string())
        messagebox.showinfo("MENSAJERÍA", "Mensaje enviado correctamente")
        smtp.quit()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo. Error: {e}")

"------------BOTON------------"
Button(ventana, text="ENVIAR", command=enviar_email, height=2, width=10, bg="black", fg="white", font=("Arial", 10, "bold")).grid(row=6, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()