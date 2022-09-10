FROM tiangolo/uvicorn-gunicorn:python3.8-slim
COPY . .
RUN pip install setuptools==45
RUN pip install -r requirements.txt