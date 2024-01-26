from tkinter import *
import datetime
from datetime import datetime
anoAtual = datetime.now().year


caixa = Tk()
caixa.title("Maior de Idade?")
caixa.geometry('230x430')

dataDeNascimento_Label = Label(text='Digite o ano de nascimento:')
dataDeNascimento_Label.pack()
dataDeNascimento_Input = Entry()
dataDeNascimento_Input.pack()

nomeDoSujeito_Label = Label(text='Digite o nome do sujeito: ')
nomeDoSujeito_Label.pack()
nomeDoSujeito_Input = Entry()
nomeDoSujeito_Input.pack()

def verificar():
    data = int(dataDeNascimento_Input.get())
    nome = nomeDoSujeito_Input.get()
    resultado = anoAtual - data
    if resultado < 1:
        print('0 anos?! Pode prender esse viajante do futuro!')
    elif resultado < 18 and resultado > 0:
        print(f'O {nome} não pode ser preso, ele tem {resultado} anos!')
    else:
        print(f'O {nome} já pode ser preso. Ele tem {resultado} anos.')
    dataDeNascimento_Input.delete(0,END)
    nomeDoSujeito_Input.delete(0,END)
    dataDeNascimento_Input.focus()

botao = Button(caixa, text="Ver se pode ser preso", command= verificar)
botao.pack()


caixa.mainloop()