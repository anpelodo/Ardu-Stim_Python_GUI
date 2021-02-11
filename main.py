# ------------------------------------------------------------
# name:        Ardu-Stim GUI.py (Python 3.x).
# description: GUI for Ardu-Stim (Speeduino version)
# purpose:     Give a ready to use GUI for ArduStim
# author:      Juan Felipe Giraldo
# ------------------------------------------------------------

__author__ = 'Juan Felipe Giraldo'
__title__ = 'Ardu-Stim'
__date__ = '22/12/2020'
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'

from tkinter import *
from tkinter import ttk, font, messagebox
import serial
import serial.tools.list_ports as coms

# TODO: re-factorizar toda la clase para mantener mejor organización

# TODO: Enlazar diferentes variables entre

class ArduStimGUI:
    def __init__(self, img_carpeta=0, iconos=0):
        # Variables de los íconos y la carpeta
        self.img_carpeta = img_carpeta
        self.iconos = iconos

        self.PuertoStr = str()             # Variable que almacena el puerto Serial seleccionado

        self.serialConection = serial.Serial(baudrate=115200)

        self.raiz = Tk()

        self.SetWindowProperties()      # Función que configura las propiedades de la ventana

        self.SetMainMenu()              # Función que define los componentes del menú principal

        # TODO: Agregar función que lea las configuraciones pre establecidas en el micro en ambos
        # Se abre la ventana
        self.raiz.mainloop()

    def comms(self):
        # print("Se ejecuta comms")
        self.dialogComms = Toplevel()

        # Configuraciónes de la ventana
        posx = str(self.raiz.winfo_rootx() + 50)
        posy = str(self.raiz.winfo_rooty() + 50)
        pos = '150x80+' + posx + "+" + posy
        self.dialogComms.geometry(pos)
        self.dialogComms.resizable(0, 0)

        self.dialogComms.title("Configuración puerto serie")

        # rutina que lista todos los puertos seriales disponibles.
        ports = coms.comports()     # Adquiere la info de todos los puertos Coms disponibles
        sizePorts = len(ports)      # Tamaño de la lista = número de puertos com disponibles

        listPorts = list(str())     # define una lista vacía para llenarla con los nombres de cada puerto
        for i in range(sizePorts):
            name = ports[i].device
            listPorts.insert(i, name)

        # print("Imprimiendo todos los puertos disponibles")
        # print(listPorts)

        if sizePorts == 0:
            # no hay puertos seriales
            stateSelectPort = "disabled"  # Se ajusta como sólo lectura
        else:
            # Existe al menos un puerto serial
            stateSelectPort = "readonly"  # Se ajusta como sólo lectura

        self.selectPort = ttk.Combobox(self.dialogComms,    # Se cargan los datos en un comboBox
                                       values=listPorts,
                                       state=stateSelectPort,
                                       width=10)

        if stateSelectPort == "disabled":
            self.selectPort.set("No ports")
        elif (self.PuertoStr == "") | (self.PuertoStr == "comms") | (self.PuertoStr == "No ports"):
            self.selectPort.set("comms")    # significa que no se ha seleccionado ningún puerto
        else:
            self.selectPort.set(self.PuertoStr)

        button = ttk.Button(self.dialogComms, text="Cerrar", command=self.getSerialPort)

        self.selectPort.pack(side=TOP, padx=5, pady=5)
        button.pack(side=BOTTOM, padx=5, pady=5)
        # self.selectPort.grid(row=0, column=0, columnspan=2)
        # empty.grid(row=1, column=0)
        # Button.grid(row=0, column=2)

        self.dialogComms.transient(master=self.raiz)

        self.dialogComms.grab_set()
        self.raiz.wait_window(self.dialogComms)

        # TODO: Intentar conectar por serial


    def rueda(self):
        print("Se ejecuta rueda")

    def RangeRPM(self):
        print("Se ejecuta Rango RPM")

    # Function to get the Serial Port Selected.
    def getSerialPort(self):
        self.PuertoStr = self.selectPort.get()
        print("getSerialPort: Puerto = " + self.PuertoStr)
        self.dialogComms.destroy()

    # Function to set all window properties
    def SetWindowProperties(self):
        # Window properties
        self.raiz.title(__title__ + " " + __version__)  # Título
        #        self.icono1 = PhotoImage(file=self.iconos[0])   # Icono app
        #        self.raiz.iconphoto(self.raiz, self.icono1)     # Asigna icono app
        self.raiz.option_add("*Font", "Helvetica 10")  # Fuente predeterminada
        self.raiz.option_add('*tearOff', False)  # Deshabilita submenús flotantes
        #        self.raiz.attributes('-fullscreen', True)       # Maximiza ventana completa
        self.raiz.minsize(700, 400)  # Establece tamaño minimo ventana
        self.fuente = font.Font(weight='normal')



    # Function to set the main menu and its elements
    def SetMainMenu(self):
        # Define los menús principales
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu

        self.menu1 = Menu(barramenu)
        self.menu2 = Menu(barramenu)

        barramenu.add_cascade(menu=self.menu1, label='Ajustes')
        barramenu.add_cascade(menu=self.menu2, label='Ayuda')

        # Define los submenús de "Ajustes"

        # TODO: Agregar íconos de ser necesario
        self.menu1.add_command(label='Comms',
                               command=self.comms,
                               underline=0,
                               accelerator="Ctrl+c",
                               # image=icono2,
                               compound=LEFT)

        self.menu1.add_command(label='Rueda',
                               command=self.rueda,
                               underline=0,
                               accelerator="Ctrl+t",
                               compound=LEFT)

        self.menu1.add_command(label="Rango RPM",
                               command=self.RangeRPM,
                               underline=0,
                               accelerator="Ctrl+r",
                               compound=LEFT)

        self.menu1.add_separator()

        # TODO: Definir las variables y los valores de los radiobuttons
        self.menu1.add_radiobutton(label="Sweep",
                                   # variable=,
                                   # command=,
                                   value=0)

        self.menu1.add_radiobutton(label="Fixed",
                                   # variable=,
                                   # command=,
                                   value=1)

        self.menu1.add_radiobutton(label="Pot",
                                   # variable=,
                                   # command=self.Test,
                                   value=2)


def main():
    mi_app = ArduStimGUI()
    return 0


if __name__ == '__main__':
    main()
