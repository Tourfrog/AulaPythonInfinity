from tkinter import *

janelinha = Tk()

janelinha.title('Aula 1 TK')
janelinha.geometry('400x400')

usuarioLabel = Label(text='Digite o seu nome de usuário: ')
usuarioLabel.pack()

usuarioInput = Entry()
usuarioInput.pack()

idadeLabel = Label(text='Digite a sua idade: ')
idadeLabel.pack()

idadeInput = Entry()
idadeInput.pack()

def saudar():
    nome = usuarioInput.get()
    idade = int(idadeInput.get())
    futuraIdade = idade + 5
    print(f'''Bem vindo, {nome}! Sua idade daqui à 5 anos será: {futuraIdade}!''')

botao = Button(janelinha, text='Enviar', command=saudar)
botao.pack()

janelinha.mainloop()