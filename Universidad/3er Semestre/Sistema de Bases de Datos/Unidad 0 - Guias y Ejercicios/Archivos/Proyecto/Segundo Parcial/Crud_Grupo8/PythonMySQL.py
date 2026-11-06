import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from Conexion import *
from PIL import Image, ImageTk

class FormularioClientes:
    global base
    base=None

    global textBoxID
    textBoxID=None

    global textBoxDireccion
    textBoxDireccion=None

    global textBoxCorreo
    textBoxCorreo=None

    global combo
    combo=None

    global groupBox
    groupBox=None

    global tree
    tree=None

    global textBoxSeleccion
    textBoxSeleccion=None

def Formulario():
    global base
    global textBoxID
    global textBoxDireccion
    global textBoxCorreo
    global combo
    global groupBox
    global tree
    global textBoxSeleccion
    try:
        base = Tk()
        base.geometry("1210x480")
        base.title("ImportTrack")
        imagen_original = Image.open("Logo.png")
        imagen_redimensionada = imagen_original.resize((32, 32))
        icono = ImageTk.PhotoImage(imagen_redimensionada)
        base.iconphoto(False, icono)

        groupBox = LabelFrame(base,text="Datos del Cliente",padx=5,pady=5)
        groupBox.grid(row=0,column=1,padx=10,pady=10)

        labelId = Label(groupBox,text="ID: ",width=13,font=("arial",12)).grid(row=0,column=0)
        textBoxID = Entry(groupBox)
        textBoxID.grid(row=0,column=1)

        labelDireccion = Label(groupBox,text="Direccion: ",width=13,font=("arial",12)).grid(row=1,column=0)
        textBoxDireccion = Entry(groupBox)
        textBoxDireccion.grid(row=1,column=1)

        labelCorreo = Label(groupBox,text="Correo: ",width=13,font=("arial",12)).grid(row=2,column=0)
        textBoxCorreo = Entry(groupBox)
        textBoxCorreo.grid(row=2,column=1)

        labelTipo = Label(groupBox,text="Tipo: ",width=13,font=("arial",12)).grid(row=3,column=0)
        seleccionTipo = tk.StringVar()
        combo = ttk.Combobox(groupBox,values=["Natural","Juridica"],textvariable=seleccionTipo)
        combo.grid(row=3,column=1)
        seleccionTipo.set("Natural")

        Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
        Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=4,column=1)
        Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=4,column=2)


        imagen_logo = Image.open("ImportTrackLogo.png")
        imagen_logo = imagen_logo.resize((300, 300))
        imagen_tk = ImageTk.PhotoImage(imagen_logo)

        labelLogo = Label(base, image=imagen_tk)
        labelLogo.image = imagen_tk
        labelLogo.grid(row=1, column=1, pady=(0, 20))


        groupBox = LabelFrame(base,text="Lista de Clientes",padx=5,pady=5)
        groupBox.grid(row=1,column=0,padx=5,pady=5)

        tree = ttk.Treeview(groupBox,columns=("ID_Cliente","Direccion","Correo","Tipo"),show='headings',height=10)
        tree.column("# 1",anchor=CENTER)
        tree.heading("# 1",text="ID_Cliente")
        tree.column("# 2",anchor=CENTER)
        tree.heading("# 2",text="Direccion")
        tree.column("# 3",anchor=CENTER)
        tree.heading("# 3",text="Correo")
        tree.column("# 4",anchor=CENTER)
        tree.heading("# 4",text="Tipo")

        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)

        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

        tree.pack()

        groupBoxBusqueda = LabelFrame(base, text="Buscar Cliente", padx=5, pady=5)
        groupBoxBusqueda.grid(row=0, column=0, padx=5, pady=5)

        labelSeleccion = Label(groupBoxBusqueda, text="Ingrese un ID para buscar:", font=("arial",12))
        labelSeleccion.grid(row=0, column=0, sticky="w")
        textBoxSeleccion = Entry(groupBoxBusqueda)
        textBoxSeleccion.grid(row=1, column=0, padx=5, pady=5)

        Button(groupBoxBusqueda, text="Buscar",command=seleccionarCliente).grid(row=2, column=0, padx=5, pady=5)
        Button(groupBoxBusqueda, text="Mostrar Todos", command=actualizarTreeView).grid(row=3, column=0, padx=5, pady=5)




        base.mainloop()
    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))


def guardarRegistros():
    global textBoxDireccion,textBoxCorreo,combo,groupBox

    try:
        if textBoxDireccion is None or textBoxCorreo is None or combo is None:
            print("Los Widget no estan inicializados")
            return
        direccion = textBoxDireccion.get()
        correo = textBoxCorreo.get()
        tipo = combo.get()
        CClientes.ingresarClientes(direccion,correo,tipo)
        messagebox.showinfo("Informacion","Los datos fueron guardados")
        actualizarTreeView()
        textBoxDireccion.delete(0,END)
        textBoxCorreo.delete(0,END)
    except ValueError as error:
        print("Error al mostrar los datos {}".format(error))


def actualizarTreeView():
    global tree
    try:
        tree.delete(*tree.get_children())
        datos = CClientes.mostrarClientes()
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)
    except ValueError as error:
        print("Error al actulizar tabla {}".format(error))    

def seleccionarRegistro(evento):
    try:
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            values = tree.item(itemSeleccionado)['values']
            textBoxID.delete(0,END)
            textBoxID.insert(0,values[0])
            textBoxDireccion.delete(0,END)
            textBoxDireccion.insert(0,values[1])
            textBoxCorreo.delete(0,END)
            textBoxCorreo.insert(0,values[2])
            combo.set(values[3])
    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
    global textBoxID,textBoxDireccion,textBoxCorreo,combo,groupBox
    try:
        if textBoxID is None or textBoxDireccion is None or textBoxCorreo is None or combo is None:
            print("Los Widget no estan inicializados")
            return
        id = textBoxID.get()
        direccion = textBoxDireccion.get()
        correo = textBoxCorreo.get()
        tipo = combo.get()
        CClientes.modificarClientes(id,direccion,correo,tipo)
        messagebox.showinfo("Informacion","Los datos fueron actualizados")
        actualizarTreeView()
        textBoxID.delete(0,END)
        textBoxDireccion.delete(0,END)
        textBoxCorreo.delete(0,END)
    except ValueError as error:
        print("Error al actualizar los datos {}".format(error))

def eliminarRegistros():
    global textBoxID,textBoxDireccion,textBoxCorreo,combo,groupBox
    try:
        if textBoxID is None:
            print("El Widget no esta inicializados")
            return
        id = textBoxID.get()
        CClientes.eliminarClientes(id)
        messagebox.showinfo("Informacion","El registro fue eliminado")
        actualizarTreeView()
        textBoxCorreo.delete(0,END)
        textBoxDireccion.delete(0,END)
        textBoxID.delete(0,END)
    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))

def seleccionarCliente():
    global textBoxSeleccion
    try:
        if textBoxSeleccion is None:
            print("No se ha ingresado una ID")
            return
        id = textBoxSeleccion.get()
        tree.delete(*tree.get_children())
        datos = CClientes.seleccionarCliente(id)
        for row in datos:
            tree.insert("","end",values=row)
        textBoxSeleccion.delete(0,END)
    except ValueError as error:
        print("Error al actualizar los datos {}".format(error))
Formulario()    