from tkinter import *
from act_validate_gui import *

def on_closing():
    exit()

def preGui():

    def consola():
        preGui.destroy()

    def gui():
        preGui.destroy()
        mainGui()

    preGui = Tk()
    preGui.geometry('500x500')

    #Frames
    frame1 = Frame(preGui)
    frame2 = Frame(preGui)

    cls = Button(frame2, text='Consola', width=10, height=5, font=("Arial", 14), command=consola)
    gui = Button(frame2, text='Interfaz Grafica', width=10, height=5, font=("Arial", 14), wraplength='100', command=gui)
    pregunta = Label(frame1, text="Que instefaz quieres?", font=("Arial", 24))

    #Grid
    frame2.columnconfigure(0, weight=1)
    frame2.grid_rowconfigure(0,weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.grid_rowconfigure(1,weight=1)

    frame1.pack(fill='x', expand='true')
    frame2.pack(fill='x', expand='true')

    pregunta.pack()
    cls.grid(row=1, column=0)
    gui.grid(row=1, column=1)

    preGui.protocol('WM_DELETE_WINDOW', on_closing)
    preGui.mainloop()
#FIN preGui------------------------------------------------
###########################################################

def mainGui():
    
    def dead():
        interfaz.destroy()

    def valid():
        global v_tries
        global respond

        if validation(usr.get()) == 'Retry':
            if v_tries >= 1:
                respond.destroy()
                
            interfaz.geometry('500x300')
            respond = Label(frame1, text='!!!!!Cuenta no encontrada. Reintente.!!!!!', font=("Arial", 14), fg='red')
            respond.pack()
            v_tries = v_tries + 1
        elif validation(usr.get()) == 'Ok':
            if v_tries >= 1:
                respond.destroy()
            usr.delete(first=0, last='end')
            label1.config(text='Introduzca el pin>> ')
            interfaz.geometry('500x230')
            enter.config(command=valid_pin)

    def valid_pin():
        global v_tries
        global tries
        global respond

        def re():
            interfaz.destroy()
            exit()

        def deposit_gui():
            global tries
            tries = 0

            def deposit():
                global tries
                digitos = Label(frame_pregunta, text='!!!Solo se pueden introducir numeros enteros!!!', font=("Arial", 15), fg='red')
                
                if depositar_fn(get_id, entry.get()) == 'No Number':
                    if tries < 1:
                        digitos.pack()
                    tries = tries + 1
                else:
                    desgloce_lista =  depositar_fn(get_id(), entry.get())
                    results = desgloce_lista
                    
                    m = Label(frame_pregunta, font=("Arial", 15), fg='blue', text='Debes depositar las siguientes cantidades:')
                    m.pack()

                    if results.count(2000) != 0:
                        l2000 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(2000)) + ' Papeletas de 2000')
                        l2000.pack()
                    if results.count(1000) != 0:
                        l1000 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(1000)) + ' Papeletas de 1000')
                        l1000.pack()
                    if results.count(500) != 0:
                        l500 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(500)) + ' Papeletas de 500')
                        l500.pack()
                    if results.count(200) != 0:
                        l200 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(200)) + ' Papeletas de 200')
                        l200.pack()
                    if results.count(100) != 0:
                        l100 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(100)) + ' Papeletas de 100')
                        l100.pack()
                    if results.count(50) != 0:
                        l50 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(50)) + ' Papeletas de 50')
                        l50.pack()
                    if results.count(25) != 0:
                        l25 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(25)) + ' Monedas de 25')
                        l25.pack()
                    if results.count(10) != 0:
                        l10 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(10)) + ' Monedas de 10')
                        l10.pack()
                    if results.count(5) != 0:
                        l5 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(5)) + ' Monedas de 5')
                        l5.pack()
                    if results.count(1) != 0:
                        l1 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(1)) + ' Monedas de 1')
                        l1.pack()
                    new = Label(frame_pregunta, text='Su nuevo balance es = ' + get_balance(), font=("Arial", 24), fg='purple')
                    new.pack()

            pregunta.config(text='Inserte el monto a depositar:')
            retirar.destroy()
            depositar.destroy()
            entry = Entry(frame_pregunta2, font=("Arial", 24), fg='red')
            btt = Button(frame_pregunta, text='Depositar' , height=5, width=20, font=("Arial", 14), command=deposit)
            btt2 = Button(frame_pregunta, text='Cerrar' , height=5, width=20, font=("Arial", 14), command=re)

            entry.pack()
            btt.pack()
            btt2.pack()

        def retiro_gui():
            global tries
            tries = 0
            def retir():
                global tries
                digitos = Label(frame_pregunta, text='!!!Solo se pueden introducir numeros enteros!!!', font=("Arial", 15), fg='red')
                if retirar_fn(get_id, entry.get()) == 'No Number':
                    if tries < 1:
                        digitos.pack()
                    tries = tries + 1
                else:
                    desgloce_lista =  retirar_fn(get_id(), entry.get())
                    results = desgloce_lista
                    m = Label(frame_pregunta, font=("Arial", 15), fg='blue', text='Debes recibir las siguientes cantidades:')
                    m.pack()
                    if results.count(2000) != 0:
                        l2000 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(2000)) + ' Papeletas de 2000')
                        l2000.pack()
                    if results.count(1000) != 0:
                        l1000 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(1000)) + ' Papeletas de 1000')
                        l1000.pack()
                    if results.count(500) != 0:
                        l500 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(500)) + ' Papeletas de 500')
                        l500.pack()
                    if results.count(200) != 0:
                        l200 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(200)) + ' Papeletas de 200')
                        l200.pack()
                    if results.count(100) != 0:
                        l100 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(100)) + ' Papeletas de 100')
                        l100.pack()
                    if results.count(50) != 0:
                        l50 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(50)) + ' Papeletas de 50')
                        l50.pack()
                    if results.count(25) != 0:
                        l25 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(25)) + ' Monedas de 25')
                        l25.pack()
                    if results.count(10) != 0:
                        l10 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(10)) + ' Monedas de 10')
                        l10.pack()
                    if results.count(5) != 0:
                        l5 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(5)) + ' Monedas de 5')
                        l5.pack()
                    if results.count(1) != 0:
                        l1 = Label(frame_pregunta, font=("Arial", 15), fg='blue', text=str(results.count(1)) + ' Monedas de 1')
                        l1.pack()
                    new = Label(frame_pregunta, text='Su nuevo balance es = ' + get_balance(), font=("Arial", 24), fg='purple')
                    new.pack()

            pregunta.config(text='Inserte el monto a retirar:')
            retirar.destroy()
            depositar.destroy()
            entry = Entry(frame_pregunta2, font=("Arial", 24), fg='red')
            btt = Button(frame_pregunta, text='Retirar' , height=5, width=20, font=("Arial", 14), command=retir)
            btt2 = Button(frame_pregunta, text='Cerrar' , height=5, width=20, font=("Arial", 14), command=re)
            entry.pack()
            btt.pack()
            btt2.pack()

        if validation_pin(usr.get()) == 'Ok':                
            frame1.destroy()
            interfaz.geometry('1100x800')

            frame_pregunta = Frame(interfaz)
            frame_pregunta2 = Frame(frame_pregunta)
            pregunta = Label(frame_pregunta, text='Bienveni@ ' + get_usr() + ' Que quieres hacer?' ,font=("Arial", 24), fg='blue')
            depositar = Button(frame_pregunta2, text='Depositar', height=5, width=20, font=("Arial", 14), command=deposit_gui)
            retirar = Button(frame_pregunta2, text='Retirar', height=5, width=20, font=("Arial", 14), command=retiro_gui)
            balance_label = Label(frame_pregunta, text='Tu balance es = ' + get_balance(), font=("Arial", 15), fg='blue')

            frame_pregunta.pack()
            pregunta.pack()
            frame_pregunta2.pack()
            depositar.grid(row='0', column='0')
            retirar.grid(row='0', column='1')
            balance_label.pack()
        else:
            if v_tries >= 1:
                respond.destroy()
            interfaz.geometry('500x300')
            respond = Label(frame1, text='!!!!!Cuenta no encontrada. Reintente.!!!!!', font=("Arial", 14), fg='red')
            respond.pack()
            v_tries = v_tries + 1
            tries = tries + 1

        if tries == 3:
            enter.destroy()
            respond.destroy()
            label1.destroy()
            usr.destroy()
            register.destroy()
            limite = Label(frame1, text='Has llegado al limite de intentos', font=("Arial", 14), fg='red')
            cerrar = Button(frame1, text='Cerar', font=("Arial", 14), command=dead)
            limite.pack()
            cerrar.pack()

    def chng_register():
        register.destroy()
        label1.config(text='Inserta un nombre y apellido>> ')
        enter.config(command=register_ya)
        global tries
        tries = 0
    
    def register_ya():
        global tries

        if usr.get() != '':

            if tries == 0:
                label1.config(text='Introduce una clave/pin (Sin espacios, seran eliminados)>> ', wraplength='500')
                register_gui(usr.get(), tries)
            elif tries == 1:
                label1.config(text='Tu numero de cuenta es ' + register_gui(usr.get(), tries) + ' No lo pierdas y apuntalo.\nCierra y vuelve a iniciar para logearte.')
                usr.destroy()
                enter.destroy()
            tries = tries + 1

    interfaz = Tk()
    interfaz.geometry('500x230')

    frame1 = Frame(interfaz)
    frame2 = Frame(frame1)

    label1 = Label(frame1, text='Bienvenid@ al ATM\nIngrese su número de cuenta>> ', font=("Arial", 24), fg='blue')
    usr = Entry(frame1, font=("Arial", 24), fg='red')
    enter = Button(frame2, text='Enter', height=5, width=20, font=("Arial", 14), command=valid)
    register = Button(frame2, text='Registrarse', height=5, width=20, font=("Arial", 14), command=chng_register)

    #Empaquetado
    frame1.pack()
    label1.pack()
    usr.pack(fill='x')
    frame2.pack()
    enter.grid(row=0, column=0)
    register.grid(row=0, column=1)

    interfaz.protocol("WM_DELETE_WINDOW", on_closing)
    interfaz.mainloop()

v_tries = 0
tries = 0
desgloce_lista = []
#preGui()#QUIIIIIIIIIIIIIIIIIIIIIITAAAAAAAAAAAAAAARRRRRRRRRRRRRRRR