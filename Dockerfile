FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY main.py .
COPY .streamlit/secrets.toml /app/.streamlit/secrets.toml
EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
