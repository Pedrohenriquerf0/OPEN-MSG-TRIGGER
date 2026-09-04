import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from application.repositories import data
from application.services.whatsapp_sender import (
    whatsapp_sender_img,
    whatsapp_sender_msg
)
from application.utils.directory_utils import (
    select_xlsx,
    find_json_files,
    directory_json
)
from application.utils.image_utils import find_imagem


def main():

    # ==========================================================
    # CONFIGURAÇÃO
    # ==========================================================

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("600x750")
    app.title("OPEN MSG TRIGGER")

    # ==========================================================
    # CONTAINER PRINCIPAL
    # ==========================================================

    card_acoes = ctk.CTkFrame(app)
    card_acoes.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    # ==========================================================
    # TÍTULO
    # ==========================================================

    lbl_titulo = ctk.CTkLabel(
        card_acoes,
        text="OPEN MSG TRIGGER",
        font=("Arial", 24, "bold")
    )
    lbl_titulo.pack(pady=(20, 5))

    lbl_subtitulo = ctk.CTkLabel(
        card_acoes,
        text="Envio de mensagens pelo WhatsApp",
        font=("Arial", 13)
    )
    lbl_subtitulo.pack(pady=(0, 15))

    # ==========================================================
    # CARD MENSAGEM
    # ==========================================================

    card_mensagem = ctk.CTkFrame(card_acoes)
    card_mensagem.pack(
        fill="x",
        padx=15,
        pady=8
    )

    lbl_msg = ctk.CTkLabel(
        card_mensagem,
        text="MENSAGEM",
        font=("Arial", 14, "bold")
    )
    lbl_msg.pack(
        anchor="w",
        padx=15,
        pady=(12, 5)
    )

    entry_msg = ctk.CTkEntry(
        card_mensagem,
        placeholder_text="Digite sua mensagem aqui...",
        height=40
    )
    entry_msg.pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    # ==========================================================
    # CARD CONTATOS
    # ==========================================================

    card_contatos = ctk.CTkFrame(card_acoes)
    card_contatos.pack(
        fill="x",
        padx=15,
        pady=8
    )

    lbl_contatos = ctk.CTkLabel(
        card_contatos,
        text="CONTATOS",
        font=("Arial", 14, "bold")
    )
    lbl_contatos.pack(
        anchor="w",
        padx=15,
        pady=(12, 5)
    )

    lbl_arquivo = ctk.CTkLabel(
        card_contatos,
        text="Arquivo de contatos:"
    )
    lbl_arquivo.pack(
        anchor="w",
        padx=15,
        pady=(5, 3)
    )

    # ==========================================================
    # COMBOBOX
    # ==========================================================

    def combobox_callback(choice):

        if choice == "Nenhum JSON encontrado":
            data.PATH_JSON = None
            return

        data.PATH_JSON = directory_json() / choice


        status_var.set(
            f"JSON selecionado: {choice}"
        )

    arquivos_json = find_json_files()

    nomes_json = [
        arquivo.name
        for arquivo in arquivos_json
    ]

    if nomes_json:

        combobox = ctk.CTkComboBox(
            card_contatos,
            values=nomes_json,
            command=combobox_callback,
            width=300
        )

        combobox.set(nomes_json[0])

        data.PATH_JSON = directory_json() / nomes_json[0]

    else:

        combobox = ctk.CTkComboBox(
            card_contatos,
            values=["Nenhum JSON encontrado"],
            width=300
        )

        combobox.set("Nenhum JSON encontrado")

        data.PATH_JSON = None

    combobox.pack(
        padx=15,
        pady=5
    )

    # ==========================================================
    # FUNÇÃO ATUALIZAR COMBOBOX
    # ==========================================================

    def update_combobox():

        arquivos_json = find_json_files()

        nomes_json = [
            arquivo.name
            for arquivo in arquivos_json
        ]

        if nomes_json:

            combobox.configure(
                values=nomes_json
            )

            # Seleciona o último JSON encontrado.
            # Normalmente será o que acabou de ser criado.
            combobox.set(nomes_json[-1])

            data.PATH_JSON = (
                directory_json() / nomes_json[-1]
            )

            status_var.set(
                f"Contatos carregados: {nomes_json[-1]}"
            )

        else:

            combobox.configure(
                values=["Nenhum JSON encontrado"]
            )

            combobox.set(
                "Nenhum JSON encontrado"
            )

            data.PATH_JSON = None

            status_var.set(
                "Nenhum arquivo JSON encontrado"
            )

    # ==========================================================
    # BOTÕES DE CONTATOS
    # ==========================================================

    frame_botoes_contatos = ctk.CTkFrame(
        card_contatos,
        fg_color="transparent"
    )
    frame_botoes_contatos.pack(
        pady=(5, 15)
    )

    btn_xlsx = ctk.CTkButton(
        frame_botoes_contatos,
        text="Carregar Planilha",
        command=select_xlsx,
        width=140
    )
    btn_xlsx.pack(
        side="left",
        padx=5
    )

    btn_update = ctk.CTkButton(
        frame_botoes_contatos,
        text="Atualizar",
        command=update_combobox,
        width=100
    )
    btn_update.pack(
        side="left",
        padx=5
    )

    # ==========================================================
    # CARD IMAGEM
    # ==========================================================

    card_imagem = ctk.CTkFrame(card_acoes)
    card_imagem.pack(
        fill="x",
        padx=15,
        pady=8
    )

    lbl_imagem = ctk.CTkLabel(
        card_imagem,
        text="IMAGEM",
        font=("Arial", 14, "bold")
    )
    lbl_imagem.pack(
        anchor="w",
        padx=15,
        pady=(12, 5)
    )

    # ==========================================================
    # CHECKBOX
    # ==========================================================

    def checkbox_event():

        if check_var.get() == "on":

            btn_img.configure(
                state="normal"
            )

            status_var.set(
                "Envio com imagem ativado"
            )

        else:

            btn_img.configure(
                state="disabled"
            )

            status_var.set(
                "Envio somente de mensagem"
            )

    check_var = ctk.StringVar(
        value="on"
    )

    checkbox = ctk.CTkCheckBox(
        card_imagem,
        text="Ativar Imagem",
        command=checkbox_event,
        variable=check_var,
        onvalue="on",
        offvalue="off"
    )
    checkbox.pack(
        anchor="w",
        padx=15,
        pady=5
    )

    btn_img = ctk.CTkButton(
        card_imagem,
        text="Carregar Imagem",
        command=find_imagem,
        width=180
    )
    btn_img.pack(
        pady=(5, 15)
    )

    # ==========================================================
    # CARD STATUS
    # ==========================================================

    card_status = ctk.CTkFrame(card_acoes)
    card_status.pack(
        fill="x",
        padx=15,
        pady=8
    )

    lbl_status_titulo = ctk.CTkLabel(
        card_status,
        text="STATUS",
        font=("Arial", 14, "bold")
    )
    lbl_status_titulo.pack(
        anchor="w",
        padx=15,
        pady=(12, 5)
    )

    status_var = ctk.StringVar(
        value="Pronto para iniciar"
    )

    lbl_status = ctk.CTkLabel(
        card_status,
        textvariable=status_var,
        font=("Arial", 13)
    )
    lbl_status.pack(
        anchor="w",
        padx=15,
        pady=(0, 12)
    )

    # ==========================================================
    # INICIAR
    # ==========================================================

    def start():

        # ------------------------------------------------------
        # VERIFICAR JSON
        # ------------------------------------------------------

        if data.PATH_JSON is None:

            CTkMessagebox(
                title="Erro",
                message="Nenhum arquivo JSON foi selecionado.",
                icon="cancel"
            )

            status_var.set(
                "Erro: nenhum JSON selecionado"
            )

            return

        # ------------------------------------------------------
        # VERIFICAR MENSAGEM
        # ------------------------------------------------------

        data.MESSAGE = entry_msg.get()

        if not data.MESSAGE.strip():

            CTkMessagebox(
                title="Erro",
                message="Digite uma mensagem antes de iniciar.",
                icon="cancel"
            )

            status_var.set(
                "Erro: mensagem não preenchida"
            )

            return

        # ------------------------------------------------------
        # STATUS
        # ------------------------------------------------------

        status_var.set(
            "Enviando mensagens..."
        )

        app.update_idletasks()

        try:

            # --------------------------------------------------
            # ENVIO COM IMAGEM
            # --------------------------------------------------

            if check_var.get() == "on":

                whatsapp_sender_img()

            # --------------------------------------------------
            # ENVIO SOMENTE MENSAGEM
            # --------------------------------------------------

            else:

                whatsapp_sender_msg()

            # --------------------------------------------------
            # FINALIZADO
            # --------------------------------------------------

            status_var.set(
                "Envio concluído!"
            )

        except Exception as error:

            print("Erro durante o envio:", error)

            status_var.set(
                "Erro durante o envio"
            )

            CTkMessagebox(
                title="Erro",
                message=f"Ocorreu um erro durante o envio:\n\n{error}",
                icon="cancel"
            )

    # ==========================================================
    # BOTÃO INICIAR
    # ==========================================================

    btn_iniciar = ctk.CTkButton(
        card_acoes,
        text="INICIAR ENVIO",
        command=start,
        height=45,
        font=("Arial", 14, "bold")
    )
    btn_iniciar.pack(
        fill="x",
        padx=50,
        pady=15
    )

    # ==========================================================

    app.mainloop()