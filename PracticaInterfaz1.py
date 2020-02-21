import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def boton_tab1():
    if nom.get()!="" and ap.get()!="" and am.get()!="" and dire.get()!="" and col.get()!="" and cd.get()!="" and mun.get()!="" :
        
        ventana_personales=tk.Tk()
        ventana_personales.title("Datos Personales Registrados")
        ttk.Label(ventana_personales, text="Nombre:\t").grid(column=0,row=0)
        ttk.Label(ventana_personales, text=nom.get()).grid(column=1, row=0)
        ttk.Label(ventana_personales, text="Apellido Paterno:\t").grid(column=0,row=1)
        ttk.Label(ventana_personales, text=ap.get()).grid(column=1,row=1)
        ttk.Label(ventana_personales, text="Apellido Materno:\t").grid(column=0,row=2)
        ttk.Label(ventana_personales, text=am.get()).grid(column=1,row=2)
        ttk.Label(ventana_personales, text="Direccion:\t").grid(column=0,row=3)
        ttk.Label(ventana_personales, text=dire.get()).grid(column=1,row=3)
        ttk.Label(ventana_personales, text="Colonia:\t").grid(column=0,row=4)
        ttk.Label(ventana_personales, text=col.get()).grid(column=1,row=4)
        ttk.Label(ventana_personales, text="Ciudad:\t").grid(column=0,row=5)
        ttk.Label(ventana_personales, text=cd.get()).grid(column=1,row=5)
        ttk.Label(ventana_personales, text="Municipio:\t").grid(column=0,row=6)
        ttk.Label(ventana_personales, text=mun.get()).grid(column=1,row=6)
    else :
        aviso=ttk.Label(tab1, text="")
        aviso.grid(column=1, row=7)
        aviso.configure(text="Datos Incompletos")

def boton_tab2():
    selector=opcion.get()
    est_civ=""
    if selector==1: est_civ="Soltero"
    elif selector==2: est_civ="Casado"
    elif selector==3: est_civ="Viudo"
    if est_civ!="":
        r=2
        ventana_extras=tk.Tk()
        ventana_extras.title("Datos Extras Registrados")
        ttk.Label(ventana_extras, text="Pasatiempos:").grid(column=0, row=1)
        if pasatiempo_1.get()==1 or pasatiempo_2.get()==1 or pasatiempo_3.get()==1:
            if pasatiempo_1.get()==1:
                ttk.Label(ventana_extras, text="Leer").grid(column=0, row=r)
                r=r+1
            if pasatiempo_2.get()==1:
                ttk.Label(ventana_extras, text="Peliculas").grid(column=0,row=r)
                r=r+1
            if pasatiempo_3.get()==1:
                ttk.Label(ventana_extras, text="Redes Sociales").grid(column=0, row=r)
                r=r+1
        else:
            tk.Label(ventana_extras, text="No se seleccionaron pasatiempos").grid(column=0, row=r)
            r=r+1
        ttk.Label(ventana_extras, text="Estado Civil:").grid(column=0, row=r)
        r=r+1
        ttk.Label(ventana_extras, text=est_civ).grid(column=0, row=r)
        r=r+1
        ttk.Label(ventana_extras, text="Objetivos de la vida").grid(column=0, row=r)
        r=r+1
        if obj.get()!="":
            ttk.Label(ventana_extras, text=obj.get()).grid(column=0, row=r)
            r=r+1
        else:
            ttk.Label(ventana_extras, text="No se escribio ningun objetivo de la vida").grid(column=0, row=r)
            r=r+1
    else:
        aviso2=ttk.Label(tab2, text="")
        aviso2.configure(text="Datos Incompletos(El campo Estado Civil es obligatorio)")
        aviso2.grid(column=1, row=7)

def funcion_imprime():
    ventana_imprime=tk.Tk()
    ventana_imprime.title("Datos")
    if nom.get()!="" and ap.get()!="" and am.get()!="" and dire.get()!="" and col.get()!="" and cd.get()!="" and mun.get()!="" :
        selector=opcion.get()
        est_civ=""
        if selector==1: est_civ="Soltero"
        elif selector==2: est_civ="Casado"
        elif selector==3: est_civ="Viudo"
        if est_civ!="":
            ttk.Label(ventana_imprime, text="Nombre:\t").grid(column=0,row=0)
            ttk.Label(ventana_imprime, text=nom.get()).grid(column=1, row=0)
            ttk.Label(ventana_imprime, text="Apellido Paterno:\t").grid(column=0,row=1)
            ttk.Label(ventana_imprime, text=ap.get()).grid(column=1,row=1)
            ttk.Label(ventana_imprime, text="Apellido Materno:\t").grid(column=0,row=2)
            ttk.Label(ventana_imprime, text=am.get()).grid(column=1,row=2)
            ttk.Label(ventana_imprime, text="Direccion:\t").grid(column=0,row=3)
            ttk.Label(ventana_imprime, text=dire.get()).grid(column=1,row=3)
            ttk.Label(ventana_imprime, text="Colonia:\t").grid(column=0,row=4)
            ttk.Label(ventana_imprime, text=col.get()).grid(column=1,row=4)
            ttk.Label(ventana_imprime, text="Ciudad:\t").grid(column=0,row=5)
            ttk.Label(ventana_imprime, text=cd.get()).grid(column=1,row=5)
            ttk.Label(ventana_imprime, text="Municipio:\t").grid(column=0,row=6)
            ttk.Label(ventana_imprime, text=mun.get()).grid(column=1,row=6)
            r=8
            pas=ttk.Label(ventana_imprime, text="Pasatiempos:")
            pas.grid(column=0, row=7)
            pas.configure(foreground='green')
            if pasatiempo_1.get()==1 or pasatiempo_2.get()==1 or pasatiempo_3.get()==1:
                if pasatiempo_1.get()==1:
                    ttk.Label(ventana_imprime, text="Leer").grid(column=0, row=r)
                    r=r+1
                if pasatiempo_2.get()==1:
                    ttk.Label(ventana_imprime, text="Peliculas").grid(column=0,row=r)
                    r=r+1
                if pasatiempo_3.get()==1:
                    ttk.Label(ventana_imprime, text="Redes Sociales").grid(column=0, row=r)
                    r=r+1
            else:
                tk.Label(ventana_imprime, text="No se seleccionaron pasatiempos").grid(column=0, row=r)
                r=r+1
            es=ttk.Label(ventana_imprime, text="Estado Civil:")
            es.grid(column=0, row=r)
            es.configure(foreground='red')
            r=r+1
            ttk.Label(ventana_imprime, text=est_civ).grid(column=0, row=r)
            r=r+1
            ob=ttk.Label(ventana_imprime, text="Objetivos de la vida")
            ob.grid(column=0, row=r)
            ob.configure(foreground="purple")
            r=r+1
            if obj.get()!="":
                ttk.Label(ventana_imprime, text=obj.get()).grid(column=0, row=r)
                r=r+1
            else:
                ttk.Label(ventana_imprime, text="No se escribio ningun objetivo de la vida").grid(column=0, row=r)
                r=r+1
        else:
            error=ttk.Label(ventana_imprime, text="Datos incompletos")
            error.grid(column=0, row=0, padx=25, pady=25)
            error.configure(foreground='red')
            ventana_imprime.geometry('200x50')
    else:
        error2=ttk.Label(ventana_imprime, text="Datos incompletos")
        error2.grid(column=0, row=0, padx=25, pady=25)
        error2.configure(foreground='red')
        ventana_imprime.geometry('200x50')

def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

def funcion_caja_mensaje():
    mBox.showinfo('Acerca de','Francisco Gerardo Cortès Rodriguez.\nISC\n4to Semestre\nITM')

ventana=tk.Tk()
ventana.title("Sistema Escolar")

tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos Personales')
tabControl.add(tab2, text='Datos Extras')
tabControl.pack(expand=1, fill="both")

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command=funcion_imprime)
opciones_menu.add_command(label="Salir",command=funcion_salir)
barra_menu.add_cascade(label="Sistema", menu=opciones_menu)
opciones_menu2=Menu(barra_menu)
opciones_menu2.add_command(label="Acerca de", command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda", menu=opciones_menu2)


nom=tk.StringVar()
ap=tk.StringVar()
am=tk.StringVar()
dire=tk.StringVar()
col=tk.StringVar()
cd=tk.StringVar()
mun=tk.StringVar()
obj=tk.StringVar()

ttk.Label(tab1, text="Nombre:").grid(column=0,row=0, padx=10, pady=10)
ttk.Label(tab1, text="Apellido Paterno:").grid(column=0,row=1, padx=10, pady=10)
ttk.Label(tab1, text="Apellido Materno:").grid(column=0,row=2, padx=10, pady=10)
ttk.Label(tab1, text="Direccion:").grid(column=0,row=3, padx=10, pady=10)
ttk.Label(tab1, text="Colonia:").grid(column=0,row=4, padx=10, pady=10)
ttk.Label(tab1, text="Ciudad:").grid(column=0,row=5, padx=10, pady=10)
ttk.Label(tab1, text="Municipio:").grid(column=0,row=6, padx=10, pady=10)

p_nom=ttk.Entry(tab1, width=20, textvariable=nom)
p_nom.grid(column=1, row=0) # 8
p_ap=ttk.Entry(tab1, width=20, textvariable=ap)
p_ap.grid(column=1, row=1) # 8
p_am=ttk.Entry(tab1, width=20, textvariable=am)
p_am.grid(column=1, row=2) # 8

s_dire=ttk.Combobox(tab1, width=20, textvariable=dire)
s_dire['values']=("1","2","3")
s_dire.grid(column=1, row=3)
s_dire.current(0)

s_col=ttk.Combobox(tab1, width=20, textvariable=col)
s_col['values']=("Santiaguito","Torreon","Pedregal")
s_col.grid(column=1, row=4)
s_col.current(0)

s_cd=ttk.Combobox(tab1, width=20, textvariable=cd)
s_cd['values']=("Morelia","Lazaro","Uruapan")
s_cd.grid(column=1, row=5)
s_cd.current(0)
s_mun=ttk.Combobox(tab1, width=20, textvariable=mun)
s_mun['values']=("Uruapan","Patzcuaro","Puruandiro")
s_mun.grid(column=1, row=6)
s_mun.current(0)
boton1=ttk.Button(tab1, text="Imprimir Datos Personales", command=boton_tab1)
boton1.grid(column=2, row=6, padx=40, pady=5)

label1=ttk.Label(tab2, text="Pasatiempos")
label1.grid(column=0, row=0, padx=20, pady=10)
label1.configure(foreground='green')

pasatiempo_1=tk.IntVar()
C1=tk.Checkbutton(tab2, text="Leer", variable=pasatiempo_1)
C1.deselect()
C1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

pasatiempo_2=tk.IntVar()
C2=tk.Checkbutton(tab2, text="Peliculas", variable=pasatiempo_2)
C2.deselect()
C2.grid(column=1, row=1, sticky=tk.W)

pasatiempo_3=tk.IntVar()
C3=tk.Checkbutton(tab2, text="Redes Sociales", variable=pasatiempo_3)
C3.deselect()
C3.grid(column=2, row=1, sticky=tk.W)

estado=ttk.Label(tab2, text="Estado Civil")
estado.grid(column=0, row=2, padx=20, pady=10)
estado.configure(foreground='green')

opcion=tk.IntVar()
radio1=tk.Radiobutton(tab2, text="Soltero", variable=opcion, value=1)
radio1.grid(column=0, row=3, sticky=tk.W, padx=10, pady=5)
radio2=tk.Radiobutton(tab2, text="Casado", variable=opcion, value=2)
radio2.grid(column=1, row=3, sticky=tk.W)
radio3=tk.Radiobutton(tab2, text="Viudo", variable=opcion, value=3)
radio3.grid(column=2, row=3, sticky=tk.W)

objetivo=ttk.Label(tab2, text="Objetivo de la vida")
objetivo.grid(column=0, row=4, padx=40, pady=10)
objetivo.configure(foreground='green')
p_obj=ttk.Entry(tab2, width=20, textvariable=obj)
p_obj.grid(column=0, row=5, padx=10, pady=0) # 8
boton2=ttk.Button(tab2, text="Botón Imprimir Datos", command=boton_tab2)
boton2.grid(column=1, row=5, padx=100, pady= 20)
ventana.mainloop()