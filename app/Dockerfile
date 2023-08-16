# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/genandlam/streamlit-docker.git .

#COPY . /Users/genevievelam/Documents/GitHub/streamlit-docker/data /app/

RUN pip install -r requirements.txt

EXPOSE 8800

HEALTHCHECK CMD curl --fail http://localhost:8800/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8800", "--server.address=0.0.0.0"]
