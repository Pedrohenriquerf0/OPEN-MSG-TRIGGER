import json
import pywhatkit


from application.utils.phone_updater import setNumber
from application.repositories import data



def whatsapp_sender_msg():
    message = data.MESSAGE
    with open(data.PATH_JSON, "r", encoding="utf-8") as arq:
        contacts = json.load(arq)

    for contact in contacts:
        nome = contact["nome"]
        telefone = setNumber(contact["telefone"])

        pywhatkit.sendwhatmsg_instantly(telefone, message)


def whatsapp_sender_img():
    message = data.MESSAGE
    image = data.PATH_IMAGE

    with open(data.PATH_JSON, "r", encoding="utf-8") as arq:
        contacts = json.load(arq)

    for contact in contacts:
        nome = contact["nome"]
        telefone = setNumber(contact["telefone"])

        pywhatkit.sendwhats_image(telefone, image, caption=message)

