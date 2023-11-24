from tkinter import *

from PIL import Image, ImageTk


janela = Tk()

janela.title('Caixa Eletrônico')
janela.geometry('500x380')
janela.configure(bg='blue')#cor de fundo da tela
#enfeitar janela

saldoAtual = 5000

#nome = input('Nome:')
nome = 'Bart'

introducao = Label(janela, text=f'Bem_vindo(a) ao caixa eletrônico , senhor(a) {nome.title()}', font=1)
introducao.grid(column=1, row=0, padx=5, pady=10)#indica a posicao desse elemento

#posicinando cartao
img = ImageTk.PhotoImage(Image.open('bancoImagem.png'))
imagem = Label(janela, image=img)
imagem.grid(column=1, row=2)

#criando botoes
botao1 = Button(janela, text='Saldo', height=3 , width=8)
botao1.grid(column=0, row=1, padx=3 , pady=1)



janela.mainloop()
