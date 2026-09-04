from pathlib import Path
from tkinter import filedialog

from application.repositories import data
from application.services import phone_fetcher

def directory_json():
    return Path.home() / "Dados MSG Trigger"



def select_xlsx():
    caminho_diretorio = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Excel", "*.xlsx *.xls")]
    )

    if caminho_diretorio:
        data.PATH_XLSX = Path(caminho_diretorio)
        phone_fetcher.phone_fetcher()



def find_json_files():
    diretorio = Path(directory_json())

    arquivos_json = list(diretorio.glob("*.json"))

    return arquivos_json