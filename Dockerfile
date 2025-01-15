# Usando a imagem oficial do Python
FROM python:3.12

# Setando o diretório de trabalho no container
WORKDIR /app

# Copiando o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instalando as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos para o container
COPY . /app/

# Expondo a porta 8501 para o Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "main.py"]
