
import json
import os

from application.repositories import data
from application.utils import directory_utils

list_contacts = []

def validator(nome, telefone):


    PATH_JSON = directory_utils.directory_json() / f"{data.PATH_XLSX.stem}.json"

    os.makedirs(os.path.dirname(PATH_JSON), exist_ok=True)

    if (len(telefone) != 11):
        return
    elif (telefone[2] != '9'):
        return


    contact = {
        "nome": nome,
        "telefone": telefone
    }

    list_contacts.append(contact)


    with open(PATH_JSON, 'w', encoding='utf-8') as arq:
        json.dump(list_contacts, arq,indent=2, ensure_ascii=False)




