# OPEN MSG TRIGGER 🚀

> Disparador automatizado de mensagens para WhatsApp via planilha Excel em Python.

O **OPEN MSG TRIGGER** é um script *open-source* desenvolvido em Python para automatizar o envio de mensagens no WhatsApp a partir de dados organizados em planilhas Excel (`.xlsx`). O script lê os dados da planilha, converte-os internamente para a estrutura `JSON` e realiza os disparos através do WhatsApp Web.

---

## ⚠️ AVISO IMPORTANTE E ISENÇÃO DE RESPONSABILIDADE

**O USO INADEQUADO DESTA FERRAMENTA PODE RESULTAR NO BANIMENTO DA SUA CONTA DO WHATSAPP.**

* O envio de mensagens em massa não solicitadas viola os [Termos de Serviço do WhatsApp](https://www.whatsapp.com/legal/terms-of-service).
* Certifique-se de utilizar a ferramenta apenas para envio de mensagens autorizadas ou para contatos que já possuem interação prévia com o seu número.
* Os desenvolvedores deste projeto **não se responsabilizam** por eventuais bloqueios, suspensões ou banimentos de contas de WhatsApp decorrentes do uso do código.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **[Python 3.x](https://www.python.org/):** Linguagem de programação principal do projeto.
* **[customtkinter](https://github.com/TomSchimansky/CustomTkinter):** Interface gráfica moderna e customizável para o usuário.
* **[CTkMessagebox](https://github.com/Akascape/CTkMessagebox):** Exibição de caixas de diálogo, alertas e mensagens estilizadas na interface.
* **[openpyxl](https://openpyxl.readthedocs.io/):** Leitura, manipulação e extração de dados da planilha Excel (`.xlsx`).
* **[pywhatkit](https://github.com/AnkitPiris/pywhatkit):** Automação para abertura do WhatsApp Web e envio das mensagens.
* **[pywin32](https://github.com/mhammond/pywin32) / `win32`:** Integração com APIs nativas do sistema operacional Windows para controle de janelas e processos.
* **`os`:** Módulo nativo do Python para manipulação de arquivos e caminhos do sistema.

## 📋 Pré-requisitos

Para que o script funcione corretamente, o seu ambiente deve atender aos seguintes requisitos:

1. **WhatsApp Web Conectado:** O seu navegador padrão (Google Chrome, Microsoft Edge, etc.) deve estar previamente logado e com a sessão ativa no [WhatsApp Web](https://web.whatsapp.com).
2. **Formatação dos Números:** Os números na planilha devem estar completos, incluindo o Código do País (DDI), Código de Área (DDD) e o número do celular.
   * *Exemplo para o Brasil:* `11999998888`.
3. **Ambiente Python:** Python 3.14 ou superior instalado.

---
