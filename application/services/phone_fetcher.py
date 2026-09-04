from application.services import phone_validator
from application.repositories import data
import openpyxl


def phone_fetcher():

    if not data.PATH_XLSX:
        return

    sheet = openpyxl.load_workbook(
        data.PATH_XLSX,
        read_only=True
    )

    tab = sheet.active

    for line in tab.iter_rows(min_row=2, values_only=True):

        if not line[0] or not line[1]:
            continue

        nome = str(line[0]).strip()
        telefone = str(line[1]).strip()

        phone_validator.validator(nome, telefone)


    sheet.close()
# PADRAO DE PLANILHA E NOME, COLUNA 1  E NUMERO, COLUNA 2 DE CONTATO COM DDD, EX: 99999999999
