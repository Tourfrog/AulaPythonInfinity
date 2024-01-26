from tkinter import *

janelinha = Tk()
janelinha.title('Tarefa')
janelinha.geometry('400x200')

numero1Label = Label(text='Digite um número qualquer:')
numero1Input = Entry()
numero1Label.pack()
numero1Input.pack()

numero2Label = Label(text='Digite um número qualquer:')
numero2Input = Entry()
numero2Label.pack()
numero2Input.pack()

def soma():
    num1 = int(numero1Input.get())
    num2 = int(numero2Input.get())
    soma = num1 + num2
    print(soma)
    numero1Input.delete(0, END)
    numero2Input.delete(0, END)
    numero1Input.focus()


botao = Button(janelinha, text='Somar', command=soma)
botao.pack()

janelinha.mainloop()

