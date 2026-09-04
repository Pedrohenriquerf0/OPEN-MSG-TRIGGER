from tkinter import filedialog
from application.repositories import data


def find_imagem():

    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
    )

    if caminho_imagem:
        data.PATH_IMAGE = caminho_imagem


