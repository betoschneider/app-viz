# Use uma imagem oficial do Python como base
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o diretório de trabalho
COPY . /app

# Defina o comando para rodar o Streamlit
CMD ["streamlit", "run", "main.py"]
