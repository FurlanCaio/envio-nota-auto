# 📩 Emissor de Orçamentos Automotivo com Envio por Email (Python)

Este projeto consiste em um sistema simples de emissão de orçamentos para oficinas mecânicas. Ele gera um PDF contendo os dados do cliente e do serviço prestado e envia o documento automaticamente por e-mail, com anexo, através do Gmail.

---

## 🚀 Funcionalidades

- Coleta de dados via terminal (nome, veículo, valor, etc.)
- Geração de orçamento personalizado em PDF com `reportlab`
- Envio automático por e-mail com `smtplib`
- Cabeçalho personalizado com logotipo e informações da oficina
- Estrutura de caixas organizadas no layout do PDF

---

## 📦 Bibliotecas Necessárias

Antes de executar, instale as dependências:

pip install reportlab unidecode

🔐 Como configurar o envio de e-mail com Gmail
Ative a verificação em duas etapas da sua conta Google.

Gere uma senha de app em: https://myaccount.google.com/apppasswords

Use essa senha gerada no lugar da sua senha do Gmail no código Python:


senha = 'SENHA_DO_APP'  # Essa não é a sua senha do gmail, é gerada pelo senha do app no google


⚠️ Nunca compartilhe essa senha publicamente!


python enviar_email.py

Preencha os dados solicitados e o PDF será criado e enviado automaticamente.

🔧 Possíveis melhorias futuras
Modularização do código (dividir em funções como gerar_pdf(), enviar_email(), etc.)

Interface gráfica com tkinter ou PyQt

Validação de CPF/CNPJ e campos obrigatórios

Log de erros e envio

Banco de dados para armazenar clientes e orçamentos

Suporte multiusuário ou multi-oficina

📹 Demonstração
Confira a demonstração em vídeo no LinkedIn: [https://www.linkedin.com/posts/caio-furlan-263978213_python-automacao-projetospython-activity-7338734358935011328-Pyhs?utm_source=share&utm_medium=member_desktop&rcm=ACoAADYSCmsB6rq9-gBW0dmvh6CWGekCESqX4Y0]

📬 Contato
Desenvolvido por Caio Furlan
📧 contato.cfurlan@gmail.com
🔗 [linkedin.com/in/caio-furlan-263978213]

