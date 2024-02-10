import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
import os

def gerar_qrcode():
    dados = entry.get()
    if dados:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(dados)
        qr.make(fit=True)

        imagem_qr = qr.make_image(fill_color="black", back_color="white")
        imagem_qr.save("qrcode.png")
        
        imagem = Image.open("qrcode.png")
        imagem = imagem.resize((200, 200))
        imagem = ImageTk.PhotoImage(imagem)
        label_qr_code.config(image=imagem)
        label_qr_code.image = imagem
        
        label_status.config(text="QR code gerado com sucesso!")
        
        instrucao_camera.config(text="Aponte a câmera do celular para a imagem para verificar o QR code.")
    else:
        label_status.config(text="Por favor, insira os dados para o QR code!")

def salvar_imagem():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
    if caminho_arquivo:
        os.rename("qrcode.png", caminho_arquivo)
        label_status.config(text=f"Imagem salva como: {caminho_arquivo}")





root = tk.Tk()
root.title("Gerador de QR Code")


fonte_instrucao = ("Arial", 10)
fonte_botao = ("Arial", 12, "bold")





label_instrucao = tk.Label(root, text="Digite os dados para o QR code (números, letras, etc.):", font=fonte_instrucao)
label_instrucao.pack(pady=(10, 5))

entry = tk.Entry(root, width=40, font=fonte_instrucao)
entry.pack(pady=5)

button_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qrcode, font=fonte_botao)
button_gerar.pack(pady=5)

label_status = tk.Label(root, text="", font=fonte_instrucao)
label_status.pack(pady=5)

label_qr_code = tk.Label(root)
label_qr_code.pack(pady=5)

button_salvar = tk.Button(root, text="Salvar Imagem", command=salvar_imagem, font=fonte_botao)
button_salvar.pack(pady=5)

instrucao_camera = tk.Label(root, text="", font=fonte_instrucao)
instrucao_camera.pack(pady=5)




largura_janela = 420
altura_janela = 480
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


root.mainloop()


def salvar_imagem():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
    if caminho_arquivo:
        imagem_qr = Image.open("qrcode.png")
        imagem_qr.save(caminho_arquivo)
        label_status.config(text=f"Imagem salva como: {caminho_arquivo}")
        os.remove("qrcode.png")

