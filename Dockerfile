FROM python:3.10.4-slim as builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip &&\
    pip install --user -r requirements.txt
FROM python:3.10.4-slim
RUN useradd appuser && mkdir -p /app
USER appuser
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
COPY --chown=appuser:appuser . /app
ENV PATH=/home/appuser/.local/bin:$PATH
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]