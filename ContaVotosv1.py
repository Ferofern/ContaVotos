import tkinter as tk
import matplotlib.pyplot as plt

listaLuisa = [0]
listaBoboa = [0]
x = 0
y = 0

def entrada1():
    vLuisa1 = CajaVotosLuisa.get()
    vLuisa2 = int(vLuisa1)
    return vLuisa2

def entrada2():
    vNoboa1 = CajaVotosBoboa.get()
    vNoboa2 = int(vNoboa1)
    return vNoboa2

def sumaVotos():
    global x, y
    vL = entrada1()
    listaLuisa.append(vL)
    x = sum(listaLuisa)
    vB = entrada2()
    listaBoboa.append(vB)
    y = sum(listaBoboa)
    z = x + y
    Lp = (x*100)/z
    Ld = (y*100)/z
    mensaje = 'Luisa Gonzales: ' + str(round(Lp, 2)) + '%' + '     Daniel Noboa: ' + str(round(Ld, 2)) + '%'
    VotosVisibles = tk.Label(menu, text=mensaje, font=('imes', 20))
    VotosVisibles.place(x=10, y=580)
    mensaje2 = 'Luisa Gonzales: ' + str(x) + '     Daniel Noboa: ' + str(y)
    VotosVisibles = tk.Label(menu, text=mensaje2, font=('Times', 20))
    VotosVisibles.place(x=10, y=620)
    return x, y

def mostrarGrafico():
    global x, y  # Utiliza las variables globales
    z = x + y
    Lp = (x * 100) / z
    Ld = (y * 100) / z
    colores = ['blue', 'purple']
    plt.bar(['Luisa Gonzales', 'Daniel Noboa'], [x, y], color=colores)
    plt.ylabel('Votos')
    plt.title('Resultados de Votos')
    plt.text(0, x, f'{Lp:.2f}%', ha='center', va='bottom', fontsize=12)
    plt.text(1, y, f'{Ld:.2f}%', ha='center', va='bottom', fontsize=12)
    plt.show()

# golka


menu = tk.Tk()
menu.title('ContaVotos 1.0')
menu.geometry('675x700')
menu.iconbitmap("C:/Users/ferof/Downloads/Diseño-sin-título-_3_.ico")
luisaFoto = tk.PhotoImage(file="C:/Users/ferof/Downloads/Diseño sin título/1.png")
luisaFotoPantalla = tk.Label(menu, image=luisaFoto)
luisaFotoPantalla.place(x=2, y=3)
LuisaNombre = tk.Label(menu, text='Luisa Gonzales', font=('Times', 20))
LuisaNombre.place(x=65, y=300)
CajaVotosLuisa = tk.Entry(menu, width=5, font=('Times', 20))
CajaVotosLuisa.place(x=105, y=350)

BoboaFoto = tk.PhotoImage(file="C:/Users/ferof/Downloads/Diseño sin título/2.png")
BoboaFotoPantalla = tk.Label(menu, image=BoboaFoto)
BoboaFotoPantalla.place(x=370, y =3)
BoboaNombre = tk.Label(menu, text='Daniel Noboa', font=('Times', 20))
BoboaNombre.place(x=440, y=300)
CajaVotosBoboa = tk.Entry(menu, width=5, font=('Times', 20))
CajaVotosBoboa.place(x=470, y=350)


botonSumaFoto = tk.PhotoImage(file="C:/Users/ferof/Downloads/SUMAR VOTOS/1.png")
boton1 = tk.Button(menu,image=botonSumaFoto, command=lambda: sumaVotos())
boton1.place(x=270, y=400)

botonResultadosFoto = tk.PhotoImage(file="C:/Users/ferof/Downloads/SUMAR VOTOS/2.png")
boton2 = tk.Button(menu,image=botonResultadosFoto, command=lambda: mostrarGrafico())
boton2.place(x=270, y=500)

Company = tk.Label(menu, text='Software Desarrollado por: RedStar Developers ✫', font=('Times', 10))
Company.place(x=10, y=670)

CompanyPhoto = tk.PhotoImage(file="C:/Users/ferof/Downloads/Diseño sin título (2).png")
CompanyPhotoPantalla = tk.Label(menu, image=CompanyPhoto)
CompanyPhotoPantalla.place(x=575, y=600)

menu.mainloop()