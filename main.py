from tkinter import * # Importando as funcionalidades do GUI Tkinter.
import string #Para gerar a senha
from random import random,choice
import pyperclip

root = Tk()
img = PhotoImage(file="foto_cadeado.png")  # Importando foto pra img

class Functions():

    def gerar_senha(self):
        #Constantes de string
        valores =  string.ascii_letters  # Todas letras
        valores += string.digits # Números de 0 a 9
        valores += string.punctuation  #Sequência de caracteres ASCII
        tamanho = 10
        global senha
        senha = " "

        


        for x in range(tamanho):
            senha += choice(valores)
            self.lbl_result['text'] = senha
            self.lbl_aviso['text'] = " "

    def notificar(self):
        self.lbl_aviso['text'] = "Senha copiada para transferência"
        pyperclip.copy( senha )


class Application(Functions):
    def __init__(self):  # Inicializando tudo

        self.root = root 
        self.configuracoes_tela()
        self.widget_tela()
        root.mainloop()

    def configuracoes_tela(self):  # Função contendo configurações da janela
        self.root.title("Gerador de senhas")  # Título da tela
        self.root.configure(bg='#1f1f2e') # Cor de fundo
        self.root.geometry("400x180") #Resolução da tela

        self.root.resizable(False, False)  # Redimensionavel? (horizontal, vertical) NÃO!

    def widget_tela(self):
        # label 
        self.lb = Label(self.root, text="Sugestão de senha:", bg= '#1f1f2e', fg = 'white')
        self.lb.place(relx=0.5, rely=0.06)

        #criando um frame.  
        self.frame_1 = Frame(self.root, bd=4, bg='#1f1f2e',
                             highlightbackground='#759fe6', highlightthickness=1)
        self.frame_1.place(relx=0.5, rely=0.25, relwidth=0.32, relheight=0.15)



        #atribuindo a foto a lbl_foto
        self.lbl_foto = Label(self.root, image=img)
        self.lbl_foto.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.7)

        #lbl pra exibir o resultado da senha
        self.lbl_result = Label(self.root, bg='#1f1f2e', fg='white')
        self.lbl_result.place(relx=0.55, rely=0.27)



        # Botões         # onde está?  |   cor     |  texto   | cor letra  | Quando clicar puxa a função gerar_senha
        self.btn_ok = Button(self.root, bg='black', text= "OK", fg='white', command = self.notificar)
        self.btn_ok.place(relx=0.5, rely=0.50, relwidth=0.15)

        #botao cancel
        self.btn_cancel = Button(self.root, bg='black', text= "Cancel", fg='white', command=self.gerar_senha)
        self.btn_cancel.place(relx=0.67, rely=0.50, relwidth=0.15)


        #lbl aviso
        self.lbl_aviso = Label(self.root, bg='#1f1f2e', fg='white')
        self.lbl_aviso.place(relx=0.5, rely=0.7)



Application()
