#Importações
from tkinter import *
#from tkinter import ttk

#Estrutura
janela = Tk()
janela.title("Calculadora")
janela.geometry("390x450")
janela.config(bg="gray")

#Display
frame_ultimo=Frame(janela,width=390, height=20, bg="blue")
frame_ultimo.grid(row=0, column=0,)
frame_tela=Frame(janela,width=390, height=50,bg="black")
frame_tela.grid(row=1, column=0,)

#Label
valor=StringVar()
app_ultimo=Label(frame_ultimo,text="12345", width=30, height=0,justify="right", relief=FLAT, anchor="n", bg="red",font=('Ani 12'), fg="white")
app_ultimo.place(x=0, y=0)
app_label=Label(frame_tela,textvariable=valor, width=18, height=1, padx=10, relief=FLAT, anchor="e", bg="black",font=('Ani 24 bold'), fg="white")
app_label.place(x=0, y=2)



#Funções
digito=""

def Calcular(event):
    global digito
    digito=digito + str(event)
    valor.set(digito)

def Clear(): 
    global digito
    digito=""
    valor.set("0")

def Total():
    resultado= eval(digito)
    print(resultado)
    valor.set(resultado)

#Botões
frame_botoes=Frame(janela,width=390, height=380,bg="gray")
frame_botoes.grid(row=2, column=0,)

# -> 1ª linha
b_1=Button(frame_botoes, command= Clear, text="C", width=20, height=3, bg="gold")
b_1.place(x=4, y=5)
b_2=Button(frame_botoes, text="M", width=8, height=3, bg="gold")
b_2.place(x=197, y=5)
b_3=Button(frame_botoes, command= lambda:Calcular("/"), text="/", width=8, height=3, bg="Navy blue", fg="white")
b_3.place(x=294, y=5)

# -> 2ª linha
b_4=Button(frame_botoes, command= lambda:Calcular("7"), text="7", width=8, height=3, bg="gray")
b_4.place(x=4, y=74)
b_5=Button(frame_botoes, command= lambda:Calcular("8"), text="8", width=8, height=3, bg="gray")
b_5.place(x=100, y=74)
b_6=Button(frame_botoes, command= lambda:Calcular("9"), text="9", width=8, height=3, bg="gray")
b_6.place(x=197, y=74)
b_7=Button(frame_botoes, command= lambda:Calcular("*"), text="*", width=8, height=3, bg="Navy blue", fg="white")
b_7.place(x=294, y=74)

# -> 3ª linha
b_8=Button(frame_botoes, command= lambda:Calcular("4"), text="4", width=8, height=3, bg="gray")
b_8.place(x=4, y=144)
b_9=Button(frame_botoes, command= lambda:Calcular("5"), text="5", width=8, height=3, bg="gray")
b_9.place(x=100, y=144)
b_10=Button(frame_botoes, command= lambda:Calcular("6"), text="6", width=8, height=3, bg="gray")
b_10.place(x=197, y=144)
b_11=Button(frame_botoes, command= lambda:Calcular("-"), text="-", width=8, height=3, bg="Navy blue", fg="white")
b_11.place(x=294, y=144)

# -> 4ª linha
b_12=Button(frame_botoes, command= lambda:Calcular("1"), text="1", width=8, height=3, bg="gray")
b_12.place(x=4, y=214)
b_13=Button(frame_botoes, command= lambda:Calcular("2"), text="2", width=8, height=3, bg="gray")
b_13.place(x=100, y=214)
b_14=Button(frame_botoes, command= lambda:Calcular("3"), text="3", width=8, height=3, bg="gray")
b_14.place(x=197, y=214)
b_15=Button(frame_botoes, command= lambda:Calcular("+"), text="+", width=8, height=3, bg="Navy blue", fg="white")
b_15.place(x=294, y=214)

# -> 5ª linha
b_16=Button(frame_botoes, command= lambda:Calcular("0"), text="0", width=8, height=4, bg="gray")
b_16.place(x=4, y=284)
b_17=Button(frame_botoes, command= lambda:Calcular("%"), text="%", width=8, height=4, bg="Navy blue", fg="white")
b_17.place(x=100, y=284)
b_18=Button(frame_botoes, command= Total, text="=", width=20, height=4, bg="gold")
b_18.place(x=197, y=284)




    
    
janela.mainloop()