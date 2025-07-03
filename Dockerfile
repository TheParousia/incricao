# Usa uma imagem base Python oficial para sua versão do Django (por exemplo, 3.9, 3.10, 3.11)
FROM python:3.9-slim-buster

# Define variáveis de ambiente para o Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=core.settings 

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências do sistema operacional necessárias para o MySQL e outras bibliotecas
# O 'build-essential' é para compilar algumas dependências Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libmysqlclient-dev \
        default-libmysqlclient-dev \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências Python
# Isso é feito separadamente para aproveitar o cache do Docker (se os requisitos não mudarem, essa etapa não será refeita)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para o diretório de trabalho
COPY . /app/

# Coleta os arquivos estáticos do Django (opcional, dependendo de como você serve estáticos em produção)
# Se você usa um CDN ou um Nginx/Apache separado para servir estáticos, pode pular ou ajustar isso.
RUN python manage.py collectstatic --noinput

# Expõe a porta que o Gunicorn irá escutar
EXPOSE 8000

# Comando para iniciar o Gunicorn
# Substitua 'your_project_name.wsgi' pelo caminho correto para o seu arquivo WSGI
# O 'bind 0.0.0.0:8000' faz com que o Gunicorn escute em todas as interfaces na porta 8000
# Os workers podem ser ajustados com base nos recursos do seu servidor (2 * número de núcleos da CPU + 1 é uma boa regra geral)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core.wsgi:application"]