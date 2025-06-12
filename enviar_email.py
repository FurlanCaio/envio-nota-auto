# 📦 Módulos necessários
import smtplib  # Envia e-mails via servidor SMTP (Gmail, Outlook, etc.)
from email.mime.multipart import MIMEMultipart  # Permite juntar corpo + anexo no mesmo e-mail
from email.mime.text import MIMEText  # Permite escrever e-mails com texto (ou HTML)
from email.mime.base import MIMEBase  # Para manipular o anexo
from email import encoders  # Codifica o anexo para o formato do e-mail
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import unidecode

# recebe os dados do cliente
cliente = str(input("Nome do Cliente: "))
endereco = str(input("Endereço: "))
cpf_cnpj = str(input("CPF/CNPJ: "))
telefone = str(input("Telefone: "))
veiculo = str(input("Veículo: "))
marca = str(input("Marca: "))
placa = str(input("Placa: "))
cor = str(input("Cor: "))
kilometragem = str(input("Kilometragem: "))
servico = str(input("Serviço: "))
valor = str(input("Valor: "))

primeiro_nome = unidecode.unidecode(cliente.split()[0])

    # Criação do documento PDF
documento_pdf = canvas.Canvas(f"valor_{primeiro_nome}.pdf", pagesize=A4)

    # Largura e altura da página A4 em pontos
largura_pagina, altura_pagina = A4


    # 🧩 Função para desenhar texto alinhado à direita
def escrever_alinhado_direita(canvas_pdf, texto, y, fonte="Helvetica", tamanho=12, margem_direita=30):
    largura_texto = canvas_pdf.stringWidth(texto, fonte, tamanho)
    posicao_x = largura_pagina - largura_texto - margem_direita
    canvas_pdf.setFont(fonte, tamanho)
    canvas_pdf.drawString(posicao_x, y, texto)


# 🖨️ Cabeçalho da nota fiscal
escrever_alinhado_direita(documento_pdf, "Auto Peças e Mecânica Furlan", 775, "Helvetica-Bold", 16)
escrever_alinhado_direita(documento_pdf, "CENTRO AUTOMOTIVO, AUTO PEÇAS, GUINCHO", 755, "Helvetica", 12, margem_direita=15)
escrever_alinhado_direita(documento_pdf, "CHAVEIRO, BATERIAS, PNEUS", 735, "Helvetica", 12, margem_direita=60)
escrever_alinhado_direita(documento_pdf, "CHAVE PIX CNPJ: 77.777.777.0001-77", 715, "Helvetica", 12)
escrever_alinhado_direita(documento_pdf, "WhatsApp (19) 98338-4106 Instagram: @furlanpy", 695, "Helvetica", 12)


# Logo
documento_pdf.drawImage("./furlan_logo.png", 40, 691, width=150, height=150)


# 📦 Função para escrever texto dentro de uma caixa com borda
def escrever_com_caixa(
    canvas_pdf,
    texto,
    x,
    y,
    fonte="Helvetica",
    tamanho=12,
    padding=5,
    cor_borda=(0, 0, 0),
    grossura_borda=1
):
    canvas_pdf.setFont(fonte, tamanho)
    largura_texto = canvas_pdf.stringWidth(texto, fonte, tamanho)
    altura_texto = tamanho * 1.2  # altura estimada da caixa

    # Desenha borda ao redor do texto
    canvas_pdf.setStrokeColorRGB(*cor_borda)
    canvas_pdf.setLineWidth(grossura_borda)
    canvas_pdf.rect(
        x - padding,
        y - padding,
        largura_texto + padding * 2,
        altura_texto + padding,
        stroke=1,
        fill=0
    )

    # Escreve o texto
    canvas_pdf.drawString(x, y, texto)

# 📋 Dados que serão escritos horizontalmente em caixas
dados = [
    f"Cliente: {cliente}",
    f"Endereço: {endereco}",
    f"CPF/CNPJ: {cpf_cnpj}",
    f"Telefone: {telefone}",
    f"Veículo/Ano: {veiculo}",
    f"Marca: {marca}",
    f"Placa: {placa}",
    f"Cor: {cor}",
    f"Kilometragem: {kilometragem}",
    f"Serviço prestado: {servico}"
]

# 🧠 Lógica para posicionamento horizontal com quebra de linha
x_inicial = 50
y_inicial = 600
x = x_inicial
y = y_inicial

espaco_horizontal = 5  # espaço entre as caixas
espaco_vertical = 30    # altura entre linhas
padding = 5             # usado nas caixas

# Itera e posiciona cada texto em grade horizontal
for texto in dados:
    # Calcula largura do texto com padding
    largura_texto = documento_pdf.stringWidth(texto, "Helvetica", 12)
    largura_caixa = largura_texto + padding * 2

    # Verifica se ainda cabe na linha
    if x + largura_caixa > largura_pagina - 20:
        x = x_inicial + espaco_horizontal
        y -= espaco_vertical

    escrever_com_caixa(documento_pdf, texto, x, y, tamanho=12, padding=padding)
    x += largura_caixa # avança para a próxima posição

documento_pdf.setFont("Helvetica-Bold", 14)
documento_pdf.drawString(50, 450, f"Orçamento: {valor} R$")

documento_pdf.drawString(50, 50, "Desenvolvido por Caio Furlan")



# 💾 Finaliza o PDF
documento_pdf.save()


def enviar_email_com_anexo():
    global cliente
    remetente = 'SEU_EMAIL_AQUI@gmail.com'  # Seu e-mail
    destinatario = 'EMAIL_DO_CLIENTE@gmail.com'  # Quem vai receber o e-mail
    senha = 'SENHA_DO_APP'  # Senha gerada no Gmail (não a senha da conta)

    mensagem = MIMEMultipart()  # Cria o e-mail com várias "partes": corpo + anexo
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = 'Email com Anexo - Projeto 2'

    corpo = f"""
    <p>Olá {cliente},</p>
    <p>Segue em anexo o orçamento solicitado.</p>
    """
    mensagem.attach(MIMEText(corpo, 'html'))  # Adiciona o corpo HTML ao e-mail

    nome_arquivo = f'valor_{primeiro_nome}.pdf'  # Nome do PDF que será enviado

    with open(nome_arquivo, 'rb') as anexo:  # Abre o PDF em modo leitura binária
        parte = MIMEBase('application', 'octet-stream')  # Tipo genérico de anexo
        parte.set_payload(anexo.read())  # Lê o conteúdo do arquivo e coloca no "payload"
        encoders.encode_base64(parte)  # Codifica o arquivo em base64 para ser enviado por e-mail
        parte.add_header('Content-Disposition', f'attachment; filename="{nome_arquivo}"')  # Define o nome do arquivo que será exibido
        mensagem.attach(parte)  # Anexa o arquivo ao e-mail

    # responsável por enviar o email
    servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Conecta ao servidor do Gmail
    servidor.starttls()  # Inicia conexão segura (criptografada)
    servidor.login(remetente, senha)  # Faz login com seu e-mail e senha de app
    servidor.sendmail(remetente, destinatario, mensagem.as_string())  # Envia o e-mail montado
    servidor.quit()  # Encerra a conexão

    print("Email com anexo enviado com sucesso!")  # Confirma o envio

enviar_email_com_anexo() # chama a função para enviar o email com o anexo



