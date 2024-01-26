from tkinter import *

janela = Tk()
janela.title('Passou de Ano?')
janela.geometry('400x400')
janela.configure(bg='lightpink')

nota1_Label = Label(text='Digite a primeira nota', font=('Arial', 15, 'italic'), height=2, bg='lightpink')
nota1_Label.pack()
nota1_Input = Entry()
nota1_Input.pack()

erro1_Label = Label(text='', bg='lightpink')
erro1_Label.pack()

nota2_Label = Label(text='Digite a segunda nota', font=('Arial', 15, 'italic'), height=2, bg='lightpink')
nota2_Label.pack()
nota2_Input = Entry()
nota2_Input.pack()

erro2_Label = Label(text='', bg='lightpink')
erro2_Label.pack()

nota3_Label = Label(text='Digite a terceira nota', font=('Arial', 15, 'italic'), height=2, bg='lightpink')
nota3_Label.pack()
nota3_Input = Entry()
nota3_Input.pack()

erro3_Label = Label(text='', bg='lightpink')
erro3_Label.pack()

def mediaDasNotas():
    nota1 = float(nota1_Input.get())
    nota2 = float(nota2_Input.get())
    nota3 = float(nota3_Input.get())

    if nota1 < 0 or nota1 > 10:
        erro1_Label.configure(text='Digite uma nota válida', fg='red')
    elif nota2 < 0 or nota2 > 10:
        erro2_Label.configure(text='Digite uma nota válida', fg='red')
    elif nota3 < 0 or nota3 > 10:
        erro3_Label.configure(text='Digite uma nota válida', fg='red')
    else:
        media = (nota1 + nota2 + nota3) / 3

        if media < 0 or media > 10:
            resultado_Label.configure(text='ERROR', bg='gray', font=('Arial', 14, 'bold'))
        elif media == 10:
            resultado_Label.configure(text='Aprovado com distinção', bg='blue', font=('Arial', 14, 'bold'))
        elif media >= 7 and media < 10:
            resultado_Label.configure(text='Aprovado', bg='green', font=('Arial', 14, 'bold'))
        else: 
            resultado_Label.configure(text='Reprovado', bg='red', font=('Arial', 14, 'bold'))
    
    nota1_Input.delete(0, END)
    nota2_Input.delete(0, END)
    nota3_Input.delete(0, END)
    nota1_Input.focus()
    

# espacoLabel = Label(text='', bg='lightpink')
# espacoLabel.pack()

botao = Button(janela, text='Verificar se passou', command=mediaDasNotas, bg='brown', font=('Verdana', 10))
botao.pack(pady=10)

resultado_Label = Label(text='', bg='lightpink')
resultado_Label.pack(pady=10)

janela.mainloop()