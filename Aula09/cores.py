from tkinter import *

janela = Tk()
janela.title('Aprendendo Cores')
janela.geometry('200x200')
janela.configure(bg='yellow')

def mostrarAltura():
    altura = float(altura_Input.get())
    resultado.configure(font=('arial', 12),text=f'Sua altura é {altura}.', fg='red')


altura_Label = Label(text='Digite a sua altura:', fg='red', bg='black')
altura_Label.pack()
altura_Input = Entry()
altura_Input.pack()

botao = Button(janela, text='Enviar', command=mostrarAltura ,bg='pink', fg='green', width=14, height=2)
botao.pack()

resultado = Label(text='', bg='yellow')
resultado.pack()


janela.mainloop()