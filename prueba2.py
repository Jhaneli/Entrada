from tkinter import *

Base = Tk()
Base.title("Registro Estudiantes")
                #alto               
Base.resizable(0,0)#gordo
#Base.geometry("500x500")
#Cambiar el .pyw para abrir directo :D
Base.config(bg = "gray")
Centro = Frame(Base, width = 600, height= 600)
Centro.pack()

Centro.config(width="500", height="400")
Centro.config(bg = "gray")
Centro.pack(fill = "y", expand ="True")
Centro.config(relief = "raised")
Centro.config(bd = 5)

Tag = Label(Centro, text = "Registro Estudiantes", fg= "Black", font= ("Arial Bold", 20)).place(x= 125, y= 10)
Tag = Label(Centro, text = "Entrada Usuario", fg= "Gray", font= ("Arial Bold", 12)).place(x= 90, y= 50)

Tag = Label(Centro, text = "Usuario", fg= "black", font= ("Arial", 10)).place(x= 25, y=100)
Usuario = Entry(Centro).place(x= 100, y= 100)
Tag = Label(Centro, text = "Clave", fg= "black", font= ("Arial", 10)).place(x= 25, y=120)
Usuario = Entry(Centro, show="*").place(x= 100, y= 120)



Ingresar= Button(Base, text = "Ingresar") 
Ingresar.pack()

def aaa():

    #Nombre
    Tag1 = Label(Centro, text = "Nombre", fg= "black", font= ("Arial", 10)).place(x= 25, y= 80)
    Datos1 = Entry(Centro).place(x= 100, y= 80)
    #Apellido
    Tag2 = Label(Centro, text = "Apellidos", fg= "black", font= ("Arial", 10)).place(x= 25, y= 120)
    Datos2 = Entry(Centro).place(x= 100, y= 120)
    #Num contacto
    Tag3 = Label(Centro, text = "Telefono", fg= "black", font= ("Arial", 10)).place(x= 25, y= 160)
    Datos3 = Entry(Centro).place(x= 100, y= 160)

    #Boton
    Enviar= Button(Base, text = "Guardar") #""""Command = enviar"""" para incluir luegos
    Enviar.pack()
    Enviar= Button(Base, text = "Borrar")
    Enviar.pack()
    Enviar= Button(Base, text = "Volver")
    Enviar.pack()

Base.mainloop() 

