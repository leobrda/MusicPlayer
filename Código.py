# Importando tkinter
from tkinter import *

# Importando pillow
from PIL import Image, ImageTk

# Importando pygame
import pygame
from pygame import mixer

import os

# Cores
cor0 = '#f0f3f5'  # cinza
cor1 = '#feffff'  # braca
cor2 = '#3fb5a3'  # verde
cor3 = '#2e2d2c'  # preta
cor4 = '#403d3d'  # preta
cor5 = '#4a88e8'  # azul

# Criando a janela
janela = Tk()
janela.title('Music Player')
janela.geometry('352x255')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Frames
frame_esquerda = Frame(janela, width=150, height=150, bg=cor3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=250, height=150, bg=cor3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=404, height=100, bg=cor3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

# Configurando frame esquerda
img_1 = Image.open('Imagens/imagem.png')
img_1 = img_1.resize((139, 139))
img_1 = ImageTk.PhotoImage(img_1)

label_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0, anchor='nw',
                   font=('ivy 16 bold'), bg=cor3, fg=cor3)
label_logo.place(x=15, y=9)


# Criando funções
def play_musica():
    rodando = listbox.get(ACTIVE)
    label_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()


def pausar_musica():
    mixer.music.pause()


def continuar_musica():
    mixer.music.unpause()


def parar_musica():
    mixer.music.stop()


def proxima_musica():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

    # Deletando os elementos na playlist
    listbox.delete(0, END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text'] = tocando


def musica_anterior():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

    # Deletando os elementos na playlist
    listbox.delete(0, END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text'] = tocando


# Configurando o frame direita
listbox = Listbox(frame_direita, selectmode=SINGLE, font=('arial 10 bold'), width=22, height=10, bg=cor3, fg=cor1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


# Configurando o frame baixo
label_rodando = Label(frame_baixo, text='Escolha a música na lista', width=44, justify=LEFT,
                      anchor='nw', font=('ivy 10'), bg=cor1, fg=cor4)
label_rodando.place(x=0, y=1)

# BOTÃO ANTERIOR
img_2 = Image.open('Imagens/2.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
b_anterior = Button(frame_baixo, command=musica_anterior, width=40, height=40, image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,
                    bg=cor3, fg=cor4)
b_anterior.place(x=34, y=28)

# BOTÃO PLAY
img_3 = Image.open('Imagens/3.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo, command=play_musica, width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,
                    bg=cor3, fg=cor4)
b_play.place(x=81, y=28)

# BOTÃO PRÓXIMA
img_4 = Image.open('Imagens/4.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
b_play = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,
                    bg=cor3, fg=cor4)
b_play.place(x=128, y=28)

# BOTÃO PAUSAR
img_5 = Image.open('Imagens/5.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
b_play = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,
                    bg=cor3, fg=cor4)
b_play.place(x=175, y=28)

# BOTÃO DESPAUSAR
img_7 = Image.open('Imagens/7.png')
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
b_play = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor4)
b_play.place(x=222, y=28)

# BOTÃO STOP
img_6 = Image.open('Imagens/6.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
b_play = Button(frame_baixo, command=parar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,
                    bg=cor3, fg=cor4)
b_play.place(x=269, y=28)

# Selecionando a pasta quem contém as músicas
os.chdir(r'C:\Users\leona\Downloads\Músicas')
musicas = os.listdir()
print(musicas)


# Função para mostrar as músicas da pasta
def mostrar():
    for i in musicas:
        listbox.insert(END, i)


mostrar()

# Inicializando o mixer
mixer.init()
janela.mainloop()
