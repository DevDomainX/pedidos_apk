# pega pedidos
import tkinter as tk

root = tk.Tk()
root.config(bg="black")

    
def pancho():
    global uno
    uno.config(text=f"""PANCHO     
              Saco / 2 (1/2) Hallulla 
              2 (1/2) Frances / 5 kilos total""")
    
def gaby():
    dos.config(text="""GABY     
     Caja /6 kilos / 4 hallullas y 2 
    Frances + racion 1.3""")
    
def yoko():
    tres.config(text="""YOKO
    saco / 7 kilos  / 5 Hallullas / 2 Frances""")            
            
def radal():
    cuatro.config(text="""Radal
    Bolsa / 30 panes hallullas (LUNES  NO VA )""")        

def jana():
    cinco.config(text="""JANA
    sacos / 2 kilos Frances / 4 kilos Hallullas 
    (SACOS DISTINTOS)""")     

def terminal():
    seis.config(text="""TERMINAL
    Bolsa / 2 kilos / 1 Hallullas / 1 Frances""")              
    
def ruta():
    siete.config(text="""RUTA
    saco / 2 kilos Hallullas""")       

def luchito():
    ocho.config(text="""LUCHITO
    caja blanca / 3 kilos Frances""")
             
def mary():
    nueve.config(text="""MARY
    Saco / 3 kilos surtido""")
                
def paco():
    dies.config(text="""PACO
    Saco / 3 kilos surtido""")
             
def margarita():
    once.config(text="""MARGARITA
    Saco / 3 kilos Frances """)      
          
def reset():
   uno.config(text=" ")            
   dos.config(text=" ")          
   tres.config(text=" ")          
   cuatro.config(text=" ")  
   cinco.config(text=" ")  
   seis.config(text=" ")  
   siete.config(text=" ")  
   ocho.config(text=" ")  
   nueve.config(text=" ")  
   dies.config(text=" ")  
   once.config(text=" ")  
      
def exit():
    root.destroy()                                                                                                                                                                                              
                                                                                                                             
creador = tk.Label(root, text="Creted By: Hans Saldias", bg="black", fg="red")       
creador.place(x=10, y=2100)                                
   
titulo = tk.Label(root, text="PEDIDOS DE LA MAÑANA 1 ", bg="black", fg="orange", font=("arial 10"))
titulo.place(x=200, y=40)                                              
                                                                  
uno = tk.Label(root, text="Buenos dias... \nPresione un boton" , bg="black", fg="cyan")
uno.place(x=100, y=350)


dos = tk.Label(root , bg="black", fg="cyan")
dos.place(x=100, y=350)

tres = tk.Label(root , bg="black", fg="cyan")
tres.place(x=100, y=350)

cuatro= tk.Label(root , bg="black", fg="cyan")
cuatro.place(x=100, y=350)

cinco = tk.Label(root , bg="black", fg="cyan")
cinco.place(x=100, y=350)

seis = tk.Label(root , bg="black", fg="cyan")
seis.place(x=100, y=350)

siete = tk.Label(root , bg="black", fg="cyan")
siete.place(x=100, y=350)

ocho = tk.Label(root , bg="black", fg="cyan")
ocho.place(x=100, y=350)

nueve = tk.Label(root , bg="black", fg="cyan")
nueve.place(x=100, y=350)

dies = tk.Label(root , bg="black", fg="cyan")
dies.place(x=100, y=350)

once = tk.Label(root , bg="black", fg="cyan")
once.place(x=100, y=350)


r = tk.Button(root, text="BORRAR",  command=reset, bg="blue", fg="orange", bd=10, font=("Curier 10"))
r.place(x=700, y=2000)

b1 = tk.Button(root,text="PANCHO", command=pancho, bg="blue", fg="orange", bd=10)
b1.place(x=400, y=550)

b2 = tk.Button(root, text="GABY", command=gaby, bg="blue", fg="orange", bd=10)
b2.place(x=400, y=650)

b3 = tk.Button(root, text="YOKO", command=yoko, bg="blue", fg="orange", bd=10)
b3.place(x=400, y=750)

b4 = tk.Button(root, text="RADAL", command=radal, bg="blue", fg="orange", bd=10)
b4.place(x=400, y=850)

b5 = tk.Button(root, text="JANA", command=jana, bg="blue", fg="orange", bd=10)
b5.place(x=400, y=950)

b6 = tk.Button(root, text="TERMINAL", command=terminal, bg="blue", fg="orange", bd=10)
b6.place(x=400, y=1050)

b7 = tk.Button(root, text="RUTA", command=ruta, bg="blue", fg="orange", bd=10)
b7.place(x=400, y=1150)

b8 = tk.Button(root, text="LUCHITO", command=luchito, bg="blue", fg="orange", bd=10)
b8.place(x=400, y=1250)

b9 = tk.Button(root, text="MARY", command=mary, bg="blue", fg="orange", bd=10)
b9.place(x=400, y=1350)

b10 = tk.Button(root, text="PACO", command=paco, bg="blue", fg="orange", bd=10)
b10.place(x=400, y=1450)

b11 = tk.Button(root, text="MARGARITA", command=margarita, bg="blue", fg="orange", bd=10)
b11.place(x=400, y=1550)

salir = tk.Button(root, text="Salir", bg="black", fg="red", bd=20, command=exit)
salir.place(x=30, y=1900)

root.mainloop()