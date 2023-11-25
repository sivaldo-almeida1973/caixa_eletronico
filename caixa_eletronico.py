from tkinter import *

from PIL import Image, ImageTk
import time

janela = Tk()

janela.title('Caixa Eletrônico')
janela.geometry('500x380')
janela.configure(bg='blue')#cor de fundo da tela
#enfeitar janela

saldoAtual = 5000
saqueTotal = 0 #variavel respons pelo controle do valor sacado
saque_pagar = True  #saque recebe True e pagar vai receber False
deposito_celular = True #deposito recebe True e celular vai receber False

def Saldo():
  conclusao['text'] = f'Seu saldo atual: R$ {saldoAtual}'
  janela.update()  #atualiza 
  normalizar() #chama função normalizar
  
def saque():
  global saque_pagar
  conclusao['text'] = f'Quanto deseja sacar?'
  saque_pagar = True
  botoesValores()

def botoesValores():
  botao1['text'] = '50'
  botao1['command'] = saque50
  botao2['text'] = '100'
  botao2['command'] = saque100
  botao3['text'] = '500'
  botao3['command'] = saque500
  botao4['text'] = '1000'
  botao4['command'] = saque1000
  botao5['text'] = '5000'
  botao5['command'] = saque5000
  botao6['text'] = 'Confirmar'
  botao6['command'] = confirmarSaque
  janela.update()  #atualiza 

#criar funçoes de saques
def saque50():
  global saqueTotal
  saqueTotal += 50
  conclusao['text'] = f'Valor: R$ {saqueTotal}'
  janela.update()

def saque100():
  global saqueTotal
  saqueTotal += 100
  conclusao['text'] = f'Valor: R$ {saqueTotal}'
  janela.update()

def saque500():
  global saqueTotal
  saqueTotal += 500
  conclusao['text'] = f'Valor: R$ {saqueTotal}'
  janela.update()

def saque1000():
  global saqueTotal
  saqueTotal += 1000
  conclusao['text'] = f'Valor: R$ {saqueTotal}'
  janela.update()

def saque5000():
  global saqueTotal
  saqueTotal += 5000
  conclusao['text'] = f'Valor: R$ {saqueTotal}'
  janela.update()

def confirmarSaque():
  global saqueTotal, saldoAtual, saque_pagar
  if saqueTotal > saldoAtual:
    conclusao['text'] = 'Saldo Insuficiente!'
    saqueTotal = 0
  else:
    saldoAtual -= saqueTotal
    if saque_pagar:
      conclusao['text'] = f'Saque de R$ {saqueTotal} realizado com sucesso!'
    else:
      conclusao['text'] = f'Pagamento de R$ {saqueTotal} realizado com sucesso!'
    saqueTotal = 0
  janela.update()  
  time.sleep(1)
  normalizar() #chamar a função nornalizar

#funcao que faz voltar tudo para o começo
def normalizar():
  time.sleep(2)
  conclusao['text'] = 'Deseja realizar alguma operação? '
  botao1['text'] = 'Saldo'
  botao1['command'] = Saldo
  botao2['text'] = 'Saque'
  botao2['command'] = saque
  botao3['text'] = 'Pagar\nConta'
  botao3['command'] = pagar
  botao4['text'] = 'Deposito'
  botao4['command'] = deposito
  botao5['text'] = 'Desb.\nCelular'
  botao5['command'] = desbloquear
  botao6['text'] = 'Sair'
  botao6['command'] = sair
  janela.update()  #atualiza 

#funcao pagar------------------------------
def pagar():
  global saque_pagar
  conclusao['text'] = f'Qual o valor do pagamento?'
  saque_pagar = False
  botoesValores()

caixa = None #variavel global
#funcao deposito---------------------------
def deposito():
  global deposito_celular, caixa
  if deposito_celular:
    conclusao['text'] = 'Qual o valor do deposito?'
  else:
    conclusao['text'] = 'Digite seu numero: '
  botao1['state'] = DISABLED
  botao2['state'] = DISABLED
  botao3['state'] = DISABLED
  botao4['state'] = DISABLED
  botao5['state'] = DISABLED
  botao6['text'] = 'Confirmar'
  botao6['command'] = confirmarDeposito
  caixaTexto = Entry(janela, font='arial 15')
  caixaTexto.grid(column=1, row=5)
  caixa = caixaTexto


def confirmarDeposito():
  global caixa , saldoAtual, deposito_celular
  if caixa.get().isnumeric():
    valorDeposito = int(caixa.get())#faz cast para inteiro
    if deposito_celular:
      saldoAtual += valorDeposito
      conclusao['text'] = f'Valor de R$ {valorDeposito} deposito com sucesso!'
    else:
      conclusao['text'] = f'O numero {valorDeposito} foi cadastrado com sucesso!'
  else:
    if deposito_celular:
     conclusao['text'] = 'valor invalido!'
    else:
      conclusao['text'] = 'Numero invalido!'
  deposito_celular = True
  caixa.destroy()
  janela.update()
  botao1['state'] = NORMAL
  botao2['state'] = NORMAL
  botao3['state'] = NORMAL
  botao4['state'] = NORMAL
  botao5['state'] = NORMAL
  normalizar()

#criar funcao desbloquear celular
def desbloquear():
  global deposito_celular
  deposito_celular = False
  deposito() #chamar funcao deposito

 
def sair():
  quit()

nome = input('Nome:')


introducao = Label(janela, text=f'Bem_vindo(a) ao caixa eletrônico , senhor(a) {nome.title()}', font='arial 12')
introducao.grid(column=1, row=0, padx=5, pady=10)#indica a posicao desse elemento

#posicinando cartao
img = ImageTk.PhotoImage(Image.open('bancoImagem.png'))
imagem = Label(janela, image=img)
imagem.grid(column=1, row=2)


#criando botoes
botao1 = Button(janela, text='Saldo',command=Saldo, height=3 , width=8)
botao1.grid(column=0, row=1, padx=3 , pady=1)

botao2 = Button(janela, text='Saque', command=saque, height=3, width=8)
botao2.grid(column=0, row=2, padx=3, pady=1)

botao3 = Button(janela, text='Pagar\nConta', command=pagar, height=3, width=8)
botao3.grid(column=0, row=3, padx=3 , pady=1)

botao4 = Button(janela, text='Deposito',command=deposito, height=3 , width=8)
botao4.grid(column=2, row=1, padx=0 , pady=1)

botao5 = Button(janela, text='Desb.\nCelular', command=desbloquear, height=3, width=8)
botao5.grid(column=2, row=2, padx=0, pady=1)

botao6 = Button(janela, text='Sair', command=sair, height=3, width=8)
botao6.grid(column=2, row=3, padx=0 , pady=1)

conclusao = Label(janela, text='Deseja realizar alguma operação? ',font='arial 12')
conclusao.grid(column=1, row=4, padx=10, pady=15)


janela.mainloop()
