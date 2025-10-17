FROM python:3.11-slim
COPY main.py main.py
COPY books/ books/
CMD ["python", "main.py"]
