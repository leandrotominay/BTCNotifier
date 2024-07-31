# Use uma imagem base do Selenium com Chrome
FROM selenium/standalone-chrome:latest

# Instale o Python e ferramentas necessárias
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Crie e ative um ambiente virtual
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Configurações do diretório de trabalho
WORKDIR /app

# Copie o código da aplicação para o contêiner
COPY . .

# Instale as dependências Python no ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

RUN chromedriver --version

# Comando para executar a aplicação
CMD ["python", "app.py"]
